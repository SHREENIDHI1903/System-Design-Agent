---
name: Bulkhead Pattern
category: Reliability
complexity: Low
impact: Isolation
related_patterns: [Circuit Breaker]
---

# Bulkhead Pattern

## Overview
Isolates system elements into separate pools (like bulkheads in a ship) so that a failure in one region doesn't exhaust all resources.

## Trade-offs

### Pros
* Prevents resource exhaustion
* Isolates impact of catastrophic failures
* Enables graceful degradation

### Cons
* Reduced resource efficiency (fragmentation)
* Increased operational monitoring
* Hard to define optimal pool sizes

## Use Cases
* Connection pool isolation
* Critical vs non-critical task scheduling
* Tenant-based resource partitioning

## Implementation Advice
This pattern should be considered when architectural requirements prioritize **Isolation**. For successful implementation, ensure that **Low** engineering resources are allocated for monitoring and management. For hybrid architectures, consider integration with **[Circuit Breaker]**.
