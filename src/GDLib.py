import json
import os
from enum import Enum
import requests
from threading import Thread

GDT_SETTINGS_FILENAME = "GDT_SETTINGS.json"

# PLEASE NOTE: these constants should be updated according to new releases
class GODOT_INSTALL(str, Enum):
    CURRENT = "https://github.com/godotengine/godot/releases/download/4.3-stable/Godot_v4.3-stable_win64.exe.zip"

# install godot to path specified
def installGodot(path: str, url: str):
    # create file for writing later
    if not os.path.exists(path):
        open(path, "w").write("")
    
    # install godot
    content = requests.get(url).content
    open(path, "wb").write(content)
    

def save_GDT_settings(fileRoot: str, GDT_settings: dict):
    with open(os.path.join(fileRoot, GDT_SETTINGS_FILENAME), "w") as f:
        f.write(json.dumps(GDT_settings, indent=4))

class gdtInit:
    DEFAULT_GDT_SETTINGS = {
        "paths": {
            "godot": ""
        }
    }
    GODOT_INIT_ERROR = '"GDT init" must be called on an empty project folder.'
    
    def initGodotEnvironment(self, fileRoot: str):
        
        print("Initializing environment...")
        
        godot_install_path: str = os.path.join(fileRoot, "engine", "godot.exe")
        
        # Create the engine directory if it doesn't exist
        engine_dir = os.path.dirname(godot_install_path)
        if not os.path.exists(engine_dir):
            os.makedirs(engine_dir)
            
        # settings file stuff
        GDT_settings = self.DEFAULT_GDT_SETTINGS
        GDT_settings_path: str = os.path.join(fileRoot, GDT_SETTINGS_FILENAME)
        
        # write default configurations
        if not os.path.exists(GDT_settings_path):
            open(GDT_settings_path, "w").write(json.dumps(
                self.DEFAULT_GDT_SETTINGS,
                indent=4
                ))
        else:
            raise FileExistsError(self.GODOT_INIT_ERROR)
        
        print("Downloading godot...")
        
        installGodot(
            godot_install_path,
            GODOT_INSTALL.CURRENT.value
            )
        
        GDT_settings["paths"]["godot"] = godot_install_path
        save_GDT_settings(fileRoot, GDT_settings)
        
        print("Finished Project Initialization.")