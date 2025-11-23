⭐ README.md (Copy the entire content below)
# LLM Benchmarking Suite  
A Comparative Benchmark of GPT-4.1, Claude 3.5 Sonnet and Llama 3.1 (Groq)

This repository contains the complete code, experiments, and documentation used to benchmark  
three modern Large Language Models (LLMs):

- **OpenAI GPT-4.1**
- **Anthropic Claude 3.5 Sonnet**
- **Meta Llama 3.1 (Groq Inference Engine)**

This benchmark measures:

- ✔ Speed (latency + tokens/sec)  
- ✔ Coding ability  
- ✔ Mathematical reasoning  
- ✔ Instruction following  
- ✔ Overall accuracy and behavior  

The benchmark follows the same style as DuckDB’s *Benchmarks Over Time* article —  
transparent, reproducible, and data-driven.

---

## 📁 Repository Structure



ml-llm-benchmark/
│
├── ARTICLE.md # Final technical article (the main deliverable)
├── README.md # Reproduction guide
│
├── benchmarks/
│ └── run_benchmarks.py # Python script for all experiments
│
└── results/
└── sample_outputs/ # API responses (optional)


---

## 🚀 How to Run the Benchmarks

### 1️⃣ **Install Python Requirements**

Create a virtual environment:



python -m venv venv


Activate it:

- On Windows:


venv\Scripts\activate


Install dependencies:



pip install openai anthropic groq python-dotenv


---

### 2️⃣ **Set Your API Keys**

Create a new file in the root folder:



.env


Add your keys:



OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
GROQ_API_KEY=your_key_here


---

### 3️⃣ **Run Benchmarks**

Run:



python benchmarks/run_benchmarks.py


This will execute:

- Speed test  
- Coding test  
- Reasoning test  
- Instruction following test  

And print all results clearly in your terminal.

---

## 📊 What This Benchmark Measures

### ✔ **Latency**
Time from request → first token returned.

### ✔ **Tokens per second (TPS)**
How fast each model streams output.

### ✔ **Coding Quality**
A Fibonacci + test-case generation task.

### ✔ **Mathematical Reasoning**
Probability, algebra, logic questions.

### ✔ **Instruction Following**
Complex constraints with multiple rules.

---

## 📝 Reproducibility

All benchmarks use:

- Temperature = `0.2`
- Max tokens = `512`
- Same prompts across models
- 3 repeated runs per test
- Averaged results

This ensures fairness and stable comparisons.

---

## 📚 Full Article

See the full report here:

👉 **`ARTICLE.md`**

This file contains:
- Complete explanations  
- Tables  
- Model comparisons  
- Experimental insights  
- Final conclusions  

---

## 🏁 Final Notes

This project was completed as part of the  
**ML/AI Intern Technical Assignment** at Process Point Technologies.

For any questions, feel free to reach out!
