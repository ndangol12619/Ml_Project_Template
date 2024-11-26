
import os
from  pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')



project_name = "MLProjectTemplate"

folder_file_list = [
    ".github/workflow/.gitkeep",
    "README.md",
    ".env",
    "dvc.yaml",
    "params.yaml",
    "schema.yaml",
    "setup.py",
    "main.py",
    "app.py",
    "requirements.txt",
    "artifacts/__init__.py",
    "config/config.yaml",
    "research/trails.ipynb",
    "templates/index.html",

    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",

    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",

    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity__init__.py",
    
    f"src/{project_name}/exception/__init__.py",
    f"src/{project_name}/exception/exception.py",

    f"src/{project_name}/logger/__init__.py",
    f"src/{project_name}/logger/logger.py",

    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py"
 
]



for filepath in folder_file_list:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize((filepath == 0))):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating Empty File: {filepath}")
    else:
        logging.info(f"{filename} is already exits")
    
