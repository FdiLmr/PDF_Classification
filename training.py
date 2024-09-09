import os
import time
from openai import OpenAI
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm, trange
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create the OpenAI client using the API key from the environment
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

# Function to read the prompt from the file
def read_prompt(file_path='prompt.txt'):
    with open(file_path, 'r') as file:
        return file.read()

PDF_CLASSIFICATION_PROMPT = read_prompt()
CSV_FILE_PATH = './data/cc-provenance-20230324-1k.csv'
CLASSIFIED_ALREADY = './data/classified_pdfs_1k.csv'
OUTPUT_FILE = './output/classified_pdfs_1k_gpt.csv'

# Function to classify the PDF using OpenAI API
def classify_pdf(pdf_url):
    prompt = PDF_CLASSIFICATION_PROMPT.format(pdf_url=pdf_url)

    # Make the API call to the OpenAI model
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # You can also use "gpt-4" if needed
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=10,  # Short tags only
        temperature=0,  # Lower temperature for more deterministic output
    )
    return response.choices[0].message.content.strip()

# Function to classify all the PDFs in the CSV file
def classify_pdfs_in_csv(input_csv, output_csv):
    # Read input CSV and open output CSV
    with open(input_csv, 'r') as infile, open(output_csv, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['classification']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            pdf_url = row['url']
            try:
                classification = classify_pdf(pdf_url)
                row['classification'] = classification
            except Exception as e:
                print(f"Error classifying {pdf_url}: {e}")
                row['classification'] = 'error'

            writer.writerow(row)

# Run the classification process
classify_pdfs_in_csv(CSV_FILE_PATH, OUTPUT_FILE)