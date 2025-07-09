
# 📋 Google Form Autofill Script

This Python script automates the process of submitting responses to a Google Form using data from an Excel file. It's ideal for batch entries such as student registrations, surveys, or attendance.

---

## 📁 Folder Structure

```
project-folder/
├── main.py             # The main Python script
├── students.xlsx       # Excel file with the form data
└── README.md           # Documentation (this file)
```

---

## ✅ Requirements

- Python 3.6 or above
- Required libraries:

```bash
pip install pandas requests openpyxl
```

---

## 💬 Prompt to generate a dummy Excel sheet.

🎯 Task:
Generate a realistic Excel sheet with dummy data to match the structure of a Google Form.

🧾 Form Structure:
- Field 1: [Label] ([Type])
- Field 2: [Label] ([Type])
- Field 3: [Label] ([Type with options if applicable])
- ...
(Note: Replace [Label] and [Type] with actual values. Supported types: Text, Email, Number, Dropdown, Radio, Checkbox)

🔢 Number of Rows:
- Generate [X] rows of unique, varied dummy data.

📄 Output Format:
- Excel (.xlsx) file with a header row.
- Column headers must exactly match the field labels above.

📌 Notes:
- For "Email", base the value on the generated names.
- For "Mobile Number", use valid-looking values (e.g., 10-digit Indian format).
- For multiple-choice or dropdown fields, pick randomly from given options.


## 📄 Excel Sheet Format (`students.xlsx`)

The Excel file must be placed in the same folder as `main.py`. The headers in your Excel file must exactly match the keys in the `ENTRY_IDS` dictionary inside the script.

**Example Excel layout:**

| Full Name   | Email                | Mobile Number | Year of Study |
|-------------|----------------------|---------------|---------------|
| Student1    | student1@example.com | 9473783073    | Third         |
| Student2    | student2@example.com | 9270540632    | Second        |

---

## 🔗 How to Get Google Form Entry IDs

I have made a dedicated youtube video for this watch it here:

[![WATCH THE VIDEO HERE](http://img.youtube.com/vi/rL4b6JKEVpo/0.jpg)](http://www.youtube.com/watch?v=rL4b6JKEVpo)

```python
ENTRY_IDS = {
    'Full Name': 'entry.2092238618',
    'Email': 'entry.1556369182',
    'Mobile Number': 'entry.1458330635',
    'Year of Study': 'entry.479301265',
}
```

Make sure the Excel column names **match exactly**.

---

## 🚀 How to Run the Script

Run the script from the terminal:

```bash
python main.py
```

What it does:
- Reads each row from `students.xlsx`
- Submits each row as a new form entry
- Waits for a random delay (10–20 seconds) between submissions

---

## ⚠ Error Handling

- The script stops if:
  - Any field is empty (`null` or blank)
  - A network error or non-200 HTTP status is encountered
- You can configure the delay range and column names in the script

---

## 🛡 Disclaimer

Use this tool responsibly. Automated form submissions should follow Google’s [Terms of Service](https://policies.google.com/terms) and be used with permission.

---

## 🙋‍♂️ Support

Need help customizing it for dropdowns, checkboxes, or multiple-choice fields? Just ask!
