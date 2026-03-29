---
category: Cloud Implementation
complexity: Medium
impact: AWS Scale
name: Circuit breaker pattern
provider: AWS
source: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/circuit-breaker.html
---

# Circuit breaker pattern

## Overview
The circuit breaker pattern can prevent a caller service from retrying a call to another
      service (callee) when the call has previously caused repeated timeouts or
      failures. The pattern is also used to detect when the callee service is functional
      again.

Circuit breaker pattern - AWS Prescriptive Guidance
 


Circuit breaker pattern - AWS Prescriptive Guidance
Documentation
AWS Prescriptive Guidance
Cloud design patterns, architectures, and implementations
Intent
Motivation
Applicability
Issues and considerations
Implementation
Blog references
Related content
Circuit breaker pattern


Intent


The circuit breaker pattern can prevent a caller service from retrying a call to another
      service (
callee
) when the call has previously caused repeated timeouts or
      failures. The pattern is also used to detect when the callee service is functional
      again.


Motivation


When multiple microservices collaborate to handle requests, one or more services might
      become unavailable or exhibit high latency. When complex applications use microservices, an
      outage in one microservice can lead to application failure. Microservices communicate through
      remote procedure calls, and transient errors could occur in network connectivity, causing
      failures. (The transient errors can be handled by using the 
retry with backoff
 pattern.) During synchronous execution, the cascading of timeouts
      or failures can cause a poor user experience.


However, in some situations, the failures could take longer to resolve—for example, when
      the callee service is down or a database contention results in timeouts. In such cases, if the
      calling service retries the calls repeatedly, these retries might result in network contention
      and database thread pool consumption. Additionally, if multiple users are retrying the
      application repeatedly, this will make the problem worse and can cause performance degradation
      in the entire application.


The circuit breaker pattern was popularized by Michael Nygard in his book,
        
Release It
 (Nygard 2018). This design pattern can prevent a caller
      service from retrying a service call that has previously caused repeated timeouts or failures.
      It can also detect when the callee service is functional again.


Circuit breaker objects work like electrical circuit breakers that automatically interrupt
      the current when there is an abnormality in the circuit. Electrical circuit breakers shut off,
      or trip, the flow of the current when there is a fault. Similarly, the circuit breaker object
      is situated between the caller and the callee service, and trips if the callee is
      unavailable.


The 
fallacies of distributed computing
 are a set of assertions made by Peter Deutsch
      and others at Sun Microsystems. They say that programmers who are new to distributed
      applications invariably make false assumptions. The network reliability, zero-latency
      expectations, and bandwidth limitations result in software applications written with minimal
      error handling for network errors.


During a network outage, applications might indefinitely wait for a reply and continually
      consume application resources. Failure to retry the operations when the network becomes
      available can also lead to application degradation. If API calls to a database or an external
      service time out because of network issues, repeated calls with no circuit breaker can affect
      cost and performance.


Applicability


Use this pattern when:






The caller service makes a call that is most likely going to fail.




A high latency exhibited by the callee service (for example, when database connections
          are slow) causes timeouts to the caller service.




The caller service makes a synchronous call, but the callee service isn't available or
          exhibits high latency.




Issues and considerations






Service agnostic implementation:
 To prevent code
          bloat, we recommend that you implement the circuit breaker object in a
          microservice-agnostic and API-driven way.




Circuit closure by callee:
 When the callee recovers
          from the performance issue or fail