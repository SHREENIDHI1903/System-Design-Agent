---
name: API Gateway
category: Edge Interface
complexity: High
impact: Security/Abstraction
related_patterns: [BFF, Strangler Fig]
---

# API Gateway

## Overview
A single entry point for all client requests, providing request routing, composition, and policy enforcement.

## Trade-offs

### Pros
* Centralized security (Auth/SSL)
* Request aggregation and abstraction
* Protocol translation

### Cons
* Single point of failure
* Bottleneck risk if not scaled correctly
* Logic creep in the gateway

## Use Cases
* Public-facing APIs
* Service mesh entrypoints
* Universal auth/metering layer

## Implementation Advice
This pattern should be considered when architectural requirements prioritize **Security/Abstraction**. For successful implementation, ensure that **High** engineering resources are allocated for monitoring and management. For hybrid architectures, consider integration with **[BFF, Strangler Fig]**.
