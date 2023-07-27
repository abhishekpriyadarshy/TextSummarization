from transformers import pipeline

# Load the pre-trained model for summarization
summarizer = pipeline("summarization")


# Example text for summarization
text = """
Artificial intelligence (AI) technology is fundamentally shaping how contact centers operate, significantly improving customer experience while delivering cost savings and efficiencies. As evidence of its value grows, AI is increasingly considered a necessity to compete effectively by delivering faster, more accurate customer service.

CX professionals understand the importance of AI, yet organizations still struggle to deploy and adopt this technology in truly meaningful ways. 89% of CX professionals believe in the importance of leveraging AI in the contact center, yet only 14% of organizations consider themselves “transformational” in employing AI to do heavy lifting for the business.

This report examines the evolving perceptions of AI and its maturity in the CX space. Download the report to explore these key drivers and expectations, as well as four key predictions on how AI will shape the contact center through 2025.

"""

#Method to summarize text
def perform_text_summary(text):
    
    # Generate the summary
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)

    # Get the summarized text
    summarized_text = summary[0]['summary_text']

    return {'result' : summarized_text}

# Generate the summary
summary = summarizer(text, max_length=150, min_length=30, do_sample=False)

# Get the summarized text
summarized_text = summary[0]['summary_text']

if __name__ == "__main__":
   summarized_text = perform_text_summary(text)
   # Print the summary
   print("Text Summary:")
   print(summarized_text)