# Project Overview

## PDF to JSON Converter with LLM Processing

This project is designed to convert PDF documents into structured JSON format using a combination of PDF parsing and Large Language Model (LLM) processing. The main components of the system are:

1. **PDF Processor**: Converts PDF documents into markdown-formatted JSON.
2. **LLM Client**: Interfaces with an LLM (using Ollama) to process the markdown content.
3. **Main Application**: Orchestrates the entire process from PDF input to final JSON output.

### Key Features

- PDF to Markdown conversion
- LLM-based content structuring
- Modular design for easy maintenance and extension
- Logging and error handling
- Configurable system prompts

### Usage

To use this application, run the `scripts/run_app.py` script. Make sure to configure the input PDF path and other settings as needed.

For more detailed information, refer to the `README.md` file in the project root directory.