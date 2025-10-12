# Eyeverse World Map

A comprehensive web-based visualization system for the Eyeverse fantasy world, featuring interactive 2D/3D maps, elevation data, and geographic overlays including landmarks, settlements, and cultural regions.

## 🗂️ Project Structure

```
eyeverse-map/
├── index.html                 # 2D Map View (Main interactive map)
├── data-explorer.html         # Data Explorer (Statistics and analysis)
├── 3d-terrain-preview.html    # 3D terrain visualization
├── styles.css                 # Global styles and theme
├── map.webp                   # Base world map image
└── data/
    ├── elevation/             # Elevation data files
    │   ├── eyeverse-elevation-optimized.bin
    │   ├── eyeverse-elevation-optimized-metadata.json
    │   ├── eyeverse-elevation-new.bin
    │   ├── eyeverse-elevation-new-metadata.json
    │   └── 3d-map.obj
    └── map-layers/            # Geographic data layers
        ├── biomes.geojson
        ├── cultures.geojson
        ├── religions.geojson
        ├── rivers.geojson
        ├── routes.geojson
        ├── states.geojson
        ├── towns_reprojected.geojson
        └── markers.geojson
```

## 🚀 Getting Started

1. **Start the local server:**
   ```bash
   python3 -m http.server 8000
   ```

2. **Open in browser:**
   - Navigate to `http://localhost:8000`
   - The 2D Map View (main interactive map) will load first

## 📊 Features

### 2D Map View (`index.html`)
- Interactive 2D map with zoom and pan controls
- Multiple visualization modes:
  - **Map**: Base terrain view
  - **Regions**: Political state boundaries
  - **Cultures**: Cultural territories with color coding
  - **Beliefs**: Religious regions and territories
  - **Biomes**: Ecological zones and environments
  - **Settlements**: Cities, towns, and population centers
  - **Landmarks**: Points of interest including dungeons, battlefields, mines, and more
  - **Rivers**: Water systems and waterways
  - **Trade Routes**: Economic connections and trade paths
- Hover tooltips with detailed information
- Responsive controls and legend system

### Data Explorer (`data-explorer.html`)
- Interactive exploration of world statistics
- Elevation data analysis and visualization
- Settlement and population statistics
- Biome, culture, and religion breakdowns
- Real-time data visualization with cards and grids

### 3D Terrain Preview (`3d-terrain-preview.html`)
- Three.js-powered 3D terrain visualization
- Real elevation data mapped to 3D geometry
- Interactive camera controls (mouse drag to rotate)
- Optimized rendering with proper world aspect ratio
- View mode controls

## 📁 Data Organization

### Elevation Data (`data/elevation/`)
- **Optimized binary format** for fast loading
- **Metadata files** with elevation statistics
- **Multiple datasets** for comparison

### Map Layers (`data/map-layers/`)
- **GeoJSON format** for geographic features
- **Organized by feature type**: biomes, cultures, religions, states, settlements, landmarks, rivers, and trade routes
- **Markers data** includes dungeons, battlefields, mines, lighthouses, sacred sites, and other points of interest
- **Consistent coordinate system** across all layers

## 🛠️ Technical Details

- **Frontend:** Vanilla HTML/CSS/JavaScript
- **3D Rendering:** Three.js library
- **Data Format:** GeoJSON, Binary elevation data
- **Server:** Python HTTP server (development)

## 🌐 Navigation

- **2D Map View:** `index.html` (Main interactive map)
- **Data Explorer:** `data-explorer.html` (Statistics and analysis)
- **3D Terrain View:** `3d-terrain-preview.html` (3D visualization)
- **Clickable "Eyeverse World Map" title** returns to 2D Map View

All pages feature consistent navigation with active state indicators and the VT323 font for the title.
