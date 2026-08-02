# Security Policy

## Purpose

AegisLayer is a security-focused research and architecture project. Responsible handling of security concerns is essential to protecting users, contributors, infrastructure, and the integrity of the project.

## Reporting a Vulnerability

Do not disclose suspected vulnerabilities in public issues, discussions, pull requests, social media, or community forums.

Report security concerns privately to:

**security@aegislayer.ai**

Include, where possible:

- A clear description of the issue
- The affected component or document
- Steps to reproduce or validate the concern
- Potential impact
- Any proof-of-concept material that can be shared safely
- Suggested mitigations, if known

Do not include credentials, personal data, customer data, or unrelated confidential information.

## Response Process

Reports will be reviewed and triaged according to severity, reproducibility, scope, and potential impact.

The project may:

1. Request additional information.
2. Confirm whether the issue is within scope.
3. Develop and validate a mitigation.
4. Coordinate disclosure timing with the reporter.
5. Publish an advisory when appropriate.

No specific resolution timeline is guaranteed. Complex issues may require additional investigation, coordination, or testing.

## Scope

This policy currently covers public content in this repository, including:

- Architecture documentation
- Threat-model documentation
- Governance materials
- Reference designs
- Public examples
- Future open-source components published here

Third-party platforms, dependencies, websites, and infrastructure are governed by their respective security policies unless explicitly stated otherwise.

## Safe-Harbor Intent

Good-faith security research should:

- Avoid privacy violations and data destruction
- Avoid service disruption
- Use the minimum access necessary
- Stop testing when sensitive information is encountered
- Report findings promptly and privately
- Allow reasonable time for investigation before disclosure

This statement expresses project intent and is not legal advice or a waiver of applicable law.

## Out of Scope

The following are generally out of scope unless they demonstrate a concrete security impact:

- Social engineering
- Physical attacks
- Denial-of-service testing
- Automated scanning that degrades service
- Reports based only on version banners
- Missing headers without demonstrated impact
- Hypothetical issues without a reproducible path
- Vulnerabilities in third-party services not controlled by this project

## Secrets and Sensitive Information

Never submit:

- API keys
- Passwords
- Access tokens
- Private keys
- Customer information
- Internal credentials
- Proprietary or patent-sensitive implementation details

If sensitive information is accidentally committed, revoke or rotate the affected credential immediately. Removing it from Git history alone does not make it safe.

## Current Project Status

This repository primarily contains public research and architecture documentation. It does not claim that every described control is implemented, independently validated, or sufficient to prevent all cyberattacks.

Copyright © VND TECH LLC.
