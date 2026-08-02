# AegisLayer Frequently Asked Questions

## What is AegisLayer?

AegisLayer is a public AI security and governance architecture initiative developed by VND TECH LLC. It explores how autonomous and agentic AI systems can be constrained by identity, authority, policy, approval, runtime controls, evidence, monitoring, and recovery mechanisms.

## Is AegisLayer a model?

No. AegisLayer is not presented as a single AI model. It is an architectural approach for governing and securing AI systems, agents, tools, data access, and execution workflows.

## Does AegisLayer guarantee that a system cannot be hacked?

No. No responsible security architecture should claim complete protection from every attack.

AegisLayer is intended to reduce risk, constrain unauthorized actions, improve visibility, preserve evidence, and strengthen detection, containment, accountability, and recovery.

## What problem does AegisLayer address?

Modern AI systems can call APIs, use tools, access data, trigger workflows, and influence consequential decisions. Traditional application security does not always address the full risk created by autonomous reasoning and execution.

AegisLayer focuses on the control boundary between AI reasoning and real-world action.

## What is the central architectural idea?

AI capability should remain separate from execution authority.

An AI system may be able to propose an action, but execution should require independent validation of identity, authority, policy, risk, approvals, runtime constraints, and evidence requirements.

## What kinds of threats are considered?

The public threat model includes:

- Prompt injection
- Unauthorized tool use
- Excessive agency
- Credential theft
- Privilege escalation
- Data poisoning
- Model and artifact tampering
- Supply-chain compromise
- Sensitive data exposure
- Evidence tampering
- Approval bypass
- Unsafe automation
- Insider threats

See `THREAT_MODEL.md` for details.

## What are the main architectural layers?

The public high-level architecture includes:

1. Identity and trust context
2. Intent and request analysis
3. Policy and risk evaluation
4. Approval and authority gates
5. Controlled execution runtime
6. Evidence and audit
7. Monitoring and incident response

See `ARCHITECTURE.md` for details.

## What does fail-closed mean?

Fail-closed means that when required identity, authority, policy, approval, or system state cannot be verified, the action should stop, deny, or escalate rather than proceed by assumption.

## Why is evidence important?

Evidence helps operators, reviewers, auditors, and investigators understand:

- Who initiated an action
- What was requested
- Which policy applied
- Who approved it
- What was executed
- What result occurred
- Whether records were altered

Evidence supports accountability, incident response, and continuous improvement.

## Is this repository production software?

No. This repository currently focuses on public architecture, research, governance, threat modeling, educational material, and approved reference content.

It does not claim that every described capability is implemented, independently certified, or production ready.

## Will proprietary source code be published here?

Only material approved for public release will be published.

The repository will not intentionally disclose confidential controls, customer information, credentials, private infrastructure, or unapproved patent-sensitive implementation details.

## Can developers contribute?

Yes. Public contributions may be considered if they are technically grounded, non-confidential, within scope, and suitable for public release.

See `../CONTRIBUTING.md`.

## How should a security vulnerability be reported?

Do not report vulnerabilities publicly.

Follow the private reporting process in `../SECURITY.md`.

## Is AegisLayer only for large enterprises?

No. The principles may be adapted to small teams, startups, enterprises, regulated organizations, research environments, and public-sector systems.

The implementation depth should match the risk, impact, and operating environment.

## Does AegisLayer replace existing cybersecurity tools?

No. It is intended to complement identity systems, cloud security, endpoint security, application security, monitoring, incident response, and compliance controls.

Its focus is the governance and security of AI-driven decisions and execution.

## Is AegisLayer a legal or compliance certification?

No. The public architecture is not legal advice, regulatory certification, or proof of compliance.

Organizations must evaluate their own laws, contractual obligations, regulatory duties, and risk profile.

## What is planned next?

Planned public work includes:

- Additional architecture specifications
- Reference diagrams
- Governance and threat-control mappings
- Public examples
- Demonstration tools
- Selected reusable components where appropriate
- Hugging Face and GitHub documentation alignment

See `../ROADMAP.md`.

## Who maintains the project?

AegisLayer is developed by VND TECH LLC.

Copyright © VND TECH LLC.
