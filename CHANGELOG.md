# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Added

### Changed

### Removed

### Fixed

- **Repository dispatch fails due to missing `pull-requests: write` permission** ([#22](https://github.com/vig-os/devcontainer-smoke-test/issues/22))
  - Added `pull-requests: write` to `repository-dispatch.yml` caller permissions so the called workflow's effective ceiling includes it
  - Added `pull-requests: write` to `ci.yml` top-level permissions to resolve the internal inconsistency with the `dependency-review` job

### Security
