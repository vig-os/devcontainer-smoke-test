---
type: pull_request
state: open
branch: bugfix/1-make-ci-cd-pass → dev
created: 2026-02-24T15:57:14Z
updated: 2026-02-24T16:11:13Z
author: c-vigo
author_url: https://github.com/c-vigo
url: https://github.com/vig-os/devcontainer-smoke-test/pull/2
comments: 0
labels: none
assignees: c-vigo
milestone: none
projects: none
relationship: none
synced: 2026-02-25T04:21:02.934Z
---

# [PR 2](https://github.com/vig-os/devcontainer-smoke-test/pull/2) chore: align setup scripts and lockfile for CI validation

## Description

This PR prepares the smoke-test repository for reliable CI workflow validation by aligning project setup scripts, dependency lock state, and supporting docs/changelog updates.

## Type of Change

- [ ] `feat` -- New feature
- [ ] `fix` -- Bug fix
- [ ] `docs` -- Documentation only
- [x] `chore` -- Maintenance task (deps, config, etc.)
- [ ] `refactor` -- Code restructuring (no behavior change)
- [ ] `test` -- Adding or updating tests
- [ ] `ci` -- CI/CD pipeline changes
- [ ] `build` -- Build system or dependency changes
- [ ] `revert` -- Reverts a previous commit
- [ ] `style` -- Code style (formatting, whitespace)

### Modifiers

- [ ] Breaking change (`!`) -- This change breaks backward compatibility

## Changes Made

- Updated `.devcontainer/scripts/setup-gh-repo.sh`
  - Adjusted repository setup behavior used during environment/bootstrap flow.
- Updated `.pre-commit-config.yaml`
  - Simplified or removed config entries no longer needed by the current workflow.
- Updated `uv.lock`
  - Refreshed locked dependency state to match current project configuration.
- Updated `README.md`
  - Documented project purpose/scope and current setup expectations.
- Updated `CHANGELOG.md`
  - Added Unreleased entries covering scaffold/docs/devcontainer image updates.

## Changelog Entry

### Added

- Deployed initial project scaffold
- Created [README.md](./README.md)
- Updated devcontainer image to development version [5753eb2](https://github.com/vig-os/devcontainer/commit/5753eb2aafda99268a199ea22de344345cacacff) ([#1](https://github.com/vig-os/devcontainer-smoke-test/issues/1))

## Testing

- [ ] Tests pass locally (`just test`)
- [ ] Manual testing performed (describe below)

### Manual Testing Details

N/A

## Checklist

- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review of my code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have updated the documentation accordingly (edit `docs/templates/`, then run `just docs`)
- [x] I have updated `CHANGELOG.md` in the `[Unreleased]` section (and pasted the entry above)
- [ ] My changes generate no new warnings or errors
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published

## Additional Notes

Purpose of this PR is to validate CI workflow behavior from a realistic maintenance branch touching setup, lockfile, and docs/changelog updates.

Refs: #1

