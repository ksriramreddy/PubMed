# PubMed CLI Fetcher

## 📌 Project Overview
This is a command-line tool that allows users to search for research papers from PubMed using the NCBI API. The tool fetches article metadata, including titles, publication dates, and affiliations, and saves the results to a CSV file.

---

## 📂 Code Organization
The project is structured as follows:
```
/PubMedAPI  # Root project folder
│── pubmedapi/  # Main package directory
│   ├── __init__.py  # Marks it as a package
│   ├── main.py  # CLI entry point
│   ├── fetcher.py  # Functions for API requests and CSV saving
│── pyproject.toml  # Poetry configuration
│── README.md  # Project documentation
```
- **main.py** → Handles command-line arguments and runs the tool.
- **fetcher.py** → Fetches data from PubMed and saves results to CSV.
- **pyproject.toml** → Defines dependencies and CLI script for Poetry.
- **README.md** → Documentation for installation and usage.

---

## 🛠️ Installation
### **1️⃣ Install Poetry (if not already installed)**
```sh
pip install poetry
```

### **2️⃣ Clone the Repository and Navigate to the Project**
```sh
git clone <repository-url>
cd PubMedAPI
```

### **3️⃣ Install Dependencies**
```sh
poetry install
```

---

## 🚀 Usage
### **Run the CLI Script**
To fetch research papers and print results:
```sh
poetry run get-papers-list "machine learning"
```

### **Save Output to CSV**
```sh
poetry run get-papers-list "cancer treatment" -f results.csv
```

### **Enable Debug Mode**
```sh
poetry run get-papers-list "covid-19 vaccine" -d
```

---

## 🔍 Example Output
```sh
🔗 Found 5 papers... Fetching details...
✅ Results saved to results.csv
```
The output will be saved in a CSV file with the following format:
| PubMed ID | Title | Publication Date | Non-academic Author(s) | Company Affiliation(s) | Corresponding Author Email |
|-----------|--------------------------------------|-----------------|-----------------------|------------------|---------------------------|
| 37282621  | Advances in Cancer Immunotherapy    | 2023 Mar        | Dr. Smith, Dr. Jones | BioPharma Inc.   | smith@biopharma.com      |

---

## 🔧 Troubleshooting
1. **Module Import Errors?**
   - Ensure the project structure is correct.
   - Run `poetry install` to reinstall dependencies.

2. **Command Not Found?**
   - Run `poetry shell` and then execute the script.

---


