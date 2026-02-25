# devcontainer Smoke Test

This repository is a smoke-test workspace for the
[vig-os/devcontainer](https://github.com/vig-os/devcontainer) project.

Its purpose is to verify that the devcontainer template and the shipped CI
workflow run successfully on real GitHub-hosted runners, not only in local or
synthetic test environments.

## Why this repo exists

The main `vig-os/devcontainer` repository publishes template files under
`assets/workspace/`, including a CI workflow
(`assets/workspace/.github/workflows/ci.yml`).

This repository provides a real target where that template can be bootstrapped
and executed end-to-end so regressions are caught early, for example:

- broken GitHub Action pins
- runner environment changes
- dependency/tooling incompatibilities (for example `uv` changes)

## Scope

This repository is intentionally minimal. It is used to:

1. bootstrap a fresh workspace from the current devcontainer template
2. run the shipped CI workflow on pull requests
3. validate that expected jobs pass in GitHub Actions
4. host CI wiring experiments such as `repository_dispatch` listeners

## Relationship to `vig-os/devcontainer`

- **Source of truth for template**: `vig-os/devcontainer`
- **Execution/verification target**: this repository

Template or workflow changes should be made in
[`vig-os/devcontainer`](https://github.com/vig-os/devcontainer), then validated
here through a normal PR run.
