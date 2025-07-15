# 📄 Resume Analyzer & Job Match Score

An intelligent Streamlit web app that helps job seekers evaluate how well their resume matches a given job description. It provides a **match score**, **extracted skills**, **missing skills**, and personalized **improvement tips**, along with downloadable reports in both **TXT** and **PDF** formats.

---

## 🚀 Features

- ✅ Upload Resume and Job Description (PDF or TXT)
- 🧠 NLP-based Skill Extraction
- 📊 Cosine Similarity Match Score
- ❌ Highlights Missing Skills
- 💡 Suggests Resume Improvement Tips
- 📥 Download Reports as TXT and PDF

---

## 🧰 Tech Stack

- Python 🐍
- Streamlit 📊
- Scikit-learn 🤖
- NLTK 🧠
- PDFMiner 📝 (for PDF text extraction)
- ReportLab 📄 (for PDF report generation)

---

## 📦 Project Structure

resume_analyzer/
│
├── app.py # Main Streamlit app
├── requirements.txt # All dependencies
├── utils/
│ ├── pdf_reader.py # Extracts text from PDF/TXT
│ ├── text_preprocessor.py # Tokenization & Lemmatization
│ ├── skill_extractor.py # Extracts skills from tokens
│ ├── match_score.py # Computes TF-IDF + Cosine similarity
│ ├── improvement_tips.py # Suggests tips for missing skills
│ ├── report_generator.py # Generates TXT reports
│ └── report_generation.py # Generates PDF reports
└── .venv/ # Virtual environment 


---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Bhanu2900/resume-analyzer.git
cd resume_analyzer
```
### 2.Create virtual Environment
```bash
python -m venv .venv
```

### 3.Activate the Environment
for Windows:
```bash
.venv\Scripts\activate
```

for Linux/macOS:
```bash
source .venv/bin/activate
```

### 4.Install Dependencies
```bash
pip install -r requirements.txt
```

### ▶️ Run the App
```bash
streamlit run app.py
```
The app will open in your browser at:
http://localhost:8501


📝 How It Works
1. Upload your resume and the job description (PDF or TXT).
2. The app:
   • Extracts & preprocesses text  
   • Identifies skills using NLP  
   • Computes a Match Score using TF-IDF + Cosine Similarity  
   • Highlights missing skills  
   • Suggests improvement tips  
   • Allows downloading reports in TXT or PDF

  
   
📄 Sample Report Output

Match Score: 78%

Resume Skills:
- python
- machine learning
- numpy
...

JD Required Skills:
- python
- deep learning
- sql
...

Missing Skills:
- sql
- deep learning

Suggested Improvements:
- Consider adding "SQL" to your resume.
- Include experience or projects related to "Deep Learning".


🤝 Contributing
Pull requests are welcome. Feel free to open issues or suggest features!


📜 License
This project is open source and available under the MIT License.


🔗 Author
Made with ❤️ by [Bhanu Pratap](https://github.com/Bhanu2900)
