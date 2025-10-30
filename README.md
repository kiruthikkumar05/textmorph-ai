# 🧠 TextMorph AI — Text Summarizer, Paraphraser & Sentiment Analyzer

An advanced **Flask-based NLP application** that performs **Text Summarization**, **Paraphrasing**, and **Sentiment Analysis** using transformer models from Hugging Face.
Built with modular architecture, YAML configuration management, and a clean responsive interface.

---

## 🚀 Features

* ✨ **Abstractive Summarization** – Generates concise, meaningful summaries
* 🔄 **Paraphrasing** – Rewrites sentences with alternate phrasing
* 💬 **Sentiment Analysis** – Classifies text emotion as Positive, Negative, or Neutral
* ⚙️ **Config-Driven Setup** – All model settings handled in `config.yaml`
* 💾 **Download Output (Upcoming)** – Save results for future use
* 🎨 **Modern Flask UI** – Simple HTML + CSS front-end

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/kiruthikkumar05/textmorph-ai.git
cd textmorph-ai
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate    # For Windows
# or
source .venv/bin/activate # For macOS/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration Setup

### 🗂️ 1. Environment File

Create a file named `.env` in your project root (same level as `app.py`)
and add your Hugging Face API Key (optional for custom models):

```
HF_API_KEY=your_huggingface_api_key
```

### ⚙️ 2. YAML Configuration

You can define model and task parameters in `config.yaml`:

```yaml
summarization:
  model: "facebook/bart-large-cnn"
  max_length: 120
  min_length: 30

paraphrasing:
  model: "Vamsi/T5_Paraphrase_Paws"
  max_length: 150

sentiment:
  model: "distilbert-base-uncased-finetuned-sst-2-english"
```

This allows easy customization of models without editing code.

---

## ▶️ Run the Application

```bash
python app.py
```

Then open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## 💡 How to Use

1. Launch the app in your browser.
2. Enter or paste your text into the input box.
3. Select one of the actions:

   * 🧩 **Summarize**
   * ✍️ **Paraphrase**
   * 💬 **Sentiment Analysis**
4. Click **Process** and view the generated output instantly.

---

## ⚡ Technologies Used

* 🧠 **Hugging Face Transformers** – BART, T5, and DistilBERT models
* ⚙️ **Flask** – Backend framework for web integration
* 🔥 **PyTorch** – Deep learning engine for model inference
* 📜 **YAML** – Configuration management
* 🎨 **HTML & CSS** – Frontend styling and layout
* 🧰 **python-dotenv** – Secure environment variable loading

---

## 🧩 Folder Structure

```
Textmorph-AI/
├── app.py
├── config.yaml
├── config_manager.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── mvp/
    ├── text_summarizer.py
    ├── text_paraphraser.py
    └── text_sentiment.py
```

---

## 👨‍💻 Author

* **Kiruthik Kumar J**
* 📧 `jkdec2004@gmail.com`
* 🌐 [GitHub Profile](https://github.com/kiruthikkumar05)

---