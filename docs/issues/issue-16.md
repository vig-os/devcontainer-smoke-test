---
type: issue
state: open
created: 2026-03-08T20:08:04Z
updated: 2026-03-08T20:08:24Z
author: c-vigo
author_url: https://github.com/c-vigo
url: https://github.com/vig-os/devcontainer-smoke-test/issues/16
comments: 0
labels: bug, area:ci
assignees: c-vigo
milestone: none
projects: none
relationship: none
synced: 2026-03-09T04:17:29.169Z
---

# [Issue 16]: [[BUG] Agent-guardrail scripts and changelog have multiple defects from dev promotion](https://github.com/vig-os/devcontainer-smoke-test/issues/16)

## Description

Copilot review on PR #15 (dev → main) surfaced 6 comments across 3 related defect categories. All originate from code already merged to `dev` and are grouped here for a single fix pass.

### A. Wrong `project_root` in agent-blocklist scripts

`check-agent-identity.py`, `check-pr-agent-fingerprints.py`, and `prepare-commit-msg-strip-trailers.py` all use `Path(__file__).resolve().parent.parent`, which resolves to `.devcontainer/` — not the repo root. The blocklist path `.devcontainer/.github/agent-blocklist.toml` never exists, so every check silently no-ops.

Additionally, `check-agent-identity.py` and `check-pr-agent-fingerprints.py` import from `vig_utils.agent_blocklist`, which is not present in this repo or its lockfile.

**Files:**
- `.devcontainer/scripts/check-agent-identity.py`
- `.devcontainer/scripts/check-pr-agent-fingerprints.py`
- `.devcontainer/scripts/prepare-commit-msg-strip-trailers.py`

### B. Inverted `IN_CONTAINER` guard in prepare-commit-msg hook

`.githooks/prepare-commit-msg` checks `IN_CONTAINER = "false"`, but outside the devcontainer the variable is typically **unset** (not the literal string `"false"`). The guard never triggers. Should check `!= "true"` to fail closed.

**File:** `.githooks/prepare-commit-msg`

### C. Changelog claims vs actual action version pins

`CHANGELOG.md` states Dependabot bumped `actions/cache` to v5, `actions/checkout` to v6, and `actions/upload-artifact` to v7, but workflows still pin these to v4 SHAs. Either update the pins or reword the changelog entry.

**Files:** `CHANGELOG.md`, `.github/workflows/ci-container.yml`

## Steps to Reproduce

1. Run any of the three blocklist scripts from `.devcontainer/scripts/` — they silently exit 0 without checking anything.
2. Commit from the host (outside devcontainer) — the `prepare-commit-msg` hook does not block it.
3. Compare `CHANGELOG.md` entries against actual action SHAs in workflow files.

## Expected Behavior

- Blocklist scripts resolve the repo root correctly (`Path(__file__).resolve().parents[2]` or `git rev-parse --show-toplevel`) and function as intended.
- Missing `vig_utils` import is replaced with inlined logic or an added dependency.
- `IN_CONTAINER` check uses `!= "true"` to fail closed when the variable is unset.
- Changelog entries accurately reflect the shipped action versions.

## Actual Behavior

- All three blocklist scripts silently no-op (blocklist path never found).
- Host commits are not blocked by the prepare-commit-msg hook.
- Changelog overstates the Dependabot version bumps.

## Environment

- Devcontainer image: `ghcr.io/vig-os/devcontainer:latest`
- Source: Copilot review comments on PR #15

## Additional Context

Copilot review: https://github.com/vig-os/devcontainer-smoke-test/pull/15#pullrequestreview-3908317755

## Possible Solution

- **A:** Change `Path(__file__).resolve().parent.parent` → `.parents[2]` in all three scripts. Inline the blocklist parsing logic to remove the `vig_utils` dependency.
- **B:** Change `if [ "${IN_CONTAINER:-}" = "false" ]` → `if [ "${IN_CONTAINER:-}" != "true" ]`.
- **C:** Either update workflow action pins to match the claimed versions, or reword the changelog entry to reflect that the Dependabot branches were reconciled without changing effective action versions.

## Changelog Category

Fixed

## Acceptance Criteria

- [ ] All three blocklist scripts correctly resolve the repo root and execute their checks
- [ ] `vig_utils` dependency is removed (logic inlined or vendored)
- [ ] `IN_CONTAINER` guard blocks commits when the variable is unset
- [ ] Changelog entries match the actual shipped action versions
- [ ] TDD compliance (see .cursor/rules/tdd.mdc)
