# 🏗️ Shadow Architect (System Design Agent)

A powerful, stateful multi-agent system designed to architect entire software ecosystems. **Shadow Architect** doesn't just suggest tools; it maintains a persistent knowledge graph, researches modern design patterns via RAG, and validates technical stacks in real-time using the Model Context Protocol (MCP).

---

## 🚀 The Vision
Shadow Architect acts as a "Senior System Architect" in your pocket. It interviews you for requirements, searches an industry-standard knowledge base of design patterns, proposes a vetted technical stack, and uses real-time signals from PyPI and GitHub to ensure your architecture is modern and maintainable.

### **Key Features**
- **🧠 Agentic Memory**: Tracks architectural decisions across nodes using a stateful LangGraph workflow.
- **📚 RAG-Powered Intelligence**: Uses ChromaDB seeded with 40+ official Azure Cloud Design Patterns (CQRS, Circuit Breaker, Saga, etc.).
- **🛠️ Real-Time Validation (MCP)**: Integrated with the Model Context Protocol to verify library versions, maintenance status, and deprecation risks.
- **🔄 Iterative Refinement**: If the "Scout" agent detects an outdated or unpopular library, the system automatically cycles back to the "Architect" for a better alternative.

---

## 🛠️ Project Structure

The project is organized for high modularity and industrial standards:

```text
.
├── shadow_architect/       # 🧠 Core Package
│   ├── agents/             # Multi-agent implementations (Interviewer, Researcher, etc.)
│   ├── core/               # LangGraph orchestrator and state definitions
│   ├── scripts/            # Internal utility scripts (KB Sync, etc.)
│   └── utils/              # MCP Clients, RAG Managers, and API Wrappers
├── tests/                  # 🧪 Test Suite (MCP & Researcher verification)
├── docs/                   # 📖 Research documentation and Sprint logs (Git Ignored)
├── knowledge_base/         # 📁 Source markdown for the RAG system
├── chroma_db/              # 🗄️ Vector Database (Local persistence)
├── README.md               # 🏠 You are here
├── main.py                 # 🚀 Application Entry Point
└── pyproject.toml          # 📦 Dependency Management (uv)
```

---

## 🚦 Getting Started

### **Prerequisites**
- **Python 3.10+**
- [**uv**](https://github.com/astral-sh/uv) (Highly recommended for lightning-fast dependency management)

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/SHREENIDHI1903/System-Design-Agent.git
   cd System-Design-Agent
   ```
2. Install dependencies:
   ```bash
   uv sync
   ```

### **Running the Architect**
Start the multi-agent workflow:
```bash
python main.py
```

### **Running Tests**
Verify the MCP and Researcher logic:
```bash
python -m tests.test_mcp
python -m tests.test_research
```

---

## 🗺️ Roadmap (The Sprints)

- [x] **Sprint 1: The Backbone** – Established LangGraph topology and state management.
- [x] **Sprint 2: The Brain** – Integrated ChromaDB with 42+ Cloud Design Patterns.
- [x] **Sprint 3: The Hands** – Implemented MCP-based real-time package verification.
- [ ] **Sprint 4: The Memory** – Adding SQLite checkpointers and final Markdown/Docker-compose artifact generation.

---

## 🛡️ License
Distributed under the MIT License. See `LICENSE` for more information.

---
*Created by [SHREENIDHI1903](https://github.com/SHREENIDHI1903)*
