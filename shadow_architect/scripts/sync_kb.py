import os
import requests
from bs4 import BeautifulSoup
import frontmatter
from typing import Dict
import time

class KBSyncTool:
    def __init__(self, kb_dir="knowledge_base"):
        self.kb_dir = kb_dir
        if not os.path.exists(self.kb_dir):
            os.makedirs(self.kb_dir)

    def fetch_azure_pattern(self, url: str) -> Dict:
        try:
            response = requests.get(url, timeout=15)
            soup = BeautifulSoup(response.content, "lxml")
            title = soup.find("h1").text.replace(" pattern", "").strip() if soup.find("h1") else "Unknown"
            description = soup.find("meta", {"name": "description"})
            summary = description["content"] if description else ""
            content_div = soup.find("div", {"class": "content"}) or soup.find("main")
            
            # Category inference
            text = soup.get_text().lower()
            if "reliability" in text: category = "Reliability"
            elif "data management" in text: category = "Data Management"
            elif "efficiency" in text: category = "Performance Efficiency"
            elif "security" in text: category = "Security"
            else: category = "General Architecture"

            return {
                "name": title,
                "category": category,
                "complexity": "Medium",
                "impact": "Architecture Scale",
                "source": url,
                "provider": "Microsoft Azure",
                "overview": summary,
                "full_content": content_div.get_text(separator="\n") if content_div else ""
            }
        except Exception as e:
            print(f"Error Azure {url}: {e}")
            return None

    def fetch_aws_pattern(self, url: str) -> Dict:
        try:
            response = requests.get(url, timeout=15)
            soup = BeautifulSoup(response.content, "lxml")
            title = soup.find("h1").text.strip() if soup.find("h1") else "AWS Pattern"
            summary = ""
            ps = soup.find_all("p")
            if ps: summary = ps[0].text.strip()

            return {
                "name": title,
                "category": "Cloud Implementation",
                "complexity": "Medium",
                "impact": "AWS Scale",
                "source": url,
                "provider": "AWS",
                "overview": summary,
                "full_content": soup.get_text(separator="\n")
            }
        except Exception as e:
            print(f"Error AWS {url}: {e}")
            return None

    def save(self, data: Dict):
        if not data: return
        filename = data["name"].lower().replace(" ", "_").replace("-", "_").strip("_") + ".md"
        path = os.path.join(self.kb_dir, filename)
        post = frontmatter.Post(data["full_content"][:4000], # Keep a healthy amount for RAG
                                name=data["name"],
                                category=data["category"],
                                complexity=data["complexity"],
                                impact=data["impact"],
                                source=data["source"],
                                provider=data["provider"])
        post.content = f"# {data['name']}\n\n## Overview\n{data['overview']}\n\n" + post.content
        with open(path, "wb") as f:
            frontmatter.dump(post, f)
        print(f"Synced {data['provider']}: {data['name']}")

if __name__ == "__main__":
    sync = KBSyncTool()
    azure_urls = [
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/ambassador",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/asynchronous-request-reply",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/backends-for-frontends",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/choreography",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/claim-check",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/competing-consumers",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/compute-resource-consolidation",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/deployment-stamp",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/external-configuration-store",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/federated-identity",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/gateway-aggregation",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/gateway-offloading",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/gateway-routing",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/geodes",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/health-endpoint-monitoring",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/index-table",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/leader-election",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/materialized-view",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/messaging-bridge",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/pipes-and-filters",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/priority-queue",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/publisher-subscriber",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/quarantine",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/queue-based-load-leveling",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/rate-limiting-pattern",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/retry",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/saga",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/scheduler-agent-supervisor",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/sequential-convoy",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/sharding",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/sidecar",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/static-content-hosting",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/throttling",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/valet-key"
    ]
    aws_urls = [
        "https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/acl.html",
        "https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/api-routing.html",
        "https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/api-routing-hostname.html",
        "https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/api-routing-path.html",
        "https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/api-routing-http.html",
        "https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/circuit-breaker.html",
        "https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/event-sourcing.html",
        "https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/hexagonal-architecture.html",
        "https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/publish-subscribe.html",
        "https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.html",
        "https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/saga.html",
        "https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/saga-choreography.html",
        "https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/saga-orchestration.html",
        "https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/scatter-gather.html",
        "https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/strangler-fig.html",
        "https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html"
    ]

    print(f"--- Starting Sync for {len(azure_urls)} Azure Patterns ---")
    for url in azure_urls:
        sync.save(sync.fetch_azure_pattern(url))
        time.sleep(0.5)

    print(f"\n--- Starting Sync for {len(aws_urls)} AWS Patterns ---")
    for url in aws_urls:
        sync.save(sync.fetch_aws_pattern(url))
        time.sleep(0.5)
