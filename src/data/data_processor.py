# src/data/data_processor.py

import PyPDF2
import os
import html
import json
from bs4 import BeautifulSoup
from markdownify import markdownify as md

class PDFProcessor:
    @staticmethod
    def pdf_to_markdown_json(pdf_path, json_path):
        """
        Convert a PDF file to a JSON file where each page is a key and its value is the Markdown content.
        
        Args:
        pdf_path (str): Path to the input PDF file.
        json_path (str): Path to save the output JSON file.
        
        Returns:
        dict: A dictionary where keys are page numbers and values are Markdown strings.
        """
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            pages_dict = {}
            
            for page_num, page in enumerate(reader.pages, 1):
                text = page.extract_text()
                html_content = "<div class='page'>"
                for paragraph in text.split('\n'):
                    html_content += f"<p>{html.escape(paragraph)}</p>"
                html_content += "</div>"
                
                soup = BeautifulSoup(html_content, 'html.parser')
                markdown_content = md(str(soup))
                pages_dict[f"page_{page_num}"] = markdown_content.strip()
            
        with open(json_path, 'w', encoding='utf-8') as output_file:
            json.dump(pages_dict, output_file, ensure_ascii=False, indent=2)
        
        print(f"Conversion complete. JSON file saved to {json_path}")
        return pages_dict

    @staticmethod
    def display_original_markdown(json_path, page_num):
        """
        Display the original Markdown content for a specific page.
        
        Args:
        json_path (str): Path to the JSON file containing Markdown content.
        page_num (str): Page number to display (e.g., "page_1").
        
        Returns:
        str: Markdown content of the specified page, or None if page not found.
        """
        with open(json_path, 'r', encoding='utf-8') as file:
            markdown_dict = json.load(file)
        if page_num in markdown_dict:
            print(f"\nOriginal Markdown content of {page_num}:")
            return markdown_dict[page_num]
        else:
            print(f"Page {page_num} not found in the document.")
            return None