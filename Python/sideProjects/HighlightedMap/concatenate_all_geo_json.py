import json
import os

def concatenate_geojson(directory, output_file):
    # Initialize an empty list to store features from all files
    features = []

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.geo.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                data = json.load(file)
                # Assume each file is a GeoJSON FeatureCollection
                if data['type'] == 'FeatureCollection':
                    features.extend(data['features'])

    # Create a new GeoJSON FeatureCollection
    new_geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    # Write the new GeoJSON to a file
    with open(output_file, 'w') as file:
        json.dump(new_geojson, file, indent=4)

# Example usage
concatenate_geojson('geojson_data/', 'combined_output.geojson')
