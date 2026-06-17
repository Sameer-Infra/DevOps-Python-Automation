import os
import json
from pathlib import Path

class ServerManager():
    def __init__(self):
        self.config_string = '{"server_name": "prod_server", "status": "active"}'

    def load_config(self):
            
        data = json.loads(self.config_string)
        
        print(f"Server Name from JSON: {data['server_name']}")


    def check_system(self):
        print(f"Current Directory: {Path.cwd()}")

        print(f"OS Name: {os.name}")


obj = ServerManager()

obj.load_config()
obj.check_system()
