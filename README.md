# PDF to Structured JSON Converter

This project converts PDF documents into structured JSON format using a combination of PDF parsing, markdown conversion, and Large Language Model (LLM) processing.

## Project Workflow

1. **PDF to HTML Conversion**
   - The PDF file is read and converted to HTML format.
   - This step preserves the structure and formatting of the original PDF.

2. **HTML to Markdown Conversion**
   - The HTML content is then converted to Markdown format.
   - This step simplifies the content while maintaining basic structure.

3. **Markdown to LLM Input**
   - The Markdown content is prepared as input for the Large Language Model.
   - Each page of the PDF is processed separately.

4. **LLM Processing**
   - The prepared Markdown content is sent to the LLM (using Ollama).
   - The LLM analyzes the content and generates a structured response.

5. **LLM Output to JSON**
   - The LLM's output (a string containing JSON) is extracted and parsed.
   - Valid JSON is extracted from the LLM's response.

6. **JSON Storage**
   - The extracted JSON for each page is saved as a separate file.
   - Files are named based on the original PDF name and page number.

## Prerequisites

Before running this project, ensure you have the following installed:

1. Python 3.9 or higher
2. Ollama - Follow the installation instructions at [Ollama's official website](https://ollama.ai/)

## Installation

1. Install the required Python libraries:
   ```
   pip install -r requirements.txt
   ```

2. Download and run the required Ollama model:
   ```
   ollama run qwen2:7b
   ```
   Note: Ensure the model name in the command matches the one specified in your `config.yaml` file.

## Configuration

Adjust the `config.yaml` file in the project root to set your preferences:

- Specify input and output directories
- Set the Ollama model and its parameters
- Configure logging preferences

## Usage

This project uses a Makefile to simplify common tasks. Here are the main commands you can use:

1. **Run the application**:
   ```
   make run
   ```
   This command will process the PDF specified in your configuration, convert it to structured JSON, and save the results in the specified output directory.

2. **Set up the project**:
   ```
   make setup
   ```
   This will create the necessary environment and install all required dependencies.

3. **Clean up**:
   ```
   make clean
   ```
   This will remove any temporary files or build artifacts.

To see all available commands, you can run:
```
make help
```

Note: Ensure you are in the project root directory when running these commands.

For more detailed information about each command, you can check the `Makefile` in the project root.

## Output

The script generates:
- A temporary Markdown JSON file (deleted after processing)
- Individual JSON files for each page of the processed PDF

## Troubleshooting

If you encounter any issues:
1. Check the log files in the `logs` directory.
2. Ensure all dependencies are correctly installed.
3. Verify that Ollama is running and the specified model is available.


## Project Structure

```
project_root/
│
├── src/                      # Source code directory
│   ├── data/                 # Data processing related code
│   │   ├── __init__.py
│   │   └── data_processor.py # PDF to Markdown conversion functionality
│   │
│   ├── models/               # Model related code
│   │   ├── __init__.py
│   │   ├── ollama_client.py  # Ollama LLM API interaction interface
│   │   └── system_prompt.txt # System prompt for the LLM
│   │
│   ├── utils/                # Utility functions
│   │   ├── __init__.py
│   │   └── helpers.py        # Helper functions (logging, JSON extraction)
│   │
│   └── app/                  # Main application code
│       ├── __init__.py
│       └── main.py           # Main application logic
│
├── scripts/                  # Script directory
│   └── run_app.py            # Script to run the application
│
│
├── data/                     # Data directory
│   ├── raw/                  # Raw PDF files
│   ├── processed/            # Processed JSON output
│   └── temp/                 # Temporary files
│
├── logs/                     # Log files directory
│
├── docs/                     # Documentation directory
│   ├── project_overview.md   # Project overview
│   └── api_documentation.md  # API documentation
│
├── config.yaml               # Configuration file
├── requirements.txt          # Project dependencies
├── README.md                 # Project README (this file)
└── .gitignore                # Git ignore file
```

### Key Components and Their Functions:

1. **data_processor.py**: 
   - Handles the conversion of PDF files to Markdown format.
   - Uses libraries like PyPDF2 and BeautifulSoup for parsing and conversion.

2. **ollama_client.py**: 
   - Manages interactions with the Ollama LLM API.
   - Sends prompts and receives responses from the LLM.

3. **helpers.py**: 
   - Contains utility functions used across the project.
   - Includes logging setup and JSON extraction functions.

4. **main.py**: 
   - Orchestrates the overall process flow.
   - Calls functions from other modules to process PDFs and generate JSON output.

5. **run_app.py**: 
   - Entry point script to run the application.
   - Sets up necessary paths and calls the main function.

6. **config.yaml**: 
   - Contains configuration settings for the application.
   - Includes paths, Ollama model settings, and other parameters.

7. **system_prompt.txt**: 
   - Contains the system prompt used to instruct the LLM on how to process the input.

8. **test_data_processor.py**: 
   - Contains unit tests for the data processing functionality.