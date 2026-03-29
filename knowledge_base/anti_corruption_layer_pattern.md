---
category: Cloud Implementation
complexity: Medium
impact: AWS Scale
name: Anti-corruption layer pattern
provider: AWS
source: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/acl.html
---

# Anti-corruption layer pattern

## Overview
The anti-corruption layer (ACL) pattern acts as a mediation layer that translates domain
      model semantics from one system to another system. It translates the model of the upstream
      bounded context (monolith) into a model that suits the downstream bounded context
      (microservice) before consuming the communication contract that's established by the
      upstream team. This pattern might be applicable when the downstream bounded context contains a
      core subdomain, or the upstream model is an unmodifiable legacy system. It also reduces
      transformation risk and business disruption by preventing changes to callers when their calls
      have to be redirected transparently to the target system.

Anti-corruption layer pattern - AWS Prescriptive Guidance
 


Anti-corruption layer pattern - AWS Prescriptive Guidance
Documentation
AWS Prescriptive Guidance
Cloud design patterns, architectures, and implementations
Intent
Motivation
Applicability
Issues and considerations
Implementation
Related content
Anti-corruption layer pattern


Intent


The anti-corruption layer (ACL) pattern acts as a mediation layer that translates domain
      model semantics from one system to another system. It translates the model of the upstream
      bounded context (monolith) into a model that suits the downstream bounded context
      (microservice) before consuming the communication contract that's established by the
      upstream team. This pattern might be applicable when the downstream bounded context contains a
      core subdomain, or the upstream model is an unmodifiable legacy system. It also reduces
      transformation risk and business disruption by preventing changes to callers when their calls
      have to be redirected transparently to the target system.


Motivation


During the migration process, when a monolithic application is migrated into
      microservices, there might be changes in the domain model semantics of the newly migrated
      service. When the features within the monolith are required to call these microservices, the
      calls should be routed to the migrated service without requiring any changes to the calling
      services. The ACL pattern allows the monolith to call the microservices transparently by
      acting as an adapter or a facade layer that translates the calls into the newer
      semantics.


Applicability


Consider using this pattern when:






Your existing monolithic application has to communicate with a function that has been
          migrated into a microservice, and the migrated service domain model and semantics differ
          from the original feature.




Two systems have different semantics and need to exchange data, but it isn't
          practical to modify one system to be compatible with the other system.




You want to use a quick and simplified approach to adapt one system to another with
          minimal impact.




Your application is communicating with an external system.




Issues and considerations






Team dependencies:
 When different services in a
          system are owned by different teams, the new domain model semantics in the migrated
          services can lead to changes in the calling systems. However, teams might not be able to
          make these changes in a coordinated way, because they might have other priorities.
          ACL decouples the callees and translates the calls to match the semantics of the new
          services, thus avoiding the need for callers to make changes in the current system.




Operational overhead:
 The ACL pattern requires
          additional effort to operate and maintain. This work includes integrating ACL with
          monitoring and alerting tools, the release process, and continuous integration and
          continuous delivery (CI/CD) processes.




Single point of failure:
 Any failures in the ACL can
          make the target service unreachable, causing application issues. To mitigate this issue,
          you should build in retry capabilities and circuit breakers. See the 
retry with backoff
 and 
circuit breaker

          patterns to understand more about these options. Setting up appropriate alerts and logging
          will improve the mean time to resolution (MTTR).




Technical debt:
 As part of your migration or
          modernization strategy, consider whether the ACL will be a transient or interim solution,
          or a long-term solution. If it's an interim solution, you should record the ACL as a
          technical debt and decommission it after all dependent callers have been migrated.




Latency:
 The additional layer can introduce latency
          due to the conversion of requests f