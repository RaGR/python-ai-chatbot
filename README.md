# 🧠 ChatGPT AI Assistant — Python Chatbot with Gradio & Console Interface

A simple yet powerful **AI Chatbot** built in **Python** using the **OpenAI API**, offering both **console (terminal)** and **web-based (Gradio)** interfaces.
This project demonstrates end-to-end integration of **large language models (LLMs)** into user applications for text-based interaction.

---

## 📁 Project Structure

```
├── console.py               # Terminal-based chatbot using OpenAI API
├── gradio.py                # Web interface chatbot using Gradio
├── fleet.py                 # (Optional) Multi-interface or extended bot management
├── Project proposal - 2023.pdf  # Original academic project documentation
```

---

## 🚀 Features

* 💬 Real-time chatbot interaction in terminal (console.py)
* 🌐 Web-based interactive chatbot UI with Gradio (gradio.py)
* ⚙️ Simple integration with OpenAI’s GPT models (GPT-3.5-Turbo)
* 🧩 Extendable architecture — can integrate multiple interfaces (e.g., Flet, Flask, Docker)
* 📚 Educational base for LLM app development

---

## 🧰 Libraries and Dependencies

Make sure you have **Python 3.8+** installed, then install the following libraries:

```bash
pip install openai gradio
```

If you plan to extend the project:

```bash
pip install torch transformers flet flask
```

### Core Libraries Used

| Library        | Purpose                                                         |
| -------------- | --------------------------------------------------------------- |
| `openai`       | Connects to the OpenAI GPT API for natural language interaction |
| `gradio`       | Builds simple web interfaces for ML and AI applications         |
| `torch`        | (Optional) Backend for local model integration                  |
| `transformers` | (Optional) Use open-source LLMs (e.g., Falcon, LLaMA, GPT-2)    |
| `flet`         | (Optional) Build desktop or browser-based UI                    |
| `flask`        | (Optional) API server or containerized deployment               |

---

## ⚙️ Setup & Configuration

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/chatgpt-ai-assistant.git
   cd chatgpt-ai-assistant
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   (Or manually install `openai` and `gradio` as above.)

3. **Set your OpenAI API key:**
   Replace the placeholder key in both scripts:

   ```python
   openai.api_key = "YOUR_OPENAI_API_KEY"
   ```

   or export it as an environment variable:

   ```bash
   export OPENAI_API_KEY="your_api_key_here"
   ```

---

## 💻 Usage

### 🧩 Console Version

Run the chatbot directly in your terminal:

```bash
python console.py
```

**Example:**

```
User: What is artificial intelligence?
ChatGPT: Artificial intelligence is the simulation of human intelligence processes by machines...
```

---

### 🌐 Gradio Web Interface

Launch the chatbot in a browser-based UI:

```bash
python gradio.py
```

Then open the **local URL** shown in the terminal (usually `http://127.0.0.1:7860/`).

---

## 🧠 How It Works

1. The user’s input is collected (via console or Gradio UI).
2. The message is sent to OpenAI’s `chat.completions.create()` endpoint.
3. The GPT model (`gpt-3.5-turbo`) processes and returns the response.
4. The reply is displayed back to the user in real time.

This simple flow allows developers to easily embed conversational AI into any Python app.

---

## 🏗️ Future Extensions

* Integrate open-source models (Falcon, Vicuna, LLaMA) via HuggingFace.
* Add **memory** and **context management**.
* Deploy with **Flask** or **FastAPI** as a REST API service.
* Wrap as a **desktop app** using **Flet**.
* Containerize with **Docker** for easy deployment.

---

## 🧩 Example Code Snippet (Console Version)

```python
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"
messages = [{"role": "system", "content": "You are a helpful assistant."}]

while True:
    message = input("User: ")
    if message:
        messages.append({"role": "user", "content": message})
        chat = openai.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message.content
        print(f"ChatGPT: {reply}")
        messages.append({"role": "assistant", "content": reply})
```

---

## 📖 References

* [OpenAI API Documentation](https://platform.openai.com/docs/api-reference)
* [Gradio Documentation](https://www.gradio.app/docs/)
* [Hugging Face Transformers](https://huggingface.co/transformers/)
* [Flet Framework](https://flet.dev/)
