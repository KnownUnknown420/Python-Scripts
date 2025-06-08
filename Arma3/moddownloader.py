import os
import re
import shutil

# Path to your Steam Workshop Arma 3 mods (usually 107410)
WORKSHOP_DIR = r"F:\SteamLibrary\steamapps\workshop\content\107410"
DESTINATION_DIR = r"D:\Arma3Server\SteamMods"  # Where to move renamed mods

# Make sure output folder exists
os.makedirs(DESTINATION_DIR, exist_ok=True)

def extract_mod_name(mod_folder):
    """Tries to read the name from meta.cpp or mod.cpp"""
    for file_name in ["meta.cpp", "mod.cpp"]:
        path = os.path.join(mod_folder, file_name)
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    match = re.search(r'name\s*=\s*"(.*?)"', line)
                    if match:
                        name = match.group(1).strip().replace(" ", "_")
                        name = re.sub(r'\W+', '', name)  # Remove non-alphanumeric (except underscore)
                        return f"@{name}"
    return None

for folder in os.listdir(WORKSHOP_DIR):
    full_path = os.path.join(WORKSHOP_DIR, folder)
    if os.path.isdir(full_path):
        new_name = extract_mod_name(full_path)
        if new_name:
            dest_path = os.path.join(DESTINATION_DIR, new_name)
            if not os.path.exists(dest_path):
                print(f"Renaming {folder} → {new_name}")
                shutil.copytree(full_path, dest_path)
            else:
                print(f"Skipped {folder}, {new_name} already exists")
        else:
            fallback_name = f"@mod_{folder}"
            dest_path = os.path.join(DESTINATION_DIR, fallback_name)
            if not os.path.exists(dest_path):
                print(f"⚠ No mod name found. Using fallback: {fallback_name}")
                shutil.copytree(full_path, dest_path)
            else:
                print(f"⚠ Skipped {folder}, fallback {fallback_name} already exists")
