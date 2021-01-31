import os
import pathlib

TRAINING_PATH = "kg/train.hrt.txt"
VALIDATION_PATH = "kg/valid.hrt.txt"
TESTING_PATH = "kg/test.hrt.txt"

MODEL_SAVE_DIR = "saved-model"
MAIN_FOLDER_LOCATION = pathlib.Path(__file__).parent
os.makedirs(os.path.join(
	MAIN_FOLDER_LOCATION, MODEL_SAVE_DIR), 
exist_ok =True)

EXPERIMENT_NAME = "knowledge_graph_training"
EXPERIMENT_TRACKING_URI = "http://127.0.0.1:5000"

# useful if we need to use the resulttracker class
TRACKER = 'mlflow'