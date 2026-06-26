# Changelog — feature/doctor-command

## Added

- Added `python nexus.py doctor`
- Added `python/engine/doctor.py`
- Updated `nexus.py` command parser

## Purpose

The doctor command checks whether the local Nexus Engine environment is healthy enough to run.

## Checks included

- Python version
- Required files
- Required folders
- `.env`
- `OPENAI_API_KEY`
- Required Python packages

## Test command

```powershell
python nexus.py doctor
```
