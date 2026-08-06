\# Changelog



All notable changes to OGS Smart Money AI will be documented in this file.



\---



\## \[0.0.1] - 2026-07-10



\### Added



\- Initial project structure

\- requirements.txt

\- .gitignore

\- README

\- LICENSE

\- CHANGELOG



\### Status



Foundation Started

## [0.1.0-alpha.2]

### Added

- Central logging framework
- Automatic log file creation
- Rotating log files
- Custom OGS exception hierarchy

### Improved

- Configuration now uses constants as the single source of truth.
## [0.1.0-alpha.3]

### Added

- Environment Manager
- Startup Manager
- Python version validation
- Package validation
- Directory validation
- Write permission validation
- Virtual environment detection

## [0.1.0-alpha.4]

### Added

- Application lifecycle model
- Service container
- Shutdown manager
## [0.1.0-alpha]

### Completed

- Application Kernel
- Startup Manager
- Shutdown Manager
- Environment Manager
- Service Container
- Kernel Lifecycle
## [0.2.0-alpha]

### Added

- Market domain package
- AssetClass enum
- Symbol enum
- Symbol classification properties

## [0.2.0-alpha]

### Added

- Timeframe domain model
- Timeframe hierarchy
- Timeframe helper properties

## [0.2.0-alpha]

### Added

- TradingSession domain model
- UTC session boundaries
- Session metadata
- ### Added

- Duplicate domain object
- DuplicateDetector
- Duplicate candle detection by timestamp
### Added

- TimezoneNormalizer
- UTC normalization for CandleSeries
- Immutable timezone conversion
### Added

- Swing domain object
- Swing price abstraction
- Swing timestamp helper

### Added

- SwingDetector
- Bill Williams 5-candle fractal algorithm
- Swing High detection
- Swing Low detection


### Added

- SwingValidator
- Validation for Swing domain objects