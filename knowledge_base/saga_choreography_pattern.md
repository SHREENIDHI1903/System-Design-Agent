---
category: Cloud Implementation
complexity: Medium
impact: AWS Scale
name: Saga choreography pattern
provider: AWS
source: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/saga-choreography.html
---

# Saga choreography pattern

## Overview
The saga choreography pattern helps preserve data integrity in distributed transactions
        that span multiple services by using event subscriptions. In a distributed transaction,
        multiple services can be called before a transaction is completed. When the services store
        data in different data stores, it can be challenging to maintain data consistency across
        these data stores.

Saga choreography pattern - AWS Prescriptive Guidance
 


Saga choreography pattern - AWS Prescriptive Guidance
Documentation
AWS Prescriptive Guidance
Cloud design patterns, architectures, and implementations
Intent
Motivation
Applicability
Issues and considerations
Implementation
Related content
Saga choreography pattern


Intent


The saga choreography pattern helps preserve data integrity in distributed transactions
        that span multiple services by using event subscriptions. In a distributed transaction,
        multiple services can be called before a transaction is completed. When the services store
        data in different data stores, it can be challenging to maintain data consistency across
        these data stores.


Motivation


A 
transaction
 is a single unit of work that might involve multiple
        steps, where all steps are completely executed or no step is executed, resulting in a data
        store that retains its consistent state. The terms 
atomicity, consistency,
          isolation, and durability (ACID)
 define the properties of a transaction.
        Relational databases provide ACID transactions to maintain data consistency.


To maintain consistency in a transaction, relational databases use the two-phase commit
        (2PC) method. This consists of a 
prepare phase
 and a 
commit
          phase
.






In the prepare phase, the coordinating process requests the transaction's
            participating processes (participants) to promise to either commit or roll back the
            transaction.




In the commit phase, the coordinating process requests the participants to commit
            the transaction. If the participants cannot agree to commit in the prepare phase, the
            transaction is rolled back.




In distributed systems that follow a database-per-service design pattern, the two-phase
        commit is not an option. This is because each transaction is distributed across various
        databases, and there is no single controller that can coordinate a process that's similar to
        the two-phase commit in relational data stores. In this case, one solution is to use the
        saga choreography pattern.


Applicability


Use the saga choreography pattern when:






Your system requires data integrity and consistency in distributed transactions that
            span multiple data stores.




The data store (for example, a NoSQL database) doesn't provide 2PC to provide ACID
            transactions, you need to update multiple tables within a single transaction, and
            implementing 2PC within the application boundaries would be a complex task.




A central controlling process that manages the participant transactions might become
            a single point of failure.




The saga participants are independent services and need to be loosely
            coupled.




There is communication between bounded contexts in a business domain.




Issues and considerations






Complexity: 
As the number of microservices
            increases, saga choreography can become difficult to manage because of the number of
            interactions between the microservices. Additionally, compensatory transactions and
            retries add complexities to the application code, which can result in maintenance
            overhead. Choreography is suitable when there are only a few participants in the saga,
            and you need a simple implementation with no single point of failure. When more
            participants are added, it becomes harder to track the dependencies between the
            participants by using this pattern.




Resilient implementation:
 In saga choreography,
            it's more difficult to implement timeouts, retries, and other resiliency patterns
            globally, compared with saga orchestration. Choreography must be implemented on
            individual components instead of at an orchestrator level.




Cyclic dependencies:
 The part