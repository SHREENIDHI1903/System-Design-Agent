---
name: Pub/Sub (Publish-Subscribe)
category: Communication
complexity: Medium
impact: Decoupling/Scalability
related_patterns: [Saga Pattern, CQRS]
---

# Pub/Sub (Publish-Subscribe)

## Overview
An asynchronous messaging pattern where senders (publishers) do not send messages directly to specific receivers (subscribers).

## Trade-offs

### Pros
* Strong decoupling of services
* Easy to add new consumers
* Handles traffic spikes via buffering

### Cons
* Lack of immediate response (Async only)
* Risk of message delivery ordering issues
* Complexity of distributed messaging bus

## Use Cases
* Event-driven architectures
* Real-time analytics
* Cross-service notifications

## Implementation Advice
This pattern should be considered when architectural requirements prioritize **Decoupling/Scalability**. For successful implementation, ensure that **Medium** engineering resources are allocated for monitoring and management. For hybrid architectures, consider integration with **[Saga Pattern, CQRS]**.
