---
category: Cloud Implementation
complexity: Medium
impact: AWS Scale
name: Retry with backoff pattern
provider: AWS
source: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.html
---

# Retry with backoff pattern

## Overview
The retry with backoff pattern improves application stability by transparently retrying
      operations that fail due to transient errors.

Retry with backoff pattern - AWS Prescriptive Guidance
 


Retry with backoff pattern - AWS Prescriptive Guidance
Documentation
AWS Prescriptive Guidance
Cloud design patterns, architectures, and implementations
Intent
Motivation
Applicability
Issues and considerations
Implementation
Related content
Retry with backoff pattern


Intent


The retry with backoff pattern improves application stability by transparently retrying
      operations that fail due to transient errors.


Motivation


In distributed architectures, transient errors might be caused by service throttling,
      temporary loss of network connectivity, or temporary service unavailability. Automatically
      retrying operations that fail because of these transient errors improves the user experience
      and application resilience. However, frequent retries can overload network bandwidth and cause
      contention. Exponential backoff is a technique where operations are retried by increasing wait
      times for a specified number of retry attempts.


Applicability


Use the retry with backoff pattern when:






Your services frequently throttle the request to prevent overload, resulting in a
            
429 Too many requests
 exception to the calling process.




The network is an unseen participant in distributed architectures, and temporary
          network issues result in failures.




The service being called is temporarily unavailable, causing failures. Frequent
          retries might cause service degradation unless you introduce a backoff timeout by using
          this pattern.




Issues and considerations






Idempotency
: If multiple calls to the method have the
          same effect as a single call on the system state, the operation is considered idempotent.
          Operations should be idempotent when you use the retry with backoff pattern. Otherwise,
          partial updates might corrupt the system state.




Network bandwidth
: Service degradation can occur if
          too many retries occupy network bandwidth, leading to slow response times.




Fail fast scenarios
: For non-transient errors, if you
          can determine the cause of the failure, it is more efficient to fail fast by using the
          circuit breaker pattern.




Backoff rate
: Introducing exponential backoff can
          have an impact on the service timeout, resulting in longer wait times for the end
          user.




Implementation


High-level architecture


The following diagram illustrates how Service A can retry the calls to Service B until a
        successful response is returned. If Service B doesn't return a successful response
        after a few tries, Service A can stop retrying and return a failure to its caller.








Implementation using AWS services


The following diagram shows a ticket processing workflow on a customer support platform.
        Tickets from unhappy customers are expedited by automatically escalating the ticket
        priority. The 
Ticket info
 Lambda function extracts the ticket details and calls
        the 
Get sentiment
 Lambda function. The 
Get sentiment
 Lambda
        function checks the customer sentiments by passing the description to 
Amazon Comprehend
 (not shown).


If the call to the 
Get sentiment
 Lambda function fails, the workflow
        retries the operation three times. AWS Step Functions allows exponential backoff by letting
        you configure the backoff value.


In this example, a maximum of three retries are configured with an increase multiplier
        of 1.5 seconds. If the first retry occurs after 3 seconds, the second retry occurs after 3 x
        1.5 seconds = 4.5 seconds, and the third retry occurs after 4.5 x 1.5 seconds = 6.75
        seconds. If the third retry is unsuccessful, the workflow fails. The backoff logic
        doesn't require any custom code―it's provided as a configuration by AWS Step Functions.








Sample code


The following code shows the implementation of the