---
category: Cloud Implementation
complexity: Medium
impact: AWS Scale
name: Transactional outbox pattern
provider: AWS
source: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html
---

# Transactional outbox pattern

## Overview
The transactional outbox pattern resolves the dual write operations issue that occurs in
      distributed systems when a single operation involves both a database write operation and a
      message or event notification. A dual write operation occurs when an application writes to two
      different systems; for example, when a microservice needs to persist data in the database and
      send a message to notify other systems. A failure in one of these operations might result in
      inconsistent data.

Transactional outbox pattern - AWS Prescriptive Guidance
 


Transactional outbox pattern - AWS Prescriptive Guidance
Documentation
AWS Prescriptive Guidance
Cloud design patterns, architectures, and implementations
Intent
Motivation
Applicability
Issues and considerations
Implementation
Sample code
GitHub repository
Transactional outbox pattern


Intent


The transactional outbox pattern resolves the dual write operations issue that occurs in
      distributed systems when a single operation involves both a database write operation and a
      message or event notification. A dual write operation occurs when an application writes to two
      different systems; for example, when a microservice needs to persist data in the database and
      send a message to notify other systems. A failure in one of these operations might result in
      inconsistent data.


Motivation


When a microservice sends an event notification after a database update, these two
      operations should run atomically to ensure data consistency and reliability.






If the database update is successful but the event notification fails, the downstream
          service will not be aware of the change, and the system can enter an inconsistent
          state.




If the database update fails but the event notification is sent, data could get
          corrupted, which might affect the reliability of the system.




Applicability


Use the transactional outbox pattern when:






You're building an event-driven application where a database update initiates an event
          notification .




You want to ensure atomicity in operations that involve two services.




You want to implement the 
event sourcing
          pattern
.




Issues and considerations






Duplicate messages
: The events processing service
          might send out duplicate messages or events, so we recommend that you make the consuming
          service idempotent by tracking the processed messages.




Order of notification
: Send messages or events in the
          same order in which the service updates the database. This is critical for the event
          sourcing pattern where you can use an event store for point-in-time recovery of the data
          store. If the order is incorrect, it might compromise the quality of the data. Eventual
          consistency and database rollback can compound the issue if the order of notifications
          isn't preserved.




Transaction rollback
: Do not send out an event
          notification if the transaction is rolled back.




Service-level transaction handling
: If the
          transaction spans services that require data store updates, use the 
saga orchestration pattern
 to preserve data
          integrity across the data stores.




Implementation


High-level architecture


The following sequence diagram shows the order of events that happen during dual write
        operations.












The flight service writes to the database and sends out an event notification to the
            payment service.




The message broker carries the messages and events to the payment service. Any
            failure in the message broker prevents the payment service from receiving the
            updates.




If the flight database update fails but the notification is sent out, the payment
        service will process the payment based on the event notification. This will cause downstream
        data inconsistencies.


Implementation using AWS services


To demonstrate the pattern in the sequence diagram, we will use the following AWS
        services, as shown in the following diagram.






Microservices are implemented by using 
AWS Lambda
.




The primary database is managed by 
Amazon Relational Database Service
              (Amazon RDS) 
.




Amazon Simple Queue Service (Amazon SQS)
 acts as the message
            broker that receives event notifications.










If the flight service fails after committing the transaction,