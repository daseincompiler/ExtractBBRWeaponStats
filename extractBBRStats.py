import os
import json
from tkinter import Tk, filedialog

weapon_count = 0

def extract_asset_data(directory_path):
    global weapon_count

    weapons_data = {}
    
    for filename in os.listdir(directory_path):
        if "_" in filename and filename.endswith(".asset"):
            with open(os.path.join(directory_path, filename), 'r') as file:
                content = file.readlines()
            
            weapon_name = filename.split("_", 1)[1].replace(".asset", "")
            data_keys = [
                "DamageOnInfantryBody", "DamageOnLightArmoredVehicles", "DamageOnHeavyHeavyVehicles",
                "BulletVelocity", "ProjectileVisualSize", "BaseHipFireAccuracy", "VerticalMouse",
                "HorizontalMouse", "FirstShotRecoil", "AdsTime", "PlayerRunningSpeed",
                "ReloadSpeed", "DrawSpeed", "RoundsPerMinute", "ShotSoundDistance"
            ]
            
            weapon_data = {}
            for key in data_keys:
                for line in content:
                    if key + ": " in line:
                        weapon_data[key] = line.split(": ")[1].strip()
                        break

            # Check if any key is missing from the extracted weapon data
            if all(key in weapon_data for key in data_keys):
                weapons_data[weapon_name] = weapon_data
                print(weapon_name)
                weapon_count += 1
                
    return weapons_data


def main():
    Tk().withdraw()  # Hide the root tkinter window
    directory_path = filedialog.askdirectory(title="Select the MonoBehaviour Asset Folder")
    
    if not directory_path:
        print("No directory selected. Exiting.")
        return

    weapons_data = extract_asset_data(directory_path)
    
    script_directory = os.path.dirname(os.path.abspath(__file__))
    output_filename = "weapons_data.json"
    
    with open(os.path.join(script_directory, output_filename), 'w') as json_file:
        json.dump(weapons_data, json_file, indent=4)

    print(f"{weapon_count} weapons had their data extracted!")

    print(f"Extraction complete!")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()