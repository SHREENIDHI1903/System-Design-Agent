---
category: Cloud Implementation
complexity: Medium
impact: AWS Scale
name: HTTP header routing pattern
provider: AWS
source: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/api-routing-http.html
---

# HTTP header routing pattern

## Overview
Header-based routing enables you to target the correct service for each request by
      specifying an HTTP header in the HTTP request. For example, sending the header
        x-service-a-action: get-thing would enable you to get thing from
        Service A. The path of the request is still important, because it offers
      guidance on which resource you're trying to work on.

HTTP header routing pattern - AWS Prescriptive Guidance
 


HTTP header routing pattern - AWS Prescriptive Guidance
Documentation
AWS Prescriptive Guidance
Cloud design patterns, architectures, and implementations
Pros
Cons
HTTP header routing pattern
Header-based routing enables you to target the correct service for each request by
      specifying an HTTP header in the HTTP request. For example, sending the header
        
x-service-a-action: get-thing
 would enable you to 
get thing
 from
        
Service A
. The path of the request is still important, because it offers
      guidance on which resource you're trying to work on.
In addition to using HTTP header routing for actions, you can use it as a mechanism for
      version routing, enabling feature flags, A/B tests, or similar needs. In reality, you will
      likely use header routing with one of the other routing methods to create robust APIs.
The architecture for HTTP header routing typically has a thin routing layer in front of
      microservices that routes to the correct service and returns a response, as illustrated in the
      following diagram. This routing layer could cover all services or just a few services to
      enable an operation such as version-based routing.






Pros


Configuration changes require minimal effort and can be automated easily. This method is
        also flexible and supports creative ways to expose only specific operations you would want
        from a service.


Cons


As with the hostname routing method, HTTP header routing assumes that you have full
        control over the client and can manipulate custom HTTP headers. Proxies, content delivery
        networks (CDNs), and load balancers can limit the header size. Although this is unlikely to
        be a concern, it could be an issue depending on how many headers and cookies you add.


 
Javascript is disabled or is unavailable in your browser.
To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.
Document Conventions
Path routing
Circuit breaker pattern
Did this page help you? - Yes
Thanks for letting us know we're doing a good job!
If you've got a moment, please tell us what we did right so we can do more of it.
Did this page help you? - No
Thanks for letting us know this page needs work. We're sorry we let you down.
If you've got a moment, please tell us how we can make the documentation better.