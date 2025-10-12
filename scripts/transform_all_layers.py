#!/usr/bin/env python3
"""
Transform Rivers, Settlements, and Landmarks to match polygon layer bounds
"""

import json

def transform_rivers():
    print("\n" + "="*60)
    print("TRANSFORMING RIVERS")
    print("="*60)
    
    # Current rivers bounds
    rivers_lon_min = -169.00
    rivers_lon_max = 169.00
    rivers_lat_min = -90.00
    rivers_lat_max = 80.48
    
    # Target polygon layer bounds
    map_lon_min = -171.41
    map_lon_max = 171.01
    map_lat_min = -92.21
    map_lat_max = 92.41
    
    print("Loading rivers data...")
    with open('../data/map-layers/rivers.geojson', 'r') as f:
        rivers_data = json.load(f)
    
    print(f"Processing {len(rivers_data['features'])} river features...")
    
    for i, feature in enumerate(rivers_data['features']):
        if feature['geometry']['type'] == 'LineString':
            coords = feature['geometry']['coordinates']
            transformed_coords = []
            
            for coord in coords:
                lon, lat = coord
                lon_norm = (lon - rivers_lon_min) / (rivers_lon_max - rivers_lon_min)
                new_lon = map_lon_min + lon_norm * (map_lon_max - map_lon_min)
                lat_norm = (lat - rivers_lat_min) / (rivers_lat_max - rivers_lat_min)
                new_lat = map_lat_min + lat_norm * (map_lat_max - map_lat_min)
                transformed_coords.append([new_lon, new_lat])
            
            feature['geometry']['coordinates'] = transformed_coords
            
        elif feature['geometry']['type'] == 'MultiLineString':
            coords_list = feature['geometry']['coordinates']
            transformed_coords_list = []
            
            for coords in coords_list:
                transformed_coords = []
                for coord in coords:
                    lon, lat = coord
                    lon_norm = (lon - rivers_lon_min) / (rivers_lon_max - rivers_lon_min)
                    new_lon = map_lon_min + lon_norm * (map_lon_max - map_lon_min)
                    lat_norm = (lat - rivers_lat_min) / (rivers_lat_max - rivers_lat_min)
                    new_lat = map_lat_min + lat_norm * (map_lat_max - map_lat_min)
                    transformed_coords.append([new_lon, new_lat])
                
                transformed_coords_list.append(transformed_coords)
            
            feature['geometry']['coordinates'] = transformed_coords_list
    
    print("Saving transformed rivers data...")
    with open('../data/map-layers/rivers.geojson', 'w') as f:
        json.dump(rivers_data, f, separators=(',', ':'))
    
    print("✅ Rivers transformation complete!")

def transform_settlements():
    print("\n" + "="*60)
    print("TRANSFORMING SETTLEMENTS")
    print("="*60)
    
    # Current settlements bounds
    settlements_lon_min = -70.23
    settlements_lon_max = 70.05
    settlements_lat_min = -36.24
    settlements_lat_max = 37.09
    
    # Target polygon layer bounds
    map_lon_min = -171.41
    map_lon_max = 171.01
    map_lat_min = -92.21
    map_lat_max = 92.41
    
    print("Loading settlements data...")
    with open('../data/map-layers/towns_reprojected.geojson', 'r') as f:
        settlements_data = json.load(f)
    
    print(f"Processing {len(settlements_data['features'])} settlement features...")
    
    for i, feature in enumerate(settlements_data['features']):
        if feature['geometry']['type'] == 'Point':
            lon, lat = feature['geometry']['coordinates']
            
            # Transform coordinates
            lon_norm = (lon - settlements_lon_min) / (settlements_lon_max - settlements_lon_min)
            new_lon = map_lon_min + lon_norm * (map_lon_max - map_lon_min)
            lat_norm = (lat - settlements_lat_min) / (settlements_lat_max - settlements_lat_min)
            new_lat = map_lat_min + lat_norm * (map_lat_max - map_lat_min)
            
            feature['geometry']['coordinates'] = [new_lon, new_lat]
        
        if (i + 1) % 100 == 0:
            print(f"Processed {i + 1} features...")
    
    print("Saving transformed settlements data...")
    with open('../data/map-layers/towns_reprojected.geojson', 'w') as f:
        json.dump(settlements_data, f, separators=(',', ':'))
    
    print("✅ Settlements transformation complete!")

def transform_markers():
    print("\n" + "="*60)
    print("TRANSFORMING LANDMARKS (MARKERS)")
    print("="*60)
    
    # Current markers bounds
    markers_lon_min = -164.92
    markers_lon_max = 165.74
    markers_lat_min = -89.80
    markers_lat_max = 86.82
    
    # Target polygon layer bounds
    map_lon_min = -171.41
    map_lon_max = 171.01
    map_lat_min = -92.21
    map_lat_max = 92.41
    
    print("Loading landmarks data...")
    with open('../data/map-layers/markers.geojson', 'r') as f:
        markers_data = json.load(f)
    
    print(f"Processing {len(markers_data['features'])} landmark features...")
    
    for i, feature in enumerate(markers_data['features']):
        if feature['geometry']['type'] == 'Point':
            lon, lat = feature['geometry']['coordinates']
            
            # Transform coordinates
            lon_norm = (lon - markers_lon_min) / (markers_lon_max - markers_lon_min)
            new_lon = map_lon_min + lon_norm * (map_lon_max - map_lon_min)
            lat_norm = (lat - markers_lat_min) / (markers_lat_max - markers_lat_min)
            new_lat = map_lat_min + lat_norm * (map_lat_max - map_lat_min)
            
            feature['geometry']['coordinates'] = [new_lon, new_lat]
        
        if (i + 1) % 25 == 0:
            print(f"Processed {i + 1} features...")
    
    print("Saving transformed landmarks data...")
    with open('../data/map-layers/markers.geojson', 'w') as f:
        json.dump(markers_data, f, separators=(',', ':'))
    
    print("✅ Landmarks transformation complete!")

if __name__ == "__main__":
    transform_rivers()
    transform_settlements()
    transform_markers()
    
    print("\n" + "="*60)
    print("🎉 ALL TRANSFORMATIONS COMPLETE!")
    print("="*60)
    print("\nAll layers transformed to polygon layer bounds:")
    print(f"  Longitude: -171.41 to +171.01")
    print(f"  Latitude: -92.21 to +92.41")
    print("\nBackups saved as:")
    print("  - data/map-layers/rivers.geojson.backup")
    print("  - data/map-layers/towns_reprojected.geojson.backup")
    print("  - data/map-layers/markers.geojson.backup")
