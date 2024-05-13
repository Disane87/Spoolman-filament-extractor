import requests
import json
import os
from jsonschema import validate, ValidationError

# URL to fetch the JSON Schema
filaments_schema_url = "https://raw.githubusercontent.com/Donkie/SpoolmanDB/main/filaments.schema.json"

# API URL to fetch filaments data
api_url = "https://spoolman.disane.dev/api/v1/filament"

# Fetch the schema from the provided URL
response_schema = requests.get(filaments_schema_url)
schema = response_schema.json()

# Make the request to the API to fetch filaments data
response_data = requests.get(api_url)
data = response_data.json()

# Function to merge colors safely
def merge_colors(filament, new_color):
    if not any(color['name'] == new_color['name'] for color in filament["colors"]):
        filament["colors"].append(new_color)

# Process data and organize by manufacturer
manufacturers = {}
for item in data:
    manufacturer_name = item["vendor"]["name"]
    
    # Initialize manufacturer entry if not present
    if manufacturer_name not in manufacturers:
        manufacturers[manufacturer_name] = {
            "manufacturer": manufacturer_name,
            "filaments": []
        }
    
    # Search for existing material entry
    filament = next((f for f in manufacturers[manufacturer_name]["filaments"] if f["material"] == item["material"]), None)
    
    if filament:
        # If material entry exists, just add the new color
        merge_colors(filament, {"name": item["name"], "hex": item["color_hex"]})
    else:
        # If no material entry exists, create new
        new_filament = {
            "name": f"{manufacturer_name} {{color_name}}",
            "material": item["material"],
            "density": item.get("density", 1.0),
            "weights": [{
                "weight": item.get("weight", 0),
                "spool_weight": item.get("spool_weight", 0)
            }],
            "diameters": [item.get("diameter", 1.75)],
            "extruder_temp": item.get("settings_extruder_temp", 200),
            "bed_temp": item.get("settings_bed_temp", 60),
            "colors": [{"name": item["name"], "hex": item["color_hex"]}]
        }
        manufacturers[manufacturer_name]["filaments"].append(new_filament)

# Validate data against the schema and save to JSON files if valid
output_dir = 'output_filaments'
os.makedirs(output_dir, exist_ok=True)
for manufacturer, content in manufacturers.items():
    try:
        validate(instance=content, schema=schema)
        output_filename = os.path.join(output_dir, f"{manufacturer.replace(' ', '_')}.json")
        with open(output_filename, 'w') as file:
            json.dump(content, file, indent=4)
        print(f"Data for {manufacturer} validated successfully and saved.")
    except ValidationError as ve:
        print(f"Validation error for {manufacturer}: {ve.message}")

print(f"All data processed and valid data saved in directory: {output_dir}")
