# 🎓 EPIC Certificate & Badge Automation

This project automates the creation of personalized **badges (PNG)** and **certificates (PDF)** for the EPIC Executive Education Program.

Instead of manually editing templates for every participant, the script reads an Excel spreadsheet and generates all documents automatically in just a few seconds.

---

## 🚀 Features

- Reads participant data from an Excel spreadsheet
- Generates personalized badges (.png)
- Generates personalized certificates (.pdf)
- Preserves the original templates
- Supports any number of participants

---

## 🛠 Tech Stack

- Python
- Pandas
- Pillow (PIL)
- Excel

---

## 📂 Project Structure

```text
.
├── Participants_spreadsheet/
├── Template_badge/
├── Template_certificate/
├── Text_Fonts/
├── Epic_Badges/
├── Epic_Certificates/
└── script.py
```

---

## ▶️ How to Run

Install the dependencies:

```bash
pip install pandas pillow openpyxl
```

Run the script:

```bash
python script.py
```

Generated files will be saved automatically in:

- `Epic_Badges/`
- `Epic_Certificates/`

---

## 🖼 Preview

### Badge

<p align="center">
  <img src="Pictures\Prints_Automation\Badge_Otávio_Cunha.png" width="350">
</p>

### Certificate

<p align="center">
  <img src="Pictures\Prints_Automation\Certificate_Otávio_Cunha.pdf" width="750">
</p>

---

## 👨‍💻 Author

Developed by **Breno Vieira** as part of the **EPIC Automation Technical Challenge**.