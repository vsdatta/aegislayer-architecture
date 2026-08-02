# AegisLayer Glossary

This glossary defines terms used across the public AegisLayer architecture, governance, and threat-model documentation.

## Agent

An AI-enabled system that can interpret goals, select actions, use tools, access data, or trigger workflows with some degree of autonomy.

## Approval

An explicit authorization decision made by a qualified human or system before a proposed action may proceed.

## Approval Gate

A control point that blocks execution until required approval conditions are satisfied.

## Artifact

A model, dataset, configuration, package, container, document, output, or other object used or produced by an AI system.

## Audit Trail

A chronological record of requests, decisions, approvals, actions, results, and changes used for review and accountability.

## Authority

The permission to perform a specific action within a defined scope, target, and period.

## Authorization

The process of determining whether a user, service, agent, or workload is permitted to perform a requested action.

## Capability

A specific action or class of actions that an actor, tool, connector, or runtime can perform.

## Capability Token

A scoped authorization object that grants limited permission to perform a defined capability under specified conditions.

## Causation Identifier

An identifier that links an event to the event or decision that caused it.

## Connector

An integration that allows an AI system or runtime to interact with an external tool, service, API, database, platform, or infrastructure component.

## Consequential Action

An action that may create material financial, legal, operational, security, safety, privacy, or reputational impact.

## Context

Information available to an AI system or control layer when evaluating a request, including identity, history, data, environment, risk, and policy state.

## Controlled Execution

Execution performed within explicit limits on permissions, tools, resources, duration, scope, and observable behavior.

## Correlation Identifier

An identifier used to associate related requests, events, decisions, evidence records, and execution steps.

## Data Classification

The process of labeling data according to sensitivity, handling requirements, and permitted use.

## Defense in Depth

A security approach that uses multiple independent and reinforcing controls rather than relying on a single safeguard.

## Delegated Authority

Authority granted by one actor to another under defined limits and conditions.

## Deny

A policy or authorization outcome that prevents a proposed action from proceeding.

## Evidence

Information recorded to support verification of identity, authority, policy decisions, approvals, execution, outcomes, and incidents.

## Evidence Chain

A sequence of related evidence records linked by order, identity, hashes, or correlation data to support integrity and reconstruction.

## Exception

A formally approved deviation from a policy or standard requirement.

## Execution Authority

Permission to carry out an action against a real system, resource, account, dataset, workflow, or environment.

## Execution Runtime

The environment responsible for carrying out an approved action under defined security and operational constraints.

## Fail-Closed

A control behavior in which execution stops, denies, or escalates when required trust conditions cannot be verified.

## Governance

The system of authority, policy, approvals, accountability, oversight, and evidence used to direct and control AI-related decisions and actions.

## Human Oversight

Review, approval, intervention, or accountability provided by a person for important AI decisions or actions.

## Identity

The verified representation of a user, service, workload, device, agent, or organization.

## Idempotency

A property in which repeating the same operation does not create unintended duplicate effects.

## Incident

An event that threatens or compromises confidentiality, integrity, availability, safety, policy compliance, or operational continuity.

## Integrity

Assurance that data, evidence, software, models, decisions, and records have not been altered in an unauthorized manner.

## Intent

The objective and meaning of a proposed request or action.

## Least Privilege

The principle that an actor should receive only the minimum access and authority required for a specific task.

## Model Artifact

A model file, adapter, weight set, configuration, tokenizer, or related package used to operate an AI model.

## Monitoring

Continuous or periodic observation of requests, decisions, actions, results, and security-relevant behavior.

## Non-Repudiation

The ability to provide evidence that a specific actor or system performed or approved an action, making later denial more difficult.

## Policy

A formal rule or set of rules that determines whether an action is allowed, denied, constrained, escalated, or subject to approval.

## Policy Decision

The result of evaluating a request against applicable policy and context.

## Policy Enforcement Point

A component that applies a policy decision by allowing, denying, constraining, or escalating execution.

## Prompt Injection

An attempt to manipulate an AI system through malicious or untrusted instructions embedded in user input, retrieved content, files, webpages, messages, or tool outputs.

## Provenance

Information describing the origin, history, ownership, and transformation of data, models, artifacts, instructions, or evidence.

## Requester

The user, service, agent, or system that initiates a proposed action.

## Residual Risk

Risk that remains after controls have been applied.

## Reversibility

The degree to which an action can be undone, compensated for, or restored without unacceptable harm.

## Risk Evaluation

The assessment of likelihood, impact, sensitivity, context, and control requirements associated with a proposed action.

## Runtime Constraint

A limit applied during execution, such as a permission boundary, timeout, quota, rate limit, target restriction, or resource cap.

## Scope

The defined boundaries of authority, including permitted actions, targets, resources, duration, data, and operating conditions.

## Secret

Sensitive authentication or cryptographic material such as a password, token, API key, private key, or credential.

## Separation of Duties

A governance principle that distributes critical responsibilities across multiple actors to reduce abuse, error, and conflicts of interest.

## Supply-Chain Risk

Risk introduced through third-party models, libraries, datasets, packages, containers, services, or build and deployment processes.

## Telemetry

Operational and security data generated by systems, including events, metrics, traces, counters, timings, and status information.

## Threat Actor

A person, organization, system, or compromised component capable of causing harm or violating security objectives.

## Threat Model

A structured analysis of assets, trust boundaries, threat actors, attack paths, controls, assumptions, and residual risk.

## Tool Use

The invocation of an external capability, connector, API, browser, terminal, database, application, or service by an AI system.

## Trust Boundary

A point where data, authority, identity, or control moves between components with different trust assumptions.

## Trust Context

The collection of identity, device, session, provenance, risk, and environmental information used to assess a request.

## Zero Trust

A security approach that does not grant implicit trust based only on location, network, ownership, or prior access, and instead requires continuous verification.

## Usage Note

These definitions are intended for this public repository. Specific implementations may use narrower or more formal definitions depending on legal, technical, or operational requirements.

Copyright © VND TECH LLC.
