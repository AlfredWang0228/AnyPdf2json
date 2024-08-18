# src/utils/helpers.py

import logging
from functools import wraps
import time
from typing import Callable
import os
import json

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def logging_decorator(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        # Extract prompts
        if len(args) > 1:  # Instance method call
            system_prompt = args[1]
            user_prompt = args[2]
        else:  # Direct function call
            system_prompt = kwargs.get('system_prompt', '')
            user_prompt = kwargs.get('user_prompt', '')
        
        input_word_count = len(system_prompt.split()) + len(user_prompt.split())
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        execution_time = end_time - start_time
        output_word_count = len(result.split())
        
        logging.info(f"Execution Time: {execution_time:.2f} seconds")
        logging.info(f"Input Word Count: {input_word_count}")
        logging.info(f"Output Word Count: {output_word_count}")
        return result
    
    return wrapper

def setup_logger(name: str, log_file: str, level: int = logging.INFO) -> logging.Logger:
    """Function to setup as many loggers as you want"""
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Ensure the directory for the log file exists
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


def extract_and_validate_json(text: str) -> dict:
    """
    Extract JSON string from text and validate it.
    
    :param text: Input text containing JSON
    :return: Extracted and validated JSON as a Python dictionary
    """
    try:
        # Find the first '{' and the last '}'
        start = text.index('{')
        end = text.rindex('}') + 1
        json_str = text[start:end]
        
        # Parse the JSON string
        json_obj = json.loads(json_str)
        return json_obj
    except (ValueError, json.JSONDecodeError) as e:
        logging.error(f"Failed to extract or parse JSON: {str(e)}")
        return {}

