---
name: Database per Service
category: Data Management
complexity: Medium
impact: Modularity/Isolation
related_patterns: [Saga Pattern]
---

# Database per Service

## Overview
Each microservice manages its own private data store to prevent tight coupling via a shared database schema.

## Trade-offs

### Pros
* Complete service isolation
* Independence in choice of database tech
* Scalability per data domain

### Cons
* Complex distributed transactions
* Difficult joined queries (Reporting)
* Increased operational overhead for DBs

## Use Cases
* Fully decoupled microservices
* Polyglot persistence environments
* Regulated data isolation

## Implementation Advice
This pattern should be considered when architectural requirements prioritize **Modularity/Isolation**. For successful implementation, ensure that **Medium** engineering resources are allocated for monitoring and management. For hybrid architectures, consider integration with **[Saga Pattern]**.
