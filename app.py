import streamlit as st
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import nltk
nltk.download('punkt')

def generate_summary(text, num_sentences=3):
    # Initialize the parser with the given text
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    
    # Initialize the LexRank summarizer
    summarizer = LexRankSummarizer()
    
    # Generate the summary
    summary = summarizer(parser.document, num_sentences)
    
    # Convert the summary to a string
    summary_text = ' '.join(str(sentence) for sentence in summary)
    
    return summary_text

def main():
    # Set page title and description
    st.set_page_config(page_title='Text Summarizer App', page_icon=':memo:', layout='centered')
    
    # Set app title and description
    st.title('Text Summarizer App')
    st.markdown('Enter the document or text and click the **Generate Summary** button to get a summary.')
    
    # Get user input
    document = st.text_area("Enter the document or text:")
    
    if st.button("Generate Summary"):
        # Generate the summary
        summary = generate_summary(document)
        
        # Print the summary
        st.subheader("Summary:")
        st.write(summary)

if __name__ == '__main__':
    main()
