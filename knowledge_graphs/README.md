Knowledge Graph Games

<u>To run the code please use the Data Analysis notebook</u>

 
<u>The code structure is as follows:</u>
	
1. requirements.txt - lists out the package requirements for running the code
- because the code uses mlflow - 
befor initiating the experiment and if using the code for 
the first time - type the following in the terminal:
```bash
mlflow ui
```
This will initialize a database on your local disk or whichever tracking uri with make required tables for experiments, params, tags and database version etc. This is required by MLFLOW.


2. config.py - sets config, ie., the location of different data files, the experiment name to use, the location for saving the data

3. utils.py - code for helper functions for logging, versioning etc.

4. model_training.py - main training code. This file contains class called KnowledgeGraph. 
This class has function for reading in data in the required format and training the model. 
It also has function to predict the top n (default value=5) closest prediction of heads for given relation and tail
	to run - 
		
		kg = KnowledgeGraph() - this would initialize with the default agrguments; 
		and raise  FileNotFoundError, if training, validation and test files 
		are not found in their default locations.
	
	after reading in the data - 
		
		kg(read_old_data=True) - would look for model in model_location folder. 
		If not found in the default location, it would raise an error.

		kg() - would train a new model and save the trained model in model-location

	after training - we can predict using kg.predict()

The class also provides properties for getting 
information about training-pipeline, model, train_data, valid_data and test_data.

By default, the names provided in model_scraps.py are taken as default location for data and model files.

The current \_\_fit method in class KnowledgeGraph is very limited. 





