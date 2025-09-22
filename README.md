# 🏥 Hospital Finder AI App

A simple **Streamlit + LangChain** application that uses **OpenAI LLMs** to suggest the best hospital in an Indian city and list its top doctors.

---

## ✨ Features
- Pick a city from the sidebar dropdown.
- Get a short introduction about healthcare facilities in that city.
- Discover the top hospital in the city.
- View details about the hospital and top 3 doctors with their degrees and specialisations.

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/sampathvadrevu/hospital-ai-app.git
cd hospital-ai-app
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set your OpenAI API key
⚠️ **Do not paste your key into code or README.**  
Instead, set it as an environment variable on your system.

**Linux / macOS**
```bash
export OPENAI_API_KEY="your_api_key_here"
```

**Windows (PowerShell)**
```bash
setx OPENAI_API_KEY "your_api_key_here"
```

### 5. Run the app
```bash
streamlit run main.py
```

---

## 📂 Project Structure
```
hospital-ai-app/
│── main.py            # Streamlit app
│── requirements.txt   # Dependencies
│── README.md          # Project description
```

---

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 📒 Learning Notebook
This repo also includes a Jupyter Notebook (`notebooks/langchain_basics.ipynb`)  
where I explored LangChain concepts step by step before building the Streamlit app.

---

## 📜 License
This project is open source and available under the MIT License.
