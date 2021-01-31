from pykeen.triples import TriplesFactory
from pykeen.pipeline import pipeline
import torch
import os
from utils import (
    get_code_version,
    generate_md5_hash,
    log_experiment,
    logger
)

from config import (
    TRAINING_PATH, 
    VALIDATION_PATH, 
    TESTING_PATH,
    MODEL_SAVE_DIR

)


class KnowledgeGraphModel:
    """
    Class takes in the training data and trains a model.
    It allows allows for loading the saved model and predicting using the saved/trained model.
    """
    def __init__(
        self,
        training_path = TRAINING_PATH,
        validation_path = VALIDATION_PATH,
        testing_path = TESTING_PATH,
        version_data=True,
        version_code=True
    ):
        # initializing the constructor here. The data is read, hashed based on the flags and then loaded.
        self.__training = None
        self.__valid = None
        self.__testing = None
        self.__result = None
        self.__model = None
        self.__exp_tags = dict()
        if version_data:
            path_exists_condition = os.path.exists(training_path) and \
                                    os.path.exists(validation_path) and \
                                    os.path.exists(testing_path)
            if not path_exists_condition:
                raise FileNotFoundError(f"File Not Found when reading either one ore more of "
                                        f"{training_path}, {validation_path} or {testing_path}. "
                                        f"Please sure the files exists and right input has been provided.")
            self.__exp_tags['train_file_hash'] = generate_md5_hash(training_path)
            self.__exp_tags['test_file_hash'] = generate_md5_hash(testing_path)
            self.__exp_tags['validation_file_hash'] = generate_md5_hash(validation_path)
        if version_code:
            (current_repo, commit_hash, dirty_repo_indicator) = get_code_version(__file__)
            self.__exp_tags['current_repo'] = current_repo
            self.__exp_tags['code_hash'] = commit_hash
            self.__exp_tags['dirty_repo_indicator'] = dirty_repo_indicator
        self.__load_train_data(training_path, validation_path, testing_path)
        
    def __call__(
        self,
        read_old_model=True,
        model='TransE',
        num_epochs=2,
        train_batch_size=512,
        evaluation_batch_size=128,
        model_location=MODEL_SAVE_DIR
    ):
        # this fits the data from the old model - if model is present.
        if read_old_model:
            if os.path.exists(os.path.join(model_location, 'trained_model.pkl')):
                # use an old saved model
                self.__model = torch.load(os.path.join(model_location, 'trained_model.pkl'))
            else:
                # if no model found - just train the model
                raise FileNotFoundError(
                    f"Old model not found at {model_location}. "
                    f"Please check the path provided"
                )
        else:
            self.__fit(
                model_text=model,
                num_epochs=num_epochs,
                train_batch_size=train_batch_size,
                eval_batch_size=evaluation_batch_size,
                model_location=model_location
            )

        # if versioning has been set to true, the details are logged in mlflow

        if len(self.__exp_tags):
            log_experiment(
                params={
                    "num_epochs":num_epochs,
                    "train_batch_size":train_batch_size,
                    "eval_batch_size":evaluation_batch_size
                },
                tags=self.__exp_tags,
            )

    def __load_train_data(self, train_data_path, validation_path, test_data_path):
        """
        Reading training data in and loading in the generating required tensors

        """
        self.__training = TriplesFactory(
            path=train_data_path,
        )
        
        self.__valid = TriplesFactory(
            path=validation_path,
            entity_to_id=self.__training.entity_to_id,
            relation_to_id=self.__training.relation_to_id,
        )
        
        self.__testing = TriplesFactory(
            path=test_data_path,
            entity_to_id=self.__training.entity_to_id,
            relation_to_id=self.__training.relation_to_id,
        )

    def __fit(
        self,
        model_text,
        num_epochs, 
        train_batch_size, 
        eval_batch_size,
        model_location
    ):
        """
        Fit the model. This method can be expanded more for optimizing the model in a better manner.
        To make the code scalable - we can use json config for training_kwargs, model_kwargs, etc.
        """
        self.__result = pipeline(
            training=self.__training,
            validation=self.__valid,
            testing=self.__testing,
            model=model_text,
            training_kwargs=dict(num_epochs=num_epochs, batch_size=train_batch_size),
            evaluation_kwargs=dict(batch_size=eval_batch_size)
        )
        
        self.__result.save_to_directory(model_location)
        self.__model = self.__result.model

    def predict(self, tail, n=5, relation="GENE_DISEASE_ot_genetic_association", use_sigmoid=True):
        """
        This method takes tail and a relation and returns dataframe with possible heads and their associated scores.
        """
        predict_head_condition = (tail in self.__training.entity_to_id) or \
                                 (tail in self.__valid.entity_to_id) or \
                                 (tail in self.__testing.entity_to_id)
        if predict_head_condition:
            try:
                # if we choose to use sigmoid - the score is between 0 and 1.
                # The first value has the highest sigmoid score/ lowest loss.
                self.__model.predict_with_sigmoid = use_sigmoid
                results = self.__model.predict_heads(relation, tail)[:n]
                return results
            except KeyError:
                logger("Invalid tail element provided. Please provide a valid tail element")

    # the following code represents properties to provide access to data and
    # results, without modifying accidentally
    @property
    def train_data(self):
        return self.__training
    
    @property
    def valid_data(self):
        return self.__valid
    
    @property
    def test_data(self):
        return self.__testing
    
    @property
    def model(self):
        return self.__model
    
    @property
    def pipeline_results(self):
        return self.__result
