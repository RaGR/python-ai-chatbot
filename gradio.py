###########################################
#                                         #
#           GRADIO - WEB APP              #
#                                         #
###########################################

import openai
import gradio
openai.api_key = "env_openai_apikey001"
prompt = "How can i help you?"

def api_calling(prompt):
    completions = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=prompt
    )
    message = completions.choices[0].text
    return message
    
def message_and_history(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = api_calling(inp)
    history.append((input, output))
    return history, history
block = gradio.Blocks(theme=gradio.themes.Monochrome())
with block:
    gradio.Markdown("""<h1><center>ChatGPT  
    ChatBot with Gradio and OpenAI</center></h1> 
    """)
    chatbot = gradio.Chatbot()
    message = gradio.Textbox(placeholder=prompt)
    state = gradio.State()
    submit = gradio.Button("SEND")
    submit.click(message_and_history,
                 inputs=[message, state],
                 outputs=[chatbot, state])
block.launch(debug = True)
