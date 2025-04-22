import pandas as pd

def serialize_tabular_to_narrative(df_row):
    narrative = (f"Patient {df_row['patient_id']} has {df_row['condition']} "
                 f"with lab result {df_row['lab_result']} recorded on {df_row['date']}.")
    return narrative

if __name__ == "__main__":
    sample_data = {
        'patient_id': '12345',
        'condition': 'diabetes',
        'lab_result': 'high glucose',
        'date': '2025-04-21'
    }
    narrative = serialize_tabular_to_narrative(sample_data)
    print(narrative)