from typing import List, Dict, Union
import llm

from functions import load_config, load_questions, write_json

import time

# load the configuration
config = load_config()


def prompt_llm(question:str, response_type:str, model_name:str) -> Union[str, Dict[str, str]]:  
    """
    Prompts the GPT-3 model with the question and returns the response.

    Args:
        question (str): The question to prompt the model with.
        response_type (str): The type of response to return. Can be 'txt' or 'json'.
        model_name (str): The name of the model to use e.g. 'gpt-3.5-turbo'.

    Returns:
        Union[str, Dict[str, str]]: The response from the model.
    """

    # load the model
    model = llm.get_model(model_name)
    if 'gpt' in model_name:
        model.key = config['OPENAI_API_KEY']
    response = model.prompt(question, system="Answer like a scientist, summarizing succintly for a student, with responses less than 200 words.")
    if response_type == 'json':
        return response.json()
    else:
        return response.text()


def run_question(question:str, response_type:str, model_name:str) -> Dict[str, Union[str, int, List[str]]]:
    """
    Runs a question through the pipeline.

    Args:
        question (str): The question to run through the pipeline.
        response_type (str): The type of response to return. Can be 'txt' or 'json'.
        model_name (str): The name of the model to use e.g. 'gpt-3.5-turbo'.

    Returns:
        Dict[str, Union[str, int, List[str]]]: The answer set.
    """

    # load the number of iterations to perform from the config
    
    iterations = config['ITERATIONS']

    # construct the answer set dictionary
    answer_set = {
        'question': question,
        'iterations': iterations,
        'model_name': model_name,
        'responses': []
    }

    print(f"[bold]Running question '{question}' through the pipeline using the {model_name} model.[/bold]")

    # perform a set of iterations
    for i in range(iterations):
        # prompt the model with the question
        response = prompt_llm(question['question'], response_type, model_name)
        # add the response to the answer set
        answer_set['responses'].append(response)
        # print the response to the terminal
        print (f"Iteration {i+1} of {iterations}:")
        print(response)
        print('\n')
        if 'gpt' in model_name:
            time.sleep(30)

    # return the answer set
    return answer_set


def main():
    response_type = 'txt'
    model_name = 'ggml-model-gpt4all-falcon-q4_0'
    
    # load the questions
    questions = load_questions(response_type=response_type)
    
    # prompt the model with each question
    for question in questions:
        answer_set = run_question(question, response_type, model_name)
        folder = f'{response_type}/{model_name}'
        write_json(answer_set, question['filename'], folder)
        

if __name__ == '__main__':
    main()