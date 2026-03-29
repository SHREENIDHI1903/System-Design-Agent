---
name: Backend for Frontend (BFF)
category: API Design
complexity: Medium
impact: Performance/DevX
related_patterns: [API Gateway, Strangler Fig]
---

# Backend for Frontend (BFF)

## Overview
Creates separate backend services tailored to the specific needs of different client types (Mobile, Web, IoT).

## Trade-offs

### Pros
* Optimized data schemas per client
* Reduced over-fetching/under-fetching
* Parallel frontend development

### Cons
* Potential for code duplication
* Increased operational footprint
* Management of multiple BFF services

## Use Cases
* Multi-platform mobile apps
* Performance-critical web dashboards
* Low-bandwidth IoT devices

## Implementation Advice
This pattern should be considered when architectural requirements prioritize **Performance/DevX**. For successful implementation, ensure that **Medium** engineering resources are allocated for monitoring and management. For hybrid architectures, consider integration with **[API Gateway, Strangler Fig]**.
