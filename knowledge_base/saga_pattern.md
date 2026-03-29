---
name: Saga Pattern
category: Distributed Transactions
complexity: High
impact: Consistency
related_patterns: [Event Sourcing, Pub/Sub]
---

# Saga Pattern

## Overview
Manages distributed transactions across multiple microservices using a sequence of local transactions and compensating actions.

## Trade-offs

### Pros
* Maintains eventual consistency
* No distributed locks required
* Resilient to partial failures

### Cons
* Complex error handling (compensations)
* Risk of 'cyclic' dependencies
* Hard to debug distributed traces

## Use Cases
* Distributed order processing
* Booking/reservation systems
* Multi-step account registration

## Implementation Advice
This pattern should be considered when architectural requirements prioritize **Consistency**. For successful implementation, ensure that **High** engineering resources are allocated for monitoring and management. For hybrid architectures, consider integration with **[Event Sourcing, Pub/Sub]**.
