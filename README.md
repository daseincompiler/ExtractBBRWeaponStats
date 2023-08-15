# ExtractBBRWeaponStats
An extraction workflow of Battlebit Remastered weapon's stats from Unity assets.  
# **Usage Guide**

To extract weapon stats from Battlebit Remastered using AssetRipper and the provided Python script, follow the steps below:

#### **Prerequisites**:

-   Make sure you have Python installed on your machine.
-   Download and extract the Asset Ripper tool. You can get it [here](https://github.com/AssetRipper/AssetRipper).

#### **Step-by-Step Guide**:

1.  **Setup Asset Ripper**:
    
    -   After downloading, extract the AssetRipper archive to your desired location.
2.  **Launch Asset Ripper & Analyze Assets**:
    
    -   Run the AssetRipper program.
    -   Point it to your Battlebit Remastered installation path, specifically at: `BattleBit Remastered\BattleBit_Data`.
3.  **Export MonoBehavior Assets**:
    
    -   Once AssetRipper has completed its analysis of all asset files, navigate to `resources.assets`.
    -   From the asset types listed, select "MonoBehavior".
    -   Click on "Export All Files of Selected Type".
4.  **Run the Provided Python Script**:
    
    -   After AssetRipper completes the export, navigate to this repository on your machine.
    -   Run the provided Python script called `extractBBRStats.py` or the compiled executable found in releases by the same name.
    -   When prompted, select the folder containing the exported "Monobehaviour" asset files. By default, this is located at: `export\BattleBit\ExportedProject\Assets\MonoBehaviour`, where `export` is the folder you selected for exporting in AssetRipper.
5.  **Check the Output**:
    
    -   Upon successful execution, the Python script will display the message "Extraction completed!".
    -   You should now see a new JSON file generated in the same directory as the script. This file, named `weapon_data.json`, contains all the extracted weapon stats.
## Educational Purposes Disclaimer
This repository is intended for educational purposes only. The content, code, and any associated materials are provided "as is" and without any express or implied warranties. 
