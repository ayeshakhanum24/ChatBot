import random
from transformers import pipeline

# Step 1: Load an NLP Model
bot = pipeline("text-generation", model="gpt-2")

# Step 2: Classify User as Technical or Non-Technical
def classify_user(query):
    tech_keywords = ["algorithm", "runtime", "OOP", "data structure"]
    if any(keyword in query for keyword in tech_keywords):
        return "technical"
    return "non-technical"

# Step 3: Generate Response Based on User Type
def generate_response(query, user_type):
    if user_type == "technical":
        # Provide detailed, technical explanation
        response = bot(query, max_length=50)[0]['generated_text']
    else:
        # Provide simplified explanation
        response = bot(f"Simplified: {query}", max_length=50)[0]['generated_text']
    return response

# Step 4: Ask for Feedback and Adjust Score
feedback_score = {}

def ask_feedback(query):
    feedback = input("Was this answer helpful? (yes/no): ").lower()
    if feedback == "yes":
        feedback_score[query] = feedback_score.get(query, 0) + 1
    else:
        feedback_score[query] = feedback_score.get(query, 0) - 1

# Step 5: Transliteration (Mock Example)
def transliterate_query(query):
    # Example: simple mock transliteration
    transliterated_query = query.replace("namaste", "hello")
    return transliterated_query

# Bot Interaction Example
query = input("Ask a question: ")
transliterated_query = transliterate_query(query)
user_type = classify_user(transliterated_query)
response = generate_response(transliterated_query, user_type)
print(response)
ask_feedback(query)
