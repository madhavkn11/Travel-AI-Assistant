from config import llm


class ChatService:

    def chat(self, guide, question):

        prompt = f"""
You are an expert AI Travel Assistant.

Travel Guide:

{guide}

User Question:

{question}

Answer the user's question using the travel guide above.
If modifications are requested, rewrite only the relevant parts.
"""

        response = llm.invoke(prompt)

        return response.content