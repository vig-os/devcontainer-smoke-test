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

### Changed

### Removed

### Fixed

### Security
