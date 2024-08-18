# src/models/ollama_client.py

import ollama
import yaml
import os
from typing import Dict, Any
from src.utils.helpers import logging_decorator, setup_logger

# Setup logger with a relative path
current_dir = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(current_dir, '..', '..', 'logs', 'ollama_client.log')
logger = setup_logger('ollama_client', log_file)


class LLMOllama:
    def __init__(self, config_path: str = 'config.yaml'):
        """
        Initialize LLMOllama class and load configuration file.
        :param config_path: The path to the configuration file
        """
        self.config = self.load_config(config_path)
        self.model = self.config['ollama']['model']
        self.options = self.config['ollama']['options']

    def load_config(self, config_path: str) -> Dict[str, Any]:
        """
        Load the configuration file.
        :param config_path: The path to the configuration file
        :return: Configuration dictionary
        """
        try:
            with open(config_path, 'r') as file:
                config = yaml.safe_load(file)
            return config
        except Exception as e:
            logger.error(f"Failed to load config file: {str(e)}")
            raise Exception(f"Failed to load config file: {str(e)}")

    @logging_decorator
    def generate_response(self, system_prompt: str, user_prompt: str) -> str:
        """
        Generate response using the specified model.
        :param system_prompt: System prompt to set the behavior of the model
        :param user_prompt: User prompt, i.e., the question or task to be answered/completed
        :return: Generated response text
        """
        try:
            response = ollama.generate(
                model=self.model,
                system=system_prompt,
                prompt=user_prompt,
                options=self.options
            )
            return response['response']
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            return f"An error occurred: {str(e)}"

# Example usage
if __name__ == "__main__":
    llm_ollama = LLMOllama()
    system_prompt = "You are a helpful assistant with expertise in programming and technology."
    user_prompt = "Explain the concept of recursion in programming."
    result = llm_ollama.generate_response(system_prompt, user_prompt)
    print(result)