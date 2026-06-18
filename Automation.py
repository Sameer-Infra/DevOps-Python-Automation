import os
import json
import logging
from pathlib import Path

logging.basicConfig(
    filename="server.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

class ServerManager():
    def __init__(self):
        self.config_string = '{"server_name": "prod_server", "status": "active"}'

    def load_config(self):
        data = json.loads(self.config_string)
        logging.info(f"Configuration loaded. Server Name: {data['server_name']}")

    def check_system(self):
        logging.info(f"System Check - Current Directory: {Path.cwd()}")
        logging.info(f"System Check - OS Name: {os.name}")

logging.info("--- Starting ServerManager Tool ---")
obj = ServerManager()
obj.load_config()
obj.check_system()
logging.info("--- ServerManager Tool Execution Completed ---")
