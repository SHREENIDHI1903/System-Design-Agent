from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import shutil

import glob
import frontmatter

class RAGManager:
    def __init__(self, persist_directory="./chroma_db", model_name="nomic-embed-text", kb_directory="./knowledge_base"):
        self.persist_directory = persist_directory
        self.kb_directory = kb_directory
        self.model_name = model_name
        self.embeddings = OllamaEmbeddings(model=self.model_name)
        self.vector_store = None

    def initialize_db(self, force_reseed=False):
        """Initializes ChromaDB and seeds it if necessary."""
        if force_reseed and os.path.exists(self.persist_directory):
            shutil.rmtree(self.persist_directory)
            print(f"Cleared existing DB at {self.persist_directory}")

        self.vector_store = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embeddings,
            collection_name="system_design_patterns"
        )
        
        # Check if we need to seed
        if len(self.vector_store.get()['ids']) == 0:
            print(f"Seeded database with documents from {self.kb_directory}...")
            self.seed_patterns()

    def seed_patterns(self):
        """Seeds the database with high-fidelity documents from the knowledge_base directory."""
        if not os.path.exists(self.kb_directory):
            print(f"Warning: Knowledge base directory {self.kb_directory} not found.")
            return

        md_files = glob.glob(os.path.join(self.kb_directory, "*.md"))
        docs = []

        for file_path in md_files:
            try:
                # Use python-frontmatter to parse YAML metadata and content
                post = frontmatter.load(file_path)
                content = post.content
                metadata = post.metadata
                
                # Ensure a name exists for identification
                pattern_name = metadata.get("name") or os.path.basename(file_path).replace(".md", "").replace("_", " ").title()
                
                # Combine metadata into Chroma's metadata field
                full_metadata = {
                    "name": pattern_name,
                    "source": file_path,
                    **metadata
                }
                
                # Add a descriptive "header" to the content to help retrieval focus on metadata
                enhanced_content = f"Pattern: {pattern_name}\nCategory: {metadata.get('category', 'General')}\nComplexity: {metadata.get('complexity', 'Medium')}\n\n{content}"
                
                docs.append(Document(page_content=enhanced_content, metadata=full_metadata))
            except Exception as e:
                print(f"Error parsing metadata from {file_path}: {str(e)}")

        if docs:
            self.vector_store.add_documents(docs)
            print(f"Successfully seeded {len(docs)} high-fidelity patterns.")
        else:
            print("No valid documents found for seeding.")

    def get_retriever(self, k=3):
        """Returns a retriever for the vector store."""
        if not self.vector_store:
            self.initialize_db()
        return self.vector_store.as_retriever(search_kwargs={"k": k})
