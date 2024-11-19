# PDF Classification Project

This project aims to classify PDF documents into broad categories using AI-powered analysis. It utilizes multiple Large Language Models to analyze PDF content and assign appropriate tags.

## Datasets and Resources

- [URL Classifications Dataset](https://huggingface.co/datasets/snats/url-classifications)
- [URL Embeddings Dataset](https://www.kaggle.com/datasets/santiagopedroza/url-embeddings-cc-provenance)
- [CC-MAIN-2021-31-PDF-UNTRUNCATED Data Card](https://corp.digitalcorpora.org/corpora/files/CC-MAIN-2021-31-PDF-UNTRUNCATED/)

## Project Structure

- `training.py`: Main script for PDF classification
- `prompt.txt`: Contains the prompt used for classification
- `.env`: Stores environment variables (e.g., OpenAI API key)
- `.gitignore`: Specifies intentionally untracked files to ignore

## Setup and Installation

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install required packages:
   ```
   pip install openai python-dotenv pandas tqdm
   ```
4. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

1. Ensure your input CSV file is in the `./data/` directory
2. Run the classification script:
   ```
   python training.py
   ```
3. The script will generate an output CSV file with classifications added

## Features

- Uses OpenAI's GPT-3.5-turbo model for classification
- Supports custom prompts for classification
- Handles errors and continues processing
- Outputs results to a CSV file

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/pdf-classification-project/issues) if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)

