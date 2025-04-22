import os
from langchain.llms import OpenAI

os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

llm = OpenAI(model="gpt-4o")

def generate_diagnosis(context):
    prompt = f"Based on the following context, provide a clinical diagnosis:\n{context}\nDiagnosis:"
    response = llm(prompt)
    return response.strip()

if __name__ == "__main__":
    context = "Patient exhibits symptoms of high glucose, frequent urination, and excessive thirst."
    diagnosis = generate_diagnosis(context)
    print(diagnosis)
