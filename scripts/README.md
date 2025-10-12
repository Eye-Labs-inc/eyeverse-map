# Scripts Directory

This directory contains utility scripts for transforming and managing map layer data.

## Files

- **`transform_all_layers.py`** - Transform Rivers, Settlements, Landmarks, and Trade Routes to unified coordinate system
- **`restore_all_layers.py`** - Restore all layers from backup files
- **`LAYER_TRANSFORMS.md`** - Detailed documentation about layer transformations

## Usage

All scripts should be run from within the `scripts/` directory:

```bash
cd scripts
python3 transform_all_layers.py
```

or

```bash
cd scripts
python3 restore_all_layers.py
```

## Important Notes

- Backups are automatically created before transformations
- Backup files are stored in `data/map-layers/*.geojson.backup`
- See `LAYER_TRANSFORMS.md` for detailed documentation
