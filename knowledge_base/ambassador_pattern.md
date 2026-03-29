---
name: Ambassador Pattern
category: Networking
complexity: Medium
impact: Resilience
related_patterns: [Sidecar Pattern, Circuit Breaker]
---

# Ambassador Pattern

## Overview
A specialized sidecar that handles offloaded networking tasks like logging, security, and request routing.

## Trade-offs

### Pros
* Offloads SDK complexity from app code
* Centralized policy enforcement
* Transparent to the application

### Cons
* Extra network hop
* Configuration management challenges
* Resource duplication

## Use Cases
* Legacy system modernization
* Standardized auth/logging
* Traffic splitting (Canary/AB)

## Implementation Advice
This pattern should be considered when architectural requirements prioritize **Resilience**. For successful implementation, ensure that **Medium** engineering resources are allocated for monitoring and management. For hybrid architectures, consider integration with **[Sidecar Pattern, Circuit Breaker]**.
