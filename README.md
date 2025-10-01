# Eyeverse World - 3D Terrain Visualization

A web-based 3D terrain visualization system for the Eyeverse fantasy world, featuring interactive maps, elevation data, and geographic overlays.

## 🗂️ Project Structure

```
eyeverse-world/
├── index.html                 # Home page (Data Explorer)
├── 2d-map-view.html           # 2D terrain visualization with overlays
├── 3d-terrain-preview.html    # 3D terrain visualization
├── styles.css                 # Global styles and theme
├── map.webp                   # Base world map image
├── package.json               # Project metadata
└── data/
    ├── elevation/             # Elevation data files
    │   ├── eyeverse-elevation-optimized.bin
    │   ├── eyeverse-elevation-optimized-metadata.json
    │   ├── eyeverse-elevation-new.bin
    │   └── eyeverse-elevation-new-metadata.json
    └── map-layers/            # Geographic data layers
        ├── biomes.geojson
        ├── cultures.geojson
        ├── religions.geojson
        ├── rivers.geojson
        ├── states.geojson
        ├── towns_reprojected.geojson
        └── [additional route and marker files]
```

## 🚀 Getting Started

1. **Start the local server:**
   ```bash
   python3 -m http.server 8000
   ```

2. **Open in browser:**
   - Navigate to `http://localhost:8000`
   - The Data Explorer (index page) will load first

## 📊 Features

### Data Explorer (`index.html`)
- Interactive exploration of world statistics
- Elevation data analysis
- Biome and state information
- Real-time data visualization

### 2D Terrain Visualizer (`2d-map-view.html`)
- Base terrain rendering with elevation mapping
- Interactive overlay layers:
  - Cultures (color-coded regions)
  - Religions (belief system territories)
  - States (political boundaries)
  - Biomes (ecological zones)
  - Rivers (water systems)
  - Trade Routes (economic connections)
- Hover information and dynamic scaling
- Coordinate display and interactive controls

### 3D Terrain Preview (`3d-terrain-preview.html`)
- Three.js-powered 3D terrain visualization
- Real elevation data mapped to 3D geometry
- Interactive camera controls (mouse drag to rotate)
- Optimized rendering with proper world aspect ratio
- View mode controls

## 🎨 Design System

- **Glass-morphism UI** with consistent styling
- **VT323 font** for the "Eyeverse World" title
- **Responsive design** with modern CSS variables
- **Consistent navigation** across all pages

## 📁 Data Organization

### Elevation Data (`data/elevation/`)
- **Optimized binary format** for fast loading
- **Metadata files** with elevation statistics
- **Multiple datasets** for comparison

### Map Layers (`data/map-layers/`)
- **GeoJSON format** for geographic features
- **Consolidated structure** - no more duplicate folders
- **Organized by feature type** (biomes, cultures, etc.)

## 🛠️ Technical Details

- **Frontend:** Vanilla HTML/CSS/JavaScript
- **3D Rendering:** Three.js library
- **Data Format:** GeoJSON, Binary elevation data
- **Server:** Python HTTP server (development)

## 🌐 Navigation

- **Home/Data Explorer:** `index.html`
- **2D Terrain View:** `terrain-visualizer.html`
- **3D Terrain View:** `3d-terrain-preview.html`
- **Clickable logo** returns to home page

All pages feature consistent navigation and styling.
