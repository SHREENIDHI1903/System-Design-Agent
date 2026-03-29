---
category: Cloud Implementation
complexity: Medium
impact: AWS Scale
name: Strangler fig pattern
provider: AWS
source: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/strangler-fig.html
---

# Strangler fig pattern

## Overview
The strangler fig pattern helps migrate a monolithic application to a microservices
      architecture incrementally, with reduced transformation risk and business disruption.

Strangler fig pattern - AWS Prescriptive Guidance
 


Strangler fig pattern - AWS Prescriptive Guidance
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
Strangler fig pattern


Intent


The strangler fig pattern helps migrate a monolithic application to a microservices
      architecture incrementally, with reduced transformation risk and business disruption.


Motivation


Monolithic applications are developed to provide most of their functionality within a
      single process or container. The code is tightly coupled. As a result, application changes
      require thorough retesting to avoid regression issues. The changes cannot be tested in
      isolation, which impacts the cycle time. As the application is enriched with more features,
      high complexity can lead to more time spent on maintenance, increased time to market, and,
      consequently, slow product innovation.


When the application scales in size, it increases the cognitive load on the team and can
      cause unclear team ownership boundaries. Scaling individual features based on the load isn't
      possible—the entire application has to be scaled to support peak load. As the systems
      age, the technology can become obsolete, which drives up support costs. Monolithic, legacy
      applications follow best practices that were available at the time of development and weren't
      designed to be distributed.


When a monolithic application is migrated into a microservices architecture, it can be
      split into smaller components. These components can scale independently, can be released
      independently, and can be owned by individual teams. This results in a higher velocity of
      change, because changes are localized and can be tested and released quickly. Changes have a
      smaller scope of impact because components are loosely coupled and can be deployed
      individually.


Replacing a monolith completely with a microservices application by rewriting or
      refactoring the code is a huge undertaking and a big risk. A big bang migration, where the
      monolith is migrated in a single operation, introduces transformation risk and business
      disruption. While the application is being refactored, it is extremely hard or even impossible
      to add new features.


One way to resolve this issue is to use the strangler fig pattern, which was introduced by
      Martin Fowler. This pattern involves moving to microservices by gradually extracting features
      and creating a new application around the existing system. The features in the monolith are
      replaced by microservices gradually, and application users are able to use the newly migrated
      features progressively. When all features are moved out to the new system, the monolithic
      application can be decommissioned safely.


Applicability


Use the strangler fig pattern when:






You want to migrate your monolithic application gradually to a microservices
          architecture.




A big bang migration approach is risky because of the size and complexity of the
          monolith.




The business wants to add new features and cannot wait for the transformation to be
          complete.




End users must be minimally impacted during the transformation.




Issues and considerations






Code base access:
 To implement the strangler fig
          pattern, you must have access to the monolith application's code base. As features are
          migrated out of the monolith, you will need to make minor code changes and implement an
          anti-corruption layer within the monolith to route calls to new microservices. You cannot
          intercept calls without code base access. Code base access is also critical for
          redirecting incoming requests―some code refactoring might be required so that the p