---
name: Saga Pattern
category: Distributed Transactions
complexity: High
impact: Consistency
source: https://learn.microsoft.com/en-us/azure/architecture/patterns/saga
provider: Microsoft Azure
related_patterns: [Event Sourcing, Pub/Sub]
---

# Saga Pattern

## Overview
The Saga pattern manages data consistency across microservices in distributed transaction scenarios. A saga is a sequence of transactions that updates each service and publishes an event or message to trigger the next transaction step.

## Trade-offs

### Pros
* Maintains eventual consistency
* No distributed locks required
* Resilient to partial failures

### Cons
* Complex error handling (compensating transactions)
* Hard to debug distributed traces
* Cyclic dependency risks

## Use Cases
* Distributed order processing
* Booking/reservation systems
* Multi-step account registration

## Implementation Advice
According to the **Microsoft Azure Architecture Center**, this pattern should be considered when architectural requirements prioritize **Consistency**. For successful implementation, identify clear failure thresholds and ensure that the **High** engineering overhead is justified by the resiliency gains.
