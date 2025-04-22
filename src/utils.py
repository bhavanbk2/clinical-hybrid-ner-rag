import pandas as pd

def load_tabular_data(filepath):
    return pd.read_csv(filepath)

def load_clinical_notes(filepath):
    with open(filepath, 'r') as file:
        notes = file.read()
    return notes
