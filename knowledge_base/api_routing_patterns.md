---
category: Cloud Implementation
complexity: Medium
impact: AWS Scale
name: API routing patterns
provider: AWS
source: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/api-routing.html
---

# API routing patterns

## Overview
In agile development environments, autonomous teams (for example squads and tribes) own one
    or more services that include many microservices. The teams expose these services as APIs to
    allow their consumers to interact with their group of services and actions.

API routing patterns - AWS Prescriptive Guidance
 


API routing patterns - AWS Prescriptive Guidance
Documentation
AWS Prescriptive Guidance
Cloud design patterns, architectures, and implementations
API routing patterns
In agile development environments, autonomous teams (for example squads and tribes) own one
    or more services that include many microservices. The teams expose these services as APIs to
    allow their consumers to interact with their group of services and actions.
There are three major methods for exposing HTTP APIs to upstream consumers by using
    hostnames and paths:




Method


Description


Example






Hostname
                routing


Expose each service as a hostname.


billing.api.example.com






Path
              routing


Expose each service as a path.


api.example.com/billing






Header-based
                routing


Expose each service as an HTTP header.


x-example-action: something




This section outlines typical use cases for these three routing methods and their trade-offs
    to help you decide which method best fits your requirements and organizational structure.
 
Javascript is disabled or is unavailable in your browser.
To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.
Document Conventions
Anti-corruption layer pattern
Hostname routing
Did this page help you? - Yes
Thanks for letting us know we're doing a good job!
If you've got a moment, please tell us what we did right so we can do more of it.
Did this page help you? - No
Thanks for letting us know this page needs work. We're sorry we let you down.
If you've got a moment, please tell us how we can make the documentation better.