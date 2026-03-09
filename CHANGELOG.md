# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Added

- Deployed initial project scaffold
- Created [README.md](./README.md)
- **Bootstrap scripts and lock state aligned for CI validation** ([#1](https://github.com/vig-os/devcontainer-smoke-test/issues/1))
  - Updated repository bootstrap/setup behavior to match the current development and CI flow
  - Refreshed pre-commit and dependency lock state to keep validation runs consistent
- **repository_dispatch listener stub** ([#3](https://github.com/vig-os/devcontainer-smoke-test/issues/3))
  - Added a dedicated workflow that listens for `repository_dispatch` events
  - Logs dispatch payload metadata as a minimal foundation for later cross-repo integration
- **Wire smoke-test dispatch to run RC CI variants** ([#13](https://github.com/vig-os/devcontainer-smoke-test/issues/13))
  - Upgraded `repository-dispatch.yml` from stub to validate/orchestrate/summary flow
  - Parameterized `ci-container.yml` image tag via `workflow_call` input (default `latest`)
  - Added `workflow_call` trigger to `ci.yml` for reusable invocation

### Changed

- **Merged Dependabot GitHub Actions branches** ([#6](https://github.com/vig-os/devcontainer-smoke-test/issues/6))
  - Merged `actions/cache-5.0.3`, `actions/checkout-6.0.2`, and `actions/upload-artifact-7.0.0`
  - Included `actions-minor-patch-a1735c214c` to pick up additional workflow pin updates
- **Refreshed devcontainer image and scaffolding templates** ([#6](https://github.com/vig-os/devcontainer-smoke-test/issues/6))
  - Updated the devcontainer baseline and supporting scripts used to bootstrap and validate local/CI workflows
  - Added guard checks for skill naming, PR agent fingerprints, and commit message trailer normalization
- **Added ci-container validation workflow and troubleshooting notes** ([#6](https://github.com/vig-os/devcontainer-smoke-test/issues/6))
  - Introduced a dedicated `ci-container` GitHub Actions workflow to run container-focused validation
  - Documented observed CI container behavior and mitigations in `docs/container-ci-quirks.md`
- **Updated devcontainer template baseline to current upstream snapshot** ([#13](https://github.com/vig-os/devcontainer-smoke-test/issues/13))
  - Synced devcontainer helper scripts, hook wiring, and lock/tooling metadata with the latest template revision
  - Added the current `.devcontainer/justfile.devc` task set and aligned hook/template metadata with the upstream revision
  - Removed deprecated bootstrap helper scripts and refreshed Python tool dependency lock state

### Removed

### Fixed

- **Repository dispatch fails due to missing `pull-requests: write` permission** ([#22](https://github.com/vig-os/devcontainer-smoke-test/issues/22))
  - Added `pull-requests: write` to `repository-dispatch.yml` caller permissions so the called workflow's effective ceiling includes it
  - Added `pull-requests: write` to `ci.yml` top-level permissions to resolve the internal inconsistency with the `dependency-review` job

### Security
