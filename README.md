# Universal Credit Act 2025 – AI Analysis Project 

This project was created for the **NIYAMR AI 48-Hour Internship Assignment**. The goal was to take the *Universal Credit Act 2025* PDF, read it, summarise it, and convert it into clean JSON outputs.

Everything in this project is kept simple and clear so anyone can understand what is happening.

---

## ✅ What This Project Does 

* It reads the **Universal Credit Act 2025** PDF.
* It extracts all the text from the PDF.
* It cleans the text and saves it in a normal readable form.
* It creates a short 5–10 point summary of the Act.
* It converts important parts of the Act into JSON.
* It checks 6 rules and tells which pass and which fail.

These were the 4 tasks given in the assignment, and all 4 are completed.

---

## 📂 Project Folder Structure

```
universal-credit-act-ai-agent/
│
├── data/
│   └── ukpga_20250022_en.pdf     (The Act PDF)
│
├── src/
│   └── extract_text.py           (Script that extracts text)
│
├── output/
│   ├── uc_act_2025_raw.txt       (Raw text from PDF)
│   ├── uc_act_2025_clean.txt     (Clean text)
│   ├── summary.md                (5–10 point summary)
│   ├── uc_act_report.json        (Structured JSON)
│   └── rule_checks.json          (Rule check results)
│
├── requirements.txt              (Python dependencies)
└── README.md                     (This document)
```

---

## 🧠 Task Overview (Explained Simply)

### **1) Task 1 – Extract Text**

* A Python script reads the PDF.
* It converts every page into text.
* It saves two files:

  * Raw text
  * Clean text

### **2) Task 2 – Summary**

A short 5–10 bullet summary explaining:

* Purpose
* Definitions
* Eligibility
* Obligations
* Key points

### **3) Task 3 – JSON Output**

A JSON file that contains:

* Definitions
* Obligations
* Responsibilities
* Eligibility rules
* Payments
* Penalties (if any)
* Record keeping

### **4) Task 4 – Rule Checks**

Checks 6 rules and marks each one as:

* Pass
* Fail
* Partial

Each rule also has:

* Evidence
* Confidence score

---

## ▶️ How To Run the Extraction Script

If someone wants to run it themselves:

```
pip install -r requirements.txt
python -m src.extract_text
```

This will recreate the **raw** and **clean** text files.

---

## 🎯 What You Submit for the Internship

You need to submit:

### ✔ 1. The GitHub repo link

### ✔ 2. The 2 JSON files (Task 3 + Task 4)

### ✔ 3. A 2-minute explanation video

Everything else is already prepared inside the `output/` folder.

---

## 🎥 Short Video Script (Easy to Read)

**Hi, I’m Dhruv. This is my submission for the NIYAMR AI internship assignment.**

I created a small pipeline that reads the Universal Credit Act 2025 PDF, extracts its text, cleans it, summarises it, and converts the important parts into JSON.

First, I placed the PDF in the `data` folder.
Then I ran my script `extract_text.py` which generated the raw and clean text files in the `output` folder.

Next, I created a 5–10 point summary of the Act.
After that, I generated a structured JSON file that contains definitions, eligibility rules, obligations, payments, penalties and record-keeping.

Finally, I completed the 6 required rule checks and stored them in another JSON file.

This project shows how an AI agent can read a legal document and produce structured, useful output.

Thank you.

---

## 👤 Author

**Dhruv Kumar** – Aspiring Data Scientist

Thank you for reviewing this assignment!
