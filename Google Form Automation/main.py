import pandas as pd
import requests
import time
import random
import sys

# Open google form and copy paste the link below.
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSc50CdwmVWbDCKOr1XoX1g2GVsVnNX35oqmX7bHElieKEQP8A/viewform"

# Change the values of Excel sheet headers and Google form questions entry Id. Check ReadMe for how to get the entry id.
ENTRY_IDS = {
    'Full Name': 'entry.2092238618',
    'Email': 'entry.1556369182',
    'Mobile Number': 'entry.1458330635',
    'Year of Study': 'entry.479301265',
}

# Change the name of excel sheet from here. Make sure your excel sheet is in same folder as main.py (this file)
EXCEL_SHEET = 'students.xlsx'



FORM_URL = FORM_URL.replace("viewform", "formResponse")

try:
    df = pd.read_excel(EXCEL_SHEET)
except Exception as e:
    print(f"[!] Failed to load Excel file: {e}")
    sys.exit(1)

# This will end the execution of program if there is any invalid value or Null value in excel sheet.
for idx, row in df.iterrows():
    for col in df.columns:
        val = str(row[col]).strip()
        if val == '' or pd.isna(val):
            print(f"[✗] Null or invalid value in row {idx + 1}, column '{col}'. Halting execution.")
            sys.exit(1)

    form_data = {
        ENTRY_IDS[col]: str(row[col]).strip() for col in df.columns
    }


    try:
        response = requests.post(FORM_URL, data=form_data)

        if response.status_code == 200:
            print(f"[✓] Submitted row {idx + 1} successfully.")
        else:
            print(f"[✗] Failed to submit row {idx + 1}: HTTP {response.status_code}")
            sys.exit(1)

    except Exception as e:
        print(f"[!] Error submitting row {idx + 1}: {e}")
        sys.exit(1)


    # Change Random delay here by adjusting the range. (Start, End). (10,20) means a random delay between 10s to 20s
    delay = random.randint(5, 20)

    print(f"⏳ Waiting for {delay} seconds before next submission...")
    time.sleep(delay)