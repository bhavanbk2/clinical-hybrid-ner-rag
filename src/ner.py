from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

model_name = "emilyalsentzer/Bio_ClinicalBERT"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

nlp = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

def extract_entities(text):
    return nlp(text)

if __name__ == "__main__":
    sample_text = "Patient diagnosed with diabetes and prescribed Metformin."
    entities = extract_entities(sample_text)
    print(entities)