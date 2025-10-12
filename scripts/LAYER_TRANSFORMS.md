# Layer Transformation Documentation

This document explains the coordinate transformations applied to map layers.

## Background

The map layers (Settlements, Landmarks, Rivers, Trade Routes) were originally in different coordinate systems than the polygon layers (Regions, Cultures, Beliefs, Biomes). To ensure all layers align correctly with the base map image, coordinate transformations were applied.

## Coordinate System

All layers now use a unified coordinate system:
- **Longitude**: -171.41 to +171.01 (span: 342.42)
- **Latitude**: -92.21 to +92.41 (span: 184.62)

## Transformation Applied

The following layers were transformed to match the polygon layer coordinate system:

1. **Trade Routes** (routes.geojson)
   - Original: Longitude -168.84 to +168.50, Latitude -87.20 to +90.00
   - Transformed: 632 route features

2. **Rivers** (rivers.geojson)
   - Original: Longitude -169.00 to +169.00, Latitude -90.00 to +80.48
   - Transformed: 58 river features

3. **Settlements** (towns_reprojected.geojson)
   - Original: Longitude -70.23 to +70.05, Latitude -36.24 to +37.09
   - Transformed: 798 settlement features

4. **Landmarks** (markers.geojson)
   - Original: Longitude -164.92 to +165.74, Latitude -89.80 to +86.82
   - Transformed: 87 landmark features

## Rendering Transformation

The map display fills 100% of the canvas. To align the transformed layers with the full canvas, an inverse transformation is applied during rendering:

```javascript
x = (((coord_lon + 171.41) / 342.42) * canvas.width - 15) / 0.97;
y = (((92.41 - coord_lat) / 184.62) * canvas.height - 15) / 0.91;
```

This compensates for the original 0.97 width squeeze, 0.91 height squeeze, and 15px offsets that were designed into the coordinate system.

## Backup Files

Original layer data is preserved in backup files:
- `data/map-layers/routes.geojson.backup`
- `data/map-layers/rivers.geojson.backup`
- `data/map-layers/towns_reprojected.geojson.backup`
- `data/map-layers/markers.geojson.backup`

## Scripts

Located in the `scripts/` directory.

### `transform_all_layers.py`
Transforms all data layers (Rivers, Settlements, Landmarks, Trade Routes) to the unified coordinate system.

**Usage:**
```bash
cd scripts
python3 transform_all_layers.py
```

### `restore_all_layers.py`
Restores all layers from their backup files.

**Usage:**
```bash
cd scripts
python3 restore_all_layers.py
```

**Note:** After restoring, you'll need to manually revert the coordinate range changes in `index.html` or use git to restore the file.

## Date Applied
October 12, 2025
