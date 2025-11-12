import os
import tempfile

# Disable TensorFlow/Flax in Transformers before any imports that may load it
os.environ.setdefault('TRANSFORMERS_NO_TF', '1')
os.environ.setdefault('TRANSFORMERS_NO_FLAX', '1')

import streamlit as st

from textsummarizationproject1 import (
    extract_text_from_pdf,
    clean_text,
    split_into_chunks,
    get_important_sentences,
    abstractive_summarizer,
)

st.set_page_config(page_title="Text Summarization Tool", layout="wide")
st.title("Text Summarization Tool")

with st.sidebar:
    st.header("Settings")
    chunk_size = st.number_input("Chunk size (words)", min_value=200, max_value=5000, value=1500, step=100)
    top_n = st.number_input("Extractive Top-N sentences", min_value=3, max_value=50, value=10, step=1)
    max_chunks = st.number_input("Max chunks to process", min_value=1, max_value=100, value=3, step=1)
    do_abstractive = st.checkbox("Run abstractive summarization (slower)", value=True)
    model_choice = st.selectbox(
        "Abstractive model",
        options=[
            "sshleifer/distilbart-cnn-12-6",  # fast
            "facebook/bart-large-cnn",        # higher quality, slower
        ],
        index=0,
    )

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"]) 

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.getbuffer())
        pdf_path = tmp.name

    with st.spinner("Extracting and cleaning text..."):
        raw_text = extract_text_from_pdf(pdf_path)
        os.unlink(pdf_path)
        cleaned_text = clean_text(raw_text)
        chunks = split_into_chunks(cleaned_text, chunk_size=chunk_size)
        if len(chunks) > max_chunks:
            chunks = chunks[:max_chunks]

    st.subheader("Summary")
    if not chunks:
        st.warning("No text extracted from the PDF. Please try another file.")
    else:
        if st.button("Run Summarization"):
            with st.spinner("Generating summaries. This can take a while..."):
                try:
                    progress = st.progress(0)
                    extractive_summary = []
                    abstractive_summary = []
                    total = len(chunks)
                    for i, chunk in enumerate(chunks, start=1):
                        extractive_summary.append(get_important_sentences(chunk, top_n=top_n))
                        if do_abstractive:
                            abstractive_summary.append(abstractive_summarizer(chunk, model_name=model_choice))
                        else:
                            abstractive_summary.append("")
                        progress.progress(int(i * 100 / total))
                except Exception as e:
                    st.error(f"Summarization failed: {e}")
                    st.stop()

            st.write("### Extractive Summaries")
            for i, summary in enumerate(extractive_summary, start=1):
                st.markdown(f"**Chunk {i}:** {summary}")

            if do_abstractive:
                st.write("### Abstractive Summaries")
                for i, summary in enumerate(abstractive_summary, start=1):
                    st.markdown(f"**Chunk {i}:** {summary}")

            combined_summary = "\n\n".join([
                (
                    f"Extractive (Chunk {i}):\n{ext}\n\nAbstractive (Chunk {i}):\n{abs_}"
                    if do_abstractive else f"Extractive (Chunk {i}):\n{ext}"
                )
                for i, (ext, abs_) in enumerate(zip(extractive_summary, abstractive_summary), start=1)
            ])

            st.download_button(
                label="Download Combined Summary",
                data=combined_summary,
                file_name="summary.txt",
                mime="text/plain",
            )
else:
    st.info("Please upload a PDF to begin.")
