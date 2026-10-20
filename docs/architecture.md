# Architecture

This project follows a layered structure:

- `src/domain`: project data model and validation rules
- `src/io`: reading/writing Excel files
- `src/integration`: Revit export and ETABS COM client
- `src/pipeline`: model generation, checks and orchestration
- `src/app`: entry point

The aim is to keep:
- input validation separate
- ETABS integration isolated
- result extraction separate
- checking rules isolated
- reporting separate

This makes the project easier to adapt to a different project or ETABS version.