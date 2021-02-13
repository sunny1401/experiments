import git
import hashlib
from mlflow.exceptions import MlflowException
import functools
from structlog import get_logger
import mlflow
from config import (
    EXPERIMENT_NAME
)
import os
logger = get_logger()


def generate_md5_hash(filename):
    """
    Generates md5 hash for the code file

    @params: filename (str): Full file path

    return (str): MD5 Hash
    """
    # function copied from a code written by john_greenall@aig
    buf_size = 65536
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(buf_size)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()


def get_code_version(filepath):
    """
    Function takes in the file[ath and returns the git repo name,
    the current git hash and if the repo is dirty or not if a git repo is initiated.
    Else, it return just returns the md5 hash of the file
    @params: (str): complete file path
    return (tuple): (name of git repo, commit hash, if the repo is dirty)
    """
    try:
        current_repo = git.Repo(filepath, search_parent_directories=True)
        dirty_repo_indicator = current_repo.is_dirty()
        commit_hash = current_repo.head.object.hexhsa
        working_dir = current_repo.working_dir
        return working_dir, commit_hash, dirty_repo_indicator

    except git.InvalidGitRepositoryError:
        logger.info(
            f"{filepath} doe not belong to any repository. "
            "Please initiate a repository for proper use. "
            f"Currently returning md5 hash for {filepath}"
        )
        return "notavalidgitrepo", generate_md5_hash(filepath), "notavalidgitrepo"


def log_experiment(
        params,
        metrics=None,
        tags=None,
        model=None,
        experiment_name=EXPERIMENT_NAME
):
    """
    Logs the model and related parameters and metrics as an experiment.
    :param params: (dict): key-value pairs of named-paramters used by the model
    :param tags: (dict): key-value pairs of tags
    :param metrics: (dict): key-value paris of metric by the model
    :param model: (str): file location of saved model
    :param experiment_name: (str): Name of experiment for which data is being logged
    :param tracking_uri: (str): Tracking uri which should be mapped to the experiment.
    For permanent uris such as postgres database etc, these can be set to environment variable - MLFLOW_TRACKING_URI
    """
    try:
        mlflow.create_experiment(experiment_name)
    except MlflowException:
        logger.info("Found existing experiment. Adding new version to that.")

    mlflow.set_experiment(experiment_name)
    with mlflow.start_run():
        mlflow.log_params(params)
        if metrics is not None:
            mlflow.log_metrics(metrics)
        mlflow.set_tags(tags)
        if model is not None:
            mlflow.log_artifact(model)
    try:
        mlflow.end_run()
    except MlflowException:
        pass
