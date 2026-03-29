---
category: Cloud Implementation
complexity: Medium
impact: AWS Scale
name: Saga patterns
provider: AWS
source: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/saga.html
---

# Saga patterns

## Overview
A saga consists of a sequence of local transactions. Each local
    transaction in a saga updates the database and triggers the next local transaction. If a
    transaction fails, the saga runs compensating transactions to revert the database changes made
    by the previous transactions.

Saga patterns - AWS Prescriptive Guidance
 


Saga patterns - AWS Prescriptive Guidance
Documentation
AWS Prescriptive Guidance
Cloud design patterns, architectures, and implementations
Saga choreography
Saga orchestration
Saga patterns
A 
saga
 consists of a sequence of local transactions. Each local
    transaction in a saga updates the database and triggers the next local transaction. If a
    transaction fails, the saga runs compensating transactions to revert the database changes made
    by the previous transactions.
This sequence of local transactions helps achieve a business workflow by using continuation
    and compensation principles. The 
continuation principle
 decides the forward
    recovery of the workflow, whereas the 
compensation principle
 decides the
    backward recovery. If the update fails at any step in the transaction, the saga publishes an
    event for either continuation (to retry the transaction) or compensation (to go back to the
    previous data state). This ensures that data integrity is maintained and is consistent across
    the data stores.
For example, when a user purchases a book from an online retailer, the process consists of a
    sequence of transactions—such as order creation, inventory update, payment, and
    shipping—that represents a business workflow. In order to complete this workflow, the
    distributed architecture issues a sequence of local transactions to create an order in the order
    database, update the inventory database, and update the payment database. When the process is
    successful, these transactions are invoked sequentially to complete the business workflow, as
    the following diagram shows. However, if any of these local transactions fails, the system
    should be able to decide on an appropriate next step—that is, either a forward recovery
    or a backward recovery.




The following two scenarios help determine whether the next step is forward recovery or
    backward recovery:




Platform-level failure, where something goes wrong with the underlying infrastructure
        and causes the transaction to fail. In this case, the saga pattern can perform a forward
        recovery by retrying the local transaction and continuing the business process.




Application-level failure, where the payment service fails because of an invalid
        payment. In this case, the saga pattern can perform a backward recovery by issuing a
        compensatory transaction to update the inventory and the order databases, and reinstate
        their previous state.


The saga pattern handles the business workflow and ensures that a desirable end state is
    reached through forward recovery. In case of failures, it reverts the local transactions by
    using backward recovery to avoid data consistency issues.
The saga pattern has two variants: choreography and orchestration.


Saga choreography


The saga choreography pattern depends on the events published by the microservices. The
      saga participants (microservices) subscribe to the events and act based on the event triggers.
      For example, the order service in the following diagram emits an 
OrderPlaced

      event. The inventory service subscribes to that event and updates the inventory when the
        
OrderPlaced
 event is emitted. Similarly, the participant services act based on
      the context of the emitted event.


The saga choreography pattern is suitable when there are only a few participants in the
      saga, and you need a simple implementation with no single point of failure. When more
      participants are added, it becomes harder to track the dependencies between the participants
      by using this pattern.








For a detailed review, see the 
Saga choreography

      section of this guide.


Saga orchestration


The saga orchestration pattern has a central coordinator called an
        
orchestrator
. The saga orchestrator manages and coordinates the entire
      transaction lifecycle.