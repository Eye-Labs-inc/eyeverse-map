#!/usr/bin/env python3
"""
Restore all transformed layers from backups
"""

import shutil

def restore_all():
    layers = [
        ('routes', 'Trade Routes'),
        ('rivers', 'Rivers'),
        ('towns_reprojected', 'Settlements'),
        ('markers', 'Landmarks')
    ]
    
    print("Restoring all layers from backups...\n")
    
    for filename, display_name in layers:
        try:
            source = f'../data/map-layers/{filename}.geojson.backup'
            dest = f'../data/map-layers/{filename}.geojson'
            shutil.copy(source, dest)
            print(f"✅ {display_name} restored")
        except FileNotFoundError:
            print(f"❌ {display_name} backup not found: {source}")
        except Exception as e:
            print(f"❌ Error restoring {display_name}: {e}")
    
    print("\n⚠️  Note: You'll need to manually revert coordinate range changes in index.html")
    print("Or use git to revert the file if it's tracked.")

if __name__ == "__main__":
    restore_all()
