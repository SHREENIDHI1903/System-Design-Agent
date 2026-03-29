---
category: Cloud Implementation
complexity: Medium
impact: AWS Scale
name: Scatter-gather pattern
provider: AWS
source: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/scatter-gather.html
---

# Scatter-gather pattern

## Overview
The scatter-gather pattern is a message routing pattern that involves broadcasting
            similar or related requests to multiple recipients, and aggregating their responses back
            into a single message by using a component called an aggregator.
            This pattern helps achieve parallelization, reduces processing latency, and handles
            asynchronous communication. It's straightforward to implement the scatter-gather pattern
            by using a synchronous approach, but a more powerful approach involves implementing it
            as message routing in asynchronous communication, either with or without a messaging
            service.

Scatter-gather pattern - AWS Prescriptive Guidance
 


Scatter-gather pattern - AWS Prescriptive Guidance
Documentation
AWS Prescriptive Guidance
Cloud design patterns, architectures, and implementations
Intent
Motivation
Applicability
Issues and considerations
Implementation
Workshop
Blog references
Related content
Scatter-gather pattern


Intent


The scatter-gather pattern is a message routing pattern that involves broadcasting
            similar or related requests to multiple recipients, and aggregating their responses back
            into a single message by using a component called an 
aggregator
.
            This pattern helps achieve parallelization, reduces processing latency, and handles
            asynchronous communication. It's straightforward to implement the scatter-gather pattern
            by using a synchronous approach, but a more powerful approach involves implementing it
            as message routing in asynchronous communication, either with or without a messaging
            service.


Motivation


In application processing, a request that might take a long time to process
            sequentially can be split into multiple requests that are processed in parallel. You can
            also send requests to multiple external systems through API calls to get a response. The
            scatter-gather pattern is useful when you need input from multiple sources.
            Scatter-gather aggregates the results to help you make an informed decision or to select
            the best response for the request.


The scatter-gather pattern consists of two phases, as its name implies:






The 
scatter phase
 processes the request message and sends
                    it to multiple recipients in parallel. During this phase, the application
                    scatters requests across the network and continues to run without waiting for
                    immediate responses.




During the 
gather phase
, the application collects the
                    responses from recipients, and filters or combines them into a unified response.
                    When all the responses have been collected, they can either be aggregated into a
                    single response or the best one can be chosen for further processing.




Applicability


Use the scatter-gather pattern when:






You plan to aggregate and consolidate data from various APIs to create an
                    accurate response. The pattern consolidates information from disparate sources
                    into a cohesive whole. For example, a booking system can make a request to
                    multiple recipients to get quotes from multiple external partners.




The same request has to be sent to multiple recipients simultaneously to
                    complete a transaction. For example, you can use this pattern to query inventory
                    data in parallel to check a product's availability.




You want to implement a reliable and scalable system where load balancing can
                    be achieved by distributing requests across multiple recipients. If one
                    recipient fails or experiences a high load, other recipients can still process
                    requests.




You want to optimize performance when implementing complex queries that
                    involve multiple data sources. You can scatter the query to relevant databases,
                    gather the partial results, and combine them into a comprehensive answer.




You are implementing a type of map-reduce processing where the data request is
                    routed to multiple data processing endpoints for sharding and replication.
                    Partial results are filtered and combined to compose the right response.




You want to distribute write operations across a partition key space in
                    write-heavy workloads in key-value databases. The aggregator reads the results
                    by queryin