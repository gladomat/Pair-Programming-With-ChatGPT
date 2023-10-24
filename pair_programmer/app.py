import gradio as gr
import os
import openai
from dotenv import load_dotenv, find_dotenv
from prompts import *

_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = os.environ["OPENAI_API_KEY"]


def improve_text(switch, existing_text):
    if switch == "Improve":
        new_text = improve_code_template.format(question=existing_text)
    elif switch == "Rewrite":
        new_text = rewrite_code_template.format(question=existing_text)
        print("rewrite", new_text)
    elif switch == "Pythonic":
        new_text = pythonic_recommend_template.format(question=existing_text)
    elif switch == "Simplify":
        new_text = simplify_code_template.format(question=existing_text)
    elif switch == "Runnable":
        new_text = runnable_script_template.format(question=existing_text)
    elif switch == "Explain":
        new_text = explain_code_template.format(question=existing_text)
    elif switch == "Document":
        new_text = document_code_template.format(question=existing_text)
    elif switch == "Test":
        new_text = test_code_template.format(question=existing_text)
    elif switch == "Debug":
        new_text = debug_code_template.format(question=existing_text)
    elif switch == "Optimize":
        new_text = efficient_code_template.format(question=existing_text)
    elif switch == "Readme":
        new_text = readme_creation_template.format(question=existing_text)
    else:
        new_text = existing_text

    prompt.update(new_text)
    return new_text


with gr.Blocks() as demo:

    def get_completion(text, model="gpt-4-0613"):
        messages = [{"role": "user", "content": text}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0,
        )
        return response.choices[0].message["content"]

    def completioner(inputs):
        return get_completion(inputs)

    gr.Markdown("## Pair Programmer")
    prompt = gr.Textbox(lines=15, label="Input Text", placeholder="Please write some code here")
    with gr.Row():
        improve = gr.Radio(
            choices=[
                "Improve",
                "Rewrite",
                "Pythonic",
                "Simplify",
                "Runnable",
                "Explain",
                "Document",
                "Test",
                "Debug",
                "Optimize",
                "Readme",
            ],
            label="Action",
        )

        submit_button = gr.Button("Submit")

    improve.change(fn=improve_text, inputs=[improve, prompt], outputs=[prompt])
    submit_button.click(fn=completioner, inputs=[prompt], outputs=gr.Textbox(lines=15, label="Output Text"))

gr.close_all()
demo.launch(share=False, server_port=int(os.environ.get("PORT", 7860)))
