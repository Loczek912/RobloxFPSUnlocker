import os
import json
import shutil
from tqdm import tqdm

def find_roblox_folder():
    exe_name = "RobloxPlayerBeta.exe"
    
    drives = ['C:', 'D:', 'E:', 'F:', 'G:', 'H:', 'I:', 'J:', 'K:', 'L:', 'M:', 'N:', 'O:', 'P:', 'Q:', 'R:', 'S:', 'T:', 'U:', 'V:', 'W:', 'X:', 'Y:', 'Z:']
    
    drives_iterator = tqdm(drives, desc="Searching for Roblox folder", leave=False)
    
    for drive in drives_iterator:
        folder_path = os.path.join(drive, '\\')
        for root, dirs, files in os.walk(folder_path):
            if exe_name in files:
                roblox_folder = os.path.abspath(root)
                drives_iterator.close()
                return roblox_folder

    drives_iterator.close()
    return None

def create_client_settings_folder(roblox_folder):
    client_settings_path = os.path.join(roblox_folder, 'ClientSettings')
    
    tqdm.write("Creating ClientSettings folder...")
    with tqdm(total=1, desc="Progress", leave=False) as pbar:
        if not os.path.exists(client_settings_path):
            os.mkdir(client_settings_path)
            pbar.update(1)

    return client_settings_path

def create_client_app_settings_json(client_settings_path):
    settings = {
        "DFIntTaskSchedulerTargetFps": 1000
    }
    
    json_file_path = os.path.join(client_settings_path, 'ClientAppSettings.json')
    
    tqdm.write("Creating ClientAppSettings.json file...")
    with open(json_file_path, 'w') as json_file:
        json.dump(settings, json_file, indent=4)

def main():
    try:
        import ctypes
        ctypes.wintypes
    except AttributeError:
        import ctypes.wintypes
    
    roblox_folder = find_roblox_folder()
    
    if roblox_folder:
        client_settings_path = create_client_settings_folder(roblox_folder)
        
        create_client_app_settings_json(client_settings_path)
        
        tqdm.write("ClientAppSettings.json created successfully in Roblox folder.")
        
        input("FPS Unlocked. Press any key to continue...")
    else:
        tqdm.write("Error finding Roblox directory. Make sure Roblox is installed.")

if __name__ == "__main__":
    main()
