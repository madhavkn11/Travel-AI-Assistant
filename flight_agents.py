from config import llm



class FlightAgent:

    def run(self, context):

        prompt = f"""
You are an expert travel assistant.

Using the information below,
generate a concise flight summary.

Return only:

✈ Nearest Airport

🛫 Airport Code

🛩 Major Airlines

💰 Approximate Fare (INR)

📅 Best Time to Book

✈ Travel Tip

Keep the answer under 150 words.

Context:

{context}
"""

        return llm.invoke(prompt).content