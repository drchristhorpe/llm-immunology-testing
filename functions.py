from typing import List, Dict, Union

import toml
import json
import os

from pathlib import Path


def load_config() -> Union[Dict[str, str],None]:
    """
    Loads the config.toml file and returns it as a dictionary.

    Returns:
        Dict[str, str]: The config.toml file as a dictionary, or None if the folder doesn't exist.
    """
    return toml.load('config.toml')


def load_questions(response_type:str='txt') -> Union[List[Dict[str, str]], None]:
    """
    Loads all the questions from the questions folder.

    Args:
        response_type (str, optional): The type of response output to load. Defaults to 'txt', can also be 'json'.

    Returns:
        List[Dict[str, str]]: A list of all the questions in the questions folder, or None if the folder doesn't exist.
    """
    # TODO: write a test for this function
    # construct the folderpath
    folderpath = f'questions/{response_type}'
    
    # check if the folder exists
    if os.path.exists(folderpath):
        # load all the files in the folder
        files = os.listdir(folderpath)
        questions = []
        for file in files:
            questions.append(load_question(file, response_type))
        return questions
    else:
        return None


def load_question(filename:str, response_type:str='txt') -> Union[Dict[str, str], None]:
    """
    Loads a question from the questions folder.

    Args:
        filename (str): The filename of the question to load.
        response_type (str, optional): The type of response output to load. Defaults to 'txt', can also be 'json'.
    """
    # TODO: write a test for this function
    # construct the filepath
    filepath = f'questions/{response_type}/{filename}'
    print (filepath)
    # check if the file exists
    if os.path.exists(filepath):
        # load the file
        with open(filepath, 'r') as f:
            # return the file as a dictionary
            question = json.load(f)
            # add the filename to the dictionary
            question['filename'] = filename.replace('.json', '')    
            return question
    else:
        # return None if the file doesn't exist
        return None


def write_json(data:Dict[str, Union[str, int, List[str]]], filename:str, folder:str) -> None:
    """
    Writes a dictionary to a json file.

    Args:
        data (Dict[str, Union[str, int, List[str]]]): The dictionary to write to the file.
        filename (str): The filename to write the dictionary to.
        folder (str): The folder to write the file to.    
    """

    # create the folder if it doesn't exist
    path = Path(f'outputs/{folder}').mkdir(parents=True, exist_ok=True)
    
    # construct the filepath
    filepath = f'outputs/{folder}/{filename}.json'
    
    # write the dictionary to the file
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)