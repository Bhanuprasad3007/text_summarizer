🧠 Text Summarization Project
🔍 Overview

This project is an AI-powered text summarization tool that automatically extracts and summarizes the contents of PDF documents.
It uses both extractive and abstractive approaches:

🧩 Extractive Summarization – Selects the most important sentences from the text using TF-IDF.

🤖 Abstractive Summarization – Uses Transformer-based deep learning models (like BART) to generate human-like summaries.

You can use the Streamlit web app to upload a PDF, adjust settings, and download the summarized output.

🚀 Features

✅ Extract text directly from PDF files
✅ Clean and preprocess raw text
✅ Split long documents into chunks for better summarization
✅ Perform extractive summarization using TF-IDF
✅ Perform abstractive summarization using Hugging Face models
✅ Web interface built with Streamlit
✅ Download combined summary as a .txt file

🏗️ Project Structure
📂 TextSummarizationProject
│
├── textsummarizationproject1.py      # Backend logic (PDF → Text → Summaries)
├── app.py                            # Streamlit frontend interface
├── requirements.txt                  # Dependencies list
└── README.md                         # Documentation (this file)

⚙️ Installation & Setup
1️⃣ Clone this Repository
git clone https://github.com/yourusername/text-summarization-project.git
cd text-summarization-project

2️⃣ Create a Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate     # for macOS/Linux
venv\Scripts\activate        # for Windows

3️⃣ Install Dependencies

Create a file named requirements.txt (or use the one below 👇)
streamlit
transformers
torch
pdfminer.six
scikit-learn
nltk
Then run:
pip install -r requirements.txt

4️⃣ Download NLTK Resources
The script automatically downloads them, but if you want to do it manually:

import nltk
nltk.download('punkt')
nltk.download('stopwords')

🧩 Usage Guide
🧱 Option 1: Run from Command Line
If you only want to run the backend script:
python textsummarizationproject1.py
Place your PDF file in the same folder.
Update the filename in the code:
pdf_file_path = "yourfile.pdf"
It will print summaries directly in the terminal.

🌐 Option 2: Run the Streamlit App (Recommended)
Launch the web app:
streamlit run app.py
Then open the displayed local URL (e.g., http://localhost:8501/).

🧭 Steps inside the app:

Upload a PDF file.
Configure summarization settings (chunk size, top-N sentences, model choice).
Click “Run Summarization”.
View extractive and abstractive summaries.
Click “Download Combined Summary” to save the result.

🧮 How It Works
🧾 Pipeline
Step	Process	Description
1️⃣	Extract	Uses pdfminer to read text from PDF
2️⃣	Clean	Removes special characters, extra spaces, and normalizes text
3️⃣	Chunking	Splits text into smaller chunks to fit model input limits
4️⃣	Extractive Summary	Uses TF-IDF to select key sentences
5️⃣	Abstractive Summary	Uses pretrained Transformer models to generate new summaries
6️⃣	Combine	Merges both summaries for final output
🧰 Models Used
Model	Description	Speed
sshleifer/distilbart-cnn-12-6	Fast and lightweight, ideal for quick summarization	⚡ Fast
facebook/bart-large-cnn	Higher quality abstractive summaries	🐢 Slower
Both are Hugging Face Transformer models.

📊 Example Output

Original PDF Text (Excerpt):
“Cloud computing is a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources...”
Extractive Summary:
Cloud computing enables on-demand access to configurable resources. It supports scalability and flexibility for various applications.
Abstractive Summary:
Cloud computing provides scalable, flexible, and on-demand access to shared IT resources.

💡 Customization Tips

Adjust chunk_size for longer or shorter summaries.
Increase top_n to include more sentences in the extractive summary.
Switch models for faster or more detailed summaries.
Extend abstractive_summarizer() with other Hugging Face models like t5-small or pegasus.

🧑‍💻 Developer Notes

Ensure your system has enough RAM (abstractive models can be memory-heavy).
For large PDFs, increase the max_chunks setting in Streamlit.
The abstractive model runs on CPU by default (to avoid CUDA setup).

🧾 License

This project is released under the MIT License.
You can freely use, modify, and distribute it.

🙌 Credits

Hugging Face Transformers
NLTK
Scikit-learn
Streamlit
PDFMiner.six

📧 Contact

For queries or contributions, feel free to reach out:
Author: Bhanu Prasad N
Email: bhanuprasad3007@gmail.com
GitHub: github.com/Bhanuprasad3007
