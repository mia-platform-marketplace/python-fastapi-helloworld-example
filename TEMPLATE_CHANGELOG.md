# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## 04/08/2023

### Changed

- [MCRDPFERT-2](https://makeitapp.atlassian.net/browse/MCRDPFERT-2): Now it's possibile to set with the environment variable HEADER_KEYS_TO_PROXY which headers the my_platform_client utility should proxy

### Fixed

- [MCRDPFERT-1](https://makeitapp.atlassian.net/browse/MCRDPFERT-1): Now it's possibile to customize the mock server's base url
- [MCRDPFERT-5](https://makeitapp.atlassian.net/browse/MCRDPFERT-5): The "by_id" methods implemented by the my_platform_client utility no longer has the final slash (before: `/resource/1/`, after: `/resource/1`)
- [MCRDPFERT-6](https://makeitapp.atlassian.net/browse/MCRDPFERT-6): The my_platform_client utility sends headers correctly
- [MCRDPFERT-3](https://makeitapp.atlassian.net/browse/MCRDPFERT-3): Logs are now shown in the monitoring console section