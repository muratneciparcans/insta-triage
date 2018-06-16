import json
import os

def load_script():
    file_directory = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(file_directory, 'resources/triage_script.json')
    
    with open(script_path) as f:
        script = json.load(f)
        return script