---
category: Cloud Implementation
complexity: Medium
impact: AWS Scale
name: Hexagonal architecture pattern
provider: AWS
source: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/hexagonal-architecture.html
---

# Hexagonal architecture pattern

## Overview
The hexagonal architecture pattern, which is also known as the ports and adapters
            pattern, was proposed by Dr. Alistair Cockburn in 2005. It aims to create loosely
            coupled architectures where application components can be tested independently, with no
            dependencies on data stores or user interfaces (UIs). This pattern helps prevent
            technology lock-in of data stores and UIs. This makes it easier to change the technology
            stack over time, with limited or no impact to business logic.
            In this loosely coupled architecture, the application communicates with external components 
            over interfaces called ports, and uses adapters 
            to translate the technical exchanges with these components.

Hexagonal architecture pattern - AWS Prescriptive Guidance
 


Hexagonal architecture pattern - AWS Prescriptive Guidance
Documentation
AWS Prescriptive Guidance
Cloud design patterns, architectures, and implementations
Intent
Motivation
Applicability
Issues and considerations
Implementation
Related content
Videos
Hexagonal architecture pattern


Intent


The hexagonal architecture pattern, which is also known as the ports and adapters
            pattern, was proposed by Dr. Alistair Cockburn in 2005. It aims to create loosely
            coupled architectures where application components can be tested independently, with no
            dependencies on data stores or user interfaces (UIs). This pattern helps prevent
            technology lock-in of data stores and UIs. This makes it easier to change the technology
            stack over time, with limited or no impact to business logic.
            In this loosely coupled architecture, the application communicates with external components 
            over interfaces called 
ports
, and uses 
adapters
 
            to translate the technical exchanges with these components.


Motivation


The hexagonal architecture pattern is used to isolate business logic (domain logic)
            from related infrastructure code, such as code to access a database or external APIs.
            This pattern is useful for creating loosely coupled business logic and infrastructure
            code for AWS Lambda functions that require integration with external services. In
            traditional architectures, a common practice is to embed business logic in the database
            layer as stored procedures and in the user interface. This practice, along with using
            UI-specific constructs within business logic, leads to closely coupled architectures
            that cause bottlenecks in database migrations and user experience (UX) modernization
            efforts. The hexagonal architecture pattern enables you to design your systems and
            applications by purpose rather than by technology. This strategy results in easily
            exchangeable application components such as databases, UX, and service
            components.


Applicability


Use the hexagonal architecture pattern when:






You want to decouple your application architecture to create components that
                    can be fully tested.




Multiple types of clients can use the same domain logic.




Your UI and database components require periodical technology refreshes that
                    don't affect application logic.




Your application requires multiple input providers and output consumers, and
                    customizing the application logic leads to code complexity and lack of
                    extensibility.




Issues and considerations






Domain-driven design
: Hexagonal architecture
                    works especially well with domain-driven design (DDD). Each application
                    component represents a sub-domain in DDD, and hexagonal architectures can be
                    used to achieve loose coupling among application components.




Testability
: By design, a hexagonal
                    architecture uses abstractions for inputs and outputs. Therefore, writing unit
                    tests and testing in isolation become easier because of the inherent loose
                    coupling.




Complexity
: The complexity of separating
                    business logic from infrastructure code, when handled carefully, can bring great
                    benefits such as agility, test coverage, and technology adaptability. Otherwise,
                    issues can become complex to solve.




Maintenance overhead
:
 
The additional adapter code that makes the architecture pluggable
                    is justified only if the application component requires several input sources
                    and output destinations to write to, or when the inputs