---
category: Cloud Implementation
complexity: Medium
impact: AWS Scale
name: Path routing pattern
provider: AWS
source: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/api-routing-path.html
---

# Path routing pattern

## Overview
Routing by paths is the mechanism of grouping multiple or all APIs under the same
      hostname, and using a request URI to isolate services; for example,
        api.example.com/service-a or api.example.com/service-b.

Path routing pattern - AWS Prescriptive Guidance
 


Path routing pattern - AWS Prescriptive Guidance
Documentation
AWS Prescriptive Guidance
Cloud design patterns, architectures, and implementations
Typical use case
HTTP service reverse proxy
API Gateway
CloudFront
Path routing pattern
Routing by paths is the mechanism of grouping multiple or all APIs under the same
      hostname, and using a request URI to isolate services; for example,
        
api.example.com/service-a
 or 
api.example.com/service-b
.


Typical use case


Most teams opt for this method because they want a simple architecture―a developer has
        to remember only one URL such as 
api.example.com
 to interact with the HTTP API.
        API documentation is often easier to digest because it is often kept together instead of
        being split across different portals or PDFs.


Path-based routing is considered a simple mechanism for sharing an HTTP API. However, it
        involves operational overhead such as configuration, authorization, integrations, and
        additional latency due to multiple hops. It also requires mature change management processes
        to ensure that a misconfiguration doesn't disrupt all services.


On AWS, there are multiple ways to share an API and route effectively to the correct
        service. The following sections discuss three approaches: HTTP service reverse proxy, API
        Gateway, and Amazon CloudFront. None of the suggested approaches for unifying API services relies on
        the downstream services running on AWS. The services could run anywhere without issue or
        on any technology, as long as they're HTTP-compatible.


HTTP service reverse proxy


You can use an HTTP server such as 
NGINX
 to
        create dynamic routing configurations. In a 
Kubernetes
 architecture, you can also create an ingress rule to match a path to a
        service. (This guide doesn't cover Kubernetes ingress; see the 
Kubernetes documentation
 for more information.)


The following configuration for NGINX dynamically maps an HTTP request of
          
api.example.com/my-service/
 to
          
my-service.internal.api.example.com
.


server 
{

    listen  80;

    location (^/[\w-]+)/(.*) 
{

        proxy_pass $scheme://$1.internal.api.example.com/$2;
    }
}


The following diagram illustrates the HTTP service reverse proxy method.










This approach might be sufficient for some use cases that don't use additional
        configurations to start processing requests, allowing for the downstream API to collect
        metrics and logs.


To get ready for operational production readiness, you will want to be able to add
        observability to every level of your stack, add additional configuration, or add scripts to
        customize your API ingress point to allow for more advanced features such as rate limiting
        or usage tokens.


Pros


The ultimate aim of the HTTP service reverse proxy method is to create a scalable and
          manageable approach to unifying APIs into a single domain so it appears coherent to any
          API consumer. This approach also enables your service teams to deploy and manage their own
          APIs, with minimal overhead after deployment. AWS managed services for tracing, such as
            
AWS X-Ray
 or 
AWS WAF
, are still applicable here.


Cons


The major downside of this approach is the extensive testing and management of
          infrastructure components that are required, although this might not be an issue if you
          have site reliability engineering (SRE) teams in place.


There is a cost tipping point with this method. At low to medium volumes, it is more
          expensive than some of the other methods discussed in this guide. At high volumes, it is
          very cost-effective (around 100K transactions per second or better).


API Gateway


The 
Amazon API Gateway
 service (REST APIs and
        HTTP APIs) can route traffic in a way that's similar