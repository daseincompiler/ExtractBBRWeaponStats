import os
import json

# Path to the directory containing the asset files
directory_path = r"C:\Users\shant\Downloads\AssetRipper_win_x64\export\BattleBit\ExportedProject\Assets\MonoBehaviour"  # Modify this path to your directory

# Dictionary to store extracted data
weapons_data = {}

# Iterate over all files in the specified directory
for filename in os.listdir(directory_path):
    # Check if file contains an underscore and ends with '.asset'
    if "_" in filename and filename.endswith(".asset"):
        with open(os.path.join(directory_path, filename), 'r') as file:
            content = file.readlines()
        
        # Extract weapon or gadget name by removing the index and underscore
        weapon_name = filename.split("_", 1)[1].replace(".asset", "")
        
        vertical_mouse = None
        horizontal_mouse = None
        rounds_per_minute = None
        
        # Iterate through lines to find the required values
        for line in content:
            if "VerticalMouse:" in line:
                vertical_mouse = line.split(":")[1].strip()
            if "HorizontalMouse:" in line:
                horizontal_mouse = line.split(":")[1].strip()
            if "RoundsPerMinute:" in line:
                rounds_per_minute = line.split(":")[1].strip()
        
        # Add extracted data to the dictionary only if none of the values are None
        if all([vertical_mouse, horizontal_mouse, rounds_per_minute]):
            weapons_data[weapon_name] = {
                "VerticalMouse": vertical_mouse,
                "HorizontalMouse": horizontal_mouse,
                "RoundsPerMinute": rounds_per_minute
            }

# Get the directory of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Write the dictionary to a JSON file in the same directory as the script
output_filename = "weapons_data.json"
with open(os.path.join(script_directory, output_filename), 'w') as json_file:
    json.dump(weapons_data, json_file, indent=4)

print("Extraction complete!")
input("Press Enter to exit...")
