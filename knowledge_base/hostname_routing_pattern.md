---
category: Cloud Implementation
complexity: Medium
impact: AWS Scale
name: Hostname routing pattern
provider: AWS
source: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/api-routing-hostname.html
---

# Hostname routing pattern

## Overview
Routing by hostname is a mechanism for isolating API services by giving each API its own
      hostname; for example, service-a.api.example.com or
        service-a.example.com.

Hostname routing pattern - AWS Prescriptive Guidance
 


Hostname routing pattern - AWS Prescriptive Guidance
Documentation
AWS Prescriptive Guidance
Cloud design patterns, architectures, and implementations
Typical use case
Pros
Cons
Hostname routing pattern
Routing by hostname is a mechanism for isolating API services by giving each API its own
      hostname; for example, 
service-a.api.example.com
 or
        
service-a.example.com
.


Typical use case


Routing by using hostnames reduces the amount of friction in releases, because nothing
        is shared between service teams. Teams are responsible for managing everything from DNS
        entries to service operations in production.








Pros


Hostname routing is by far the most straightforward and scalable method for HTTP API
        routing. You can use any relevant AWS service to build an architecture that follows this
        method―you can create an architecture with 
Amazon API Gateway
, 
AWS AppSync
, 
Application Load Balancers
 and 
Amazon Elastic Compute Cloud (Amazon EC2)
, or any other HTTP-compliant service.


Teams can use hostname routing to fully own their subdomain. It also makes it easier to
        isolate, test, and orchestrate deployments for specific AWS Regions or versions; for
        example, 
region.service-a.api.example.com
 or
          
dev.region.service-a.api.example.com
.


Cons


When you use hostname routing, your consumers have to remember different hostnames to
        interact with each API that you expose. You can mitigate this issue by providing a client
        SDK. However, client SDKs come with their own set of challenges. For example, they have to
        support rolling updates, multiple languages, versioning, communicating breaking changes
        caused by security issues or bug fixes, documentation, and so on.


When you use hostname routing, you also need to register the subdomain or domain every
        time you create a new service.


 
Javascript is disabled or is unavailable in your browser.
To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.
Document Conventions
API routing patterns
Path routing
Did this page help you? - Yes
Thanks for letting us know we're doing a good job!
If you've got a moment, please tell us what we did right so we can do more of it.
Did this page help you? - No
Thanks for letting us know this page needs work. We're sorry we let you down.
If you've got a moment, please tell us how we can make the documentation better.