import streamlit as st
from Helper import user_input
from evaluate import load
# Load the ROUGE metric
import evaluate

def create_ui():
    st.title("PDF made easy!")
    # st.sidebar.image("image.png", use_column_width=True)
    st.sidebar.write("### Welcome to PDF made easy!")
    st.sidebar.write("Ask a question below and get instant insights.")

    # Add some instructions
    st.markdown("### Instructions")
    st.markdown(
        """
        1. Enter your question in the text box below.
        2. Click on 'Submit' to get the response.
        3. View the answer generated based on the context from the PDFs and URLs provided.
        """
    )

    # Get user input
    question = st.text_input("Ask a question:")

    # Call user_input function when user clicks submit
    if st.button("Submit"):
        with st.spinner("Generating response..."):
            response , context_docs = user_input(question)
            rouge = evaluate.load('rouge')
            output_text = response.get('output_text', 'No response')  # Extract the 'output_text' from the response
            context = ' '.join([doc.page_content for doc in context_docs])
            # Ensure predictions and references are lists of strings
            results = rouge.compute(predictions=[output_text], references=[context])
            st.success("Response:")
            st.write(output_text)
            st.success("Rougue score:")
            st.write(results)

    # Add some footer
    st.markdown("---")
    st.markdown("**Powered by**: Shaurya Mishra")

# Main function to run the app
def main():
    create_ui()

if __name__ == "__main__":
    main()
