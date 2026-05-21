# Autonomous LLM Self-Improvement Code Pipeline

An automated, self-evolving CI/CD pipeline built to satisfy DevOps and automation challenges. The project leverages an LLM agent to continually refactor repository source code and provisions an isolated, on-demand Hetzner Cloud VPS to run integration verifications via a secure Self-Hosted GitHub Runner.

## System Architecture & Workflow

1. **Code Evolution (Task 1):** A scheduled GitHub Actions CRON workflow triggers every 2 hours, running a Python script that pipes `target_code.py` content to the OpenAI API (`gpt-4o-mini`). The LLM optimizes the code under strict guardrails.
2. **Isolating Changes:** If code enhancements are detected, the agent cuts a isolated feature branch and files an automated Pull Request (PR) rather than pushing directly to `main`, preserving stability.
3. **Infrastructure Provisioning (Task 2):** Opening/updating a PR triggers a local bash script that interacts with the Hetzner Cloud API (`hcloud`), dynamically provisioning a secure, minimal `cx22` virtual machine instance.
4. **Stealth Mode Security:** The Hetzner instance is linked to a completely restricted Firewall containing zero Inbound rules (all public incoming traffic, including standard port 22 SSH, is permanently dropped). 
5. **Egress-based Tunneling:** Upon boot, `cloud-init` hooks register an ephemeral GitHub Actions runner. This runner establishes an outbound encrypted channel (HTTPS/WebSockets long-polling) back to GitHub.
6. **Self-Destruction & Cost Optimization:** The runner processes exactly one integration test suite via `pytest` and streams the outcome logs back to the GitHub UI. Immediately upon task completion, the instance triggers a callback API request to self-terminate, minimizing execution costs down to fractions of a cent ($0.004/hr).

## Repository Blueprint
* `.github/workflows/self_improve.yml` — Orchestrates the biennial automated LLM refactoring loop.
* `.github/workflows/run_tests.yml` — Provisions the secure Hetzner cloud framework on Pull Request events.
* `.github/workflows/test_job.yml` — Runs the test suites inside the provisioned self-hosted runner environment.
* `scripts/improve_code.py` — Python wrapper managing the LLM contextual logic and payload operations.
* `scripts/deploy_vps.sh` — Bash automation orchestrating `hcloud` operations and `cloud-init` payloads.
* `tests/test_target.py` — System test layer confirming environment host validation and algorithmic safety.
* `target_code.py` — The core source module subject to automated continuous refactoring.

## Setup Requirements

To run this pipeline efficiently, configure the following secrets within your GitHub Repository settings under `Settings -> Secrets and variables -> Actions`:

* `LLM_API_KEY`: A valid subscription token granting programmatic access to the LLM backend (e.g., OpenAI API).
* `HCLOUD_TOKEN`: A Hetzner Cloud API Access Token configured with full Read & Write privileges.
* `PAT_TOKEN`: A GitHub Personal Access Token (`classic`) possessing comprehensive `repo` scopes to manage automated branch pushes and automated pull requests.