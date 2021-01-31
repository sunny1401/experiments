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


<u>Discussion on tracking model and data changes </u>

The pipeline class provides ResultTracker and uses mlflow for this purposes. 
However the functionality is very limited. 
Using the pipeline class only, we can track changes in parameters and metrics - 
which would give an idea about what changed in the model. \_\_fit method method can be used to extend the 
pipeline using training_kwargs, evaluator_kwargs and model_kwargs as .json files.

To use MLFlow properly, we need to MLFLOW_TRACKING_URI and 
MLFLOW_ARTIFACT_URI as environment variables. 

We also need to provide Extra_ARGS for S3 in environent_variables 

<u> TODO: update 1 </u>

The model can definitely be trained in a better manner. 
We can try for different loss functions - 
Adaptive Margin Ranking Loss can alleviate some of the issues of loss function. 
The loss function currently used in not very robust. 

Stratified train-test split can be tried as a starting point -  would be wise to use the hyperop pipeline 
and tune the parameters of the model. 

Code very slow. Adapt the code - maybe adapt pykeen




