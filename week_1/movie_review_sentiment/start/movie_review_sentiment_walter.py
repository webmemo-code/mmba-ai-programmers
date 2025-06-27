from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()

def analyze_sentiment(review):
    """
    Analyze the sentiment of a movie review using structured output.
    Returns a dictionary with 'thought' and 'sentiment' keys.
    """
    # TODO: Create a prompt that:
    # 1. Asks for sentiment analysis
    # 2. Specifies the required output format
    #       thought: [analysis]
    #       sentiment: [positive/negative/mixed]
    # 3. Includes the review text
    prompt = f"""
    Analyze the sentiment of the following movie review. Provide your analysis in exactly this format:
    
    thought: [Your detailed analysis of the review]
    sentiment: [positive, negative, or mixed]
    
    Review: {review}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    content = response.choices[0].message.content
    
    # Parse the response to extract thought and sentiment
    lines = content.strip().split('\n')
    thought = ""
    sentiment = ""
    
    for line in lines:
        line = line.strip()
        if line.startswith("thought:"):
            thought = line.replace("thought:", "").strip()
        elif line.startswith("sentiment:"):
            sentiment = line.replace("sentiment:", "").strip()
    
    result = {
        "thought": thought,
        "sentiment": sentiment
    }
    
    return result

def main():
    # Test cases
    reviews = [
        "This film shouldn't work at all. It doesn't have much of a story and the whole dial up internet thing is incredibly dated. However Hanks and Ryan sell it beautifully.",
        "The movie was terrible. The acting was wooden, the plot made no sense, and I want my two hours back.",
        "An absolute masterpiece! The cinematography was stunning, the acting was superb, and the story kept me engaged from start to finish."
    ]

    # Test each review
    for i, review in enumerate(reviews, 1):
        result = analyze_sentiment(review)
        print(f"\nReview {i}:")
        print(f"Thought: {result['thought']}")
        print(f"Sentiment: {result['sentiment']}")

if __name__ == "__main__":
    main()