# src/app/main.py

import os
import json
import yaml
from src.data.data_processor import PDFProcessor
from src.models.ollama_client import LLMOllama
from src.utils.helpers import setup_logger, extract_and_validate_json
from tqdm import tqdm

# Load configuration
with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

# Setup logger
current_dir = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(current_dir, '..', '..', config['logging']['file_path'])
logger = setup_logger('main_app', log_file)

def process_pdf(pdf_path: str, json_path: str) -> dict:
    """
    Process PDF and convert it to JSON with markdown content.
    """
    processor = PDFProcessor()
    return processor.pdf_to_markdown_json(pdf_path, json_path)

def process_markdown_with_llm(markdown_dict: dict, system_prompt: str, llm_client: LLMOllama) -> dict:
    """
    Process markdown content with LLM.
    """
    results = {}
    for page_num, markdown_content in tqdm(markdown_dict.items(), desc="Processing pages"):
        user_prompt = f"###markdown string###\n{markdown_content}\n\n###output json###"
        result = llm_client.generate_response(system_prompt, user_prompt)
        results[page_num] = result
    return results

def load_system_prompt(file_path: str) -> str:
    """
    Load system prompt from a text file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().strip()

def save_json_results(results: dict, output_dir: str, base_filename: str):
    """
    Save JSON results for each page in separate files.
    """
    os.makedirs(output_dir, exist_ok=True)
    for page_num, content in results.items():
        json_obj = extract_and_validate_json(content)
        if json_obj:
            filename = f"{base_filename}_page_{page_num}.json"
            file_path = os.path.join(output_dir, filename)
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(json_obj, file, ensure_ascii=False, indent=2)
            logger.info(f"Saved JSON for page {page_num} to {file_path}")
        else:
            logger.warning(f"Failed to extract valid JSON for page {page_num}")

def main():
    # Set up paths
    input_path = os.path.join(config['app']['input_dir'], config['app']['default_input_file'])
    temp_json_path = os.path.join(config['app']['temp_dir'], config['app']['temp_markdown_name'])
    output_dir = config['app']['output_dir']
    system_prompt_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'system_prompt.txt')
    
    # Ensure directories exist
    os.makedirs(config['app']['input_dir'], exist_ok=True)
    os.makedirs(config['app']['output_dir'], exist_ok=True)
    os.makedirs(config['app']['temp_dir'], exist_ok=True)
    
    # Process PDF
    logger.info(f"Starting PDF processing for file: {input_path}")
    markdown_dict = process_pdf(input_path, temp_json_path)
    logger.info("PDF processing completed")
    
    # Set up LLM client
    llm_client = LLMOllama(config_path='config.yaml')
    
    # Load system prompt
    system_prompt = load_system_prompt(system_prompt_path)
    
    # Process markdown with LLM
    logger.info("Starting LLM processing")
    results = process_markdown_with_llm(markdown_dict, system_prompt, llm_client)
    logger.info("LLM processing completed")
    
    # Save JSON results
    base_filename = os.path.splitext(config['app']['default_input_file'])[0]
    save_json_results(results, output_dir, base_filename)
    
    # Clean up temporary file
    if os.path.exists(temp_json_path):
        os.remove(temp_json_path)
        logger.info(f"Temporary file {temp_json_path} removed")
    
    # Display sample result
    sample_page = next(iter(results))
    print(f"\nSample result for {sample_page}:")
    print(results[sample_page][:500] + "...")  # Display first 500 characters

if __name__ == "__main__":
    main()