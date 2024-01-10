import os
from pathlib import Path

package_name= "DiamondPricePrediction"

list_of_files=[
    "github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/componnets/__init__.py",
    f"src/{package_name}/componnets/data_ingestion.py",
    f"src/{package_name}/componnets/data_transformation.py",
    f"src/{package_name}/componnets/model_trainer.py",
    f"src/{package_name}/pipelines/__init__.py"
    f"src/{package_name}/pipelines/training_piprline.py",
    f"src/{package_name}/pipelines/prediction_pipeline.py",
    f"src/{package_name}/logger.py",
    f"src/{package_name}/exceptions.py",
    f"src/{package_name}/utils/__init__.py",
    f"notebooks/research.ipynb",
    f"notebooks/data/.gitkeep",
    f"requirements.txt",
    f"setup.py",
    f"init_setup.sh"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
    else:
        print("file already exists")