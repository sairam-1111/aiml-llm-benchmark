import os
import time
import requests
from groq import Groq
from openai import OpenAI
from dotenv import load_dotenv

# ---------------------------
# Load environment variables from .env
# ---------------------------
load_dotenv()  # Automatically loads .env file in the same directory

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize clients using environment variables
client_groq = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None
client_openai = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None

# ---------------------------
# Measure execution time helper
# ---------------------------
def measure_time(fn):
    start = time.time()
    output = fn()
    end = time.time()
    return output, round(end - start, 3)

# ---------------------------
# DeepSeek API call
# ---------------------------
def call_deepseek(prompt):
    if not DEEPSEEK_API_KEY:
        return "DeepSeek API Key not set"

    url = "https://api.deepseek.com/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
    }
    data = {
        "model": "deepseek-reasoner",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response_json = response.json()
        if "choices" in response_json:
            return response_json["choices"][0]["message"]["content"]
        else:
            return f"DeepSeek API Error: {response_json}"
    except Exception as e:
        return f"DeepSeek API Exception: {str(e)}"

# ---------------------------
# Groq API call
# ---------------------------
def call_groq(prompt):
    if not client_groq:
        return "Groq API Key not set"

    try:
        response = client_groq.chat.completions.create(
            model="your-accessible-model",  # Replace with a valid Groq model
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Groq API Error: {str(e)}"

# ---------------------------
# OpenAI GPT call
# ---------------------------
def call_openai(prompt):
    if not client_openai:
        return "OpenAI API Key not set"

    try:
        response = client_openai.chat.completions.create(
            model="gpt-4o-mini",  # or any other OpenAI model you have access to
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"OpenAI API Error: {str(e)}"

# ---------------------------
# Tasks to benchmark
# ---------------------------
tasks = {
    "math_reasoning": "Solve: A car travels 60 km/h for 2 hours. How far does it go?",
    "coding": "Write a Python function to reverse a string.",
    "chat": "Explain AI in simple words."
}

# ---------------------------
# Run all benchmarks
# ---------------------------
def run_all():
    results = {}
    for task_name, prompt in tasks.items():
        print(f"\nRunning task: {task_name}")

        output_ds, latency_ds = measure_time(lambda: call_deepseek(prompt))
        output_groq, latency_groq = measure_time(lambda: call_groq(prompt))
        output_oa, latency_oa = measure_time(lambda: call_openai(prompt))

        results[task_name] = {
            "deepseek_output": output_ds,
            "deepseek_latency": latency_ds,
            "groq_output": output_groq,
            "groq_latency": latency_groq,
            "openai_output": output_oa,
            "openai_latency": latency_oa
        }
    return results

# ---------------------------
# Main
# ---------------------------
if __name__ == "__main__":
    print("\n▶ Starting benchmarks: DeepSeek + Groq + OpenAI GPT\n")
    results = run_all()

    print("\n==================== RESULTS ====================\n")
    for task, res in results.items():
        print(f"\nTask: {task}")
        print(f"DeepSeek Output: {res['deepseek_output']}")
        print(f"DeepSeek Latency: {res['deepseek_latency']}s")
        print(f"Groq Output:     {res['groq_output']}")
        print(f"Groq Latency:     {res['groq_latency']}s")
        print(f"OpenAI Output:   {res['openai_output']}")
        print(f"OpenAI Latency:   {res['openai_latency']}s")
    print("\n=================================================\n")
