# API Documentation

## PDFProcessor

### `pdf_to_markdown_json(pdf_path: str, json_path: str) -> dict`

Converts a PDF file to a JSON file where each page is a key and its value is the Markdown content.

- **Parameters**:
  - `pdf_path` (str): Path to the input PDF file.
  - `json_path` (str): Path to save the output JSON file.
- **Returns**: dict: A dictionary where keys are page numbers and values are Markdown strings.

## LLMOllama

### `__init__(self, config_path: str = None)`

Initialize LLMOllama class and load configuration file.

- **Parameters**:
  - `config_path` (str, optional): The path to the configuration file.

### `generate_response(self, system_prompt: str, user_prompt: str) -> str`

Generate response using the specified model.

- **Parameters**:
  - `system_prompt` (str): System prompt to set the behavior of the model.
  - `user_prompt` (str): User prompt, i.e., the question or task to be answered/completed.
- **Returns**: str: Generated response text.

## Utility Functions

### `logging_decorator(func: Callable) -> Callable`

A decorator that logs execution time and word counts for the decorated function.

### `setup_logger(name: str, log_file: str, level: int = logging.INFO) -> logging.Logger`

Sets up a logger with the specified name and log file.

- **Parameters**:
  - `name` (str): Name of the logger.
  - `log_file` (str): Path to the log file.
  - `level` (int, optional): Logging level. Defaults to logging.INFO.
- **Returns**: logging.Logger: Configured logger object.

For more detailed information on usage and implementation, refer to the source code and comments in each module.