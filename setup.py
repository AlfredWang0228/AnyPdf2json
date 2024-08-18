from setuptools import setup, find_packages

setup(
    name="pdf_to_json_converter",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'PyPDF2==3.0.1',
        'beautifulsoup4==4.12.3',
        'markdownify==0.13.1',
        'PyYAML==6.0.2',  # Using the latest version you provided
        'tqdm==4.66.4',
        'ollama==0.3.1',
        'reportlab==4.2.2',
    ],
    author="Yuxiang Wang",
    author_email="yuxiang.wang@hillresearch.ai",
    description="A tool to convert PDF to structured JSON using LLM processing",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    python_requires='>=3.9'
)