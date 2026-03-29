---
category: Cloud Implementation
complexity: Medium
impact: AWS Scale
name: Saga orchestration pattern
provider: AWS
source: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/saga-orchestration.html
---

# Saga orchestration pattern

## Overview
The saga orchestration pattern uses a central coordinator
          (orchestrator) to help preserve data integrity in distributed
        transactions that span multiple services. In a distributed transaction, multiple services
        can be called before a transaction is completed. When the services store data in different
        data stores, it can be challenging to maintain data consistency across these data
        stores.

Saga orchestration pattern - AWS Prescriptive Guidance
 


Saga orchestration pattern - AWS Prescriptive Guidance
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
Videos
Saga orchestration pattern


Intent


The saga orchestration pattern uses a central coordinator
          (
orchestrator
) to help preserve data integrity in distributed
        transactions that span multiple services. In a distributed transaction, multiple services
        can be called before a transaction is completed. When the services store data in different
        data stores, it can be challenging to maintain data consistency across these data
        stores.


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
        saga orchestration pattern.


Applicability


Use the saga orchestration pattern when:






Your system requires data integrity and consistency in distributed transactions that
            span multiple data stores.




The data store doesn't provide 2PC to provide ACID transactions, and implementing
            2PC within the application boundaries is a complex task.




You have NoSQL databases, which do not provide ACID transactions, and you need to
            update multiple tables within a single transaction.




Issues and considerations






Complexity
: Compensatory transactions and retries
            add complexities to the application code, which can result in maintenance
            overhead.




Eventual consistency
: The sequential processing of
            local transactions results in eventual consistency, which can be a challenge in systems
            that require strong consistency. You can address this issue by setting your business
            teams' expectations for the consistency model or by switching to a data store that
            provides strong consistency.




Idempotency
: Saga participants need to be
            idempotent to allow repeated execution in case of transient failures caused by
            unexpected crashes and orchestrator failures.




Transaction isolation
: Saga lacks transaction
            isolation. Concurrent orchestration of transactions can lead to stale data. We recommend
            using semantic locking to handle such scenarios.




Observability
: Observability refers to detailed
            logging and tracing to troubleshoot issues in the execution and orchestration process.
            This becomes important when the number of saga participants increases, resulting in