---
category: Cloud Implementation
complexity: Medium
impact: AWS Scale
name: Event sourcing pattern
provider: AWS
source: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/event-sourcing.html
---

# Event sourcing pattern

## Overview
In event-driven architectures, the event sourcing pattern stores the events that result in a
   state change in a data store. This helps to capture and maintain a complete history of state
   changes, and promotes auditability, traceability, and the ability to analyze past states.

Event sourcing pattern - AWS Prescriptive Guidance
 


Event sourcing pattern - AWS Prescriptive Guidance
Documentation
AWS Prescriptive Guidance
Cloud design patterns, architectures, and implementations
Intent
Motivation
Applicability
Issues and considerations
Implementation
Blog references
Event sourcing pattern


Intent


In event-driven architectures, the event sourcing pattern stores the events that result in a
   state change in a data store. This helps to capture and maintain a complete history of state
   changes, and promotes auditability, traceability, and the ability to analyze past states.


Motivation


Multiple microservices can collaborate to handle requests, and they communicate through
   events. These events can result in a change in state (data). Storing event objects in the order
   in which they occur provides valuable information on the current state of the data entity and
   additional information about how it arrived at that state.


Applicability


Use the event sourcing pattern when:






An immutable history of the events that occur in an application is required for
     tracking.




Polyglot data projections are required from a single source of truth (SSOT).




Point-in time reconstruction of the application state is needed.




Long-term storage of application state isn't required, but you might want to
     reconstruct it as needed.




Workloads have different read and write volumes. For example, you have write-intensive
     workloads that don't require real-time processing.




Change data capture (CDC) is required to analyze the application performance and other
     metrics.




Audit data is required for all events that happen in a system for reporting and compliance
     purposes.




You want to derive what-if scenarios by changing (inserting, updating, or deleting) events
     during the replay process to determine the possible end state.




Issues and considerations






Optimistic concurrency control: 
This pattern stores every
     event that causes a state change in the system. Multiple users or services can try to update
     the same piece of data at the same time, causing event collisions. These collisions happen when
     conflicting events are created and applied at the same time, which results in a final data
     state that doesn't match reality. To solve this issue, you can implement strategies to
     detect and resolve event collisions. For example, you can implement an optimistic concurrency
     control scheme by including versioning or by adding timestamps to events to track the order of
     updates.




Complexity:
 Implementing event sourcing necessitates a
     shift in mindset from traditional CRUD operations to event-driven thinking. The replay process,
     which is used to restore the system to its original state, can be complex in order to ensure
     data idempotency. Event storage, backups, and snapshots can also add additional
     complexity.




Eventual consistency
: Data projections derived from the
     events are eventually consistent because of the latency in updating data by using the command
     query responsibility segregation (CQRS)  pattern or materialized views. When consumers
     process data from an event store and publishers send new data, the data projection or the
     application object might not represent the current state.




Querying
: Retrieving current or aggregate data from event
     logs can be more intricate and slower compared to traditional databases, particularly for
     complex queries and reporting tasks. To mitigate this issue, event sourcing is often
     implemented with the CQRS pattern.




Size and cost of the event store: 
The event store can
     experience exponential growth in size as events are continuously persisted, especially in
     systems that have high event throughput or extended retention periods. Consequently, you must
     periodically archive event data to cost-effective storage to prevent the ev