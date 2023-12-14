import gradio as gr
import os
import openai
from dotenv import load_dotenv, find_dotenv
from prompts import *
from utils import *

_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = os.environ["OPENAI_API_KEY"]

"""
Get inspired here for
https://github.com/project-baize/baize-chatbot/blob/main/demo/app_modules/utils.py
"""


# Define a custom CSS style for the HTML output
custom_css = """
.custom-html-output {
    height: 30em;  # Adjust the height to resemble 30 lines
    overflow-y: scroll;  # Add scroll for overflow content
    background-color: #f5f5f5;  # Background color similar to a textbox
    border: 1px solid #ccc;  # Border similar to a textbox
    padding: 10px;  # Padding inside the box
    font-family: monospace;  # Monospace font for code-like appearance
}
"""


def improve_text(switch, existing_text):
    if switch == "Improve":
        new_text = improve_code_template.format(question=existing_text)
    elif switch == "Rewrite":
        new_text = rewrite_code_template.format(question=existing_text)
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
    elif switch == "Docstring":
        new_text = docstring_code_template.format(question=existing_text)
    elif switch == "Test":
        new_text = test_code_template.format(question=existing_text)
    elif switch == "Debug":
        new_text = debug_code_template.format(question=existing_text)
    elif switch == "Optimize":
        new_text = efficient_code_template.format(question=existing_text)
    elif switch == "Readme":
        new_text = readme_creation_template.format(question=existing_text)
    elif switch == "Pydantic":
        new_text = pydantic_conversion_template.format(question=existing_text)
    elif switch == "Clear":
        new_text = ""
    else:
        new_text = existing_text

    prompt.update(new_text)
    return new_text


def reset_textbox():
    return gr.update(value=""), ""


class State:
    interrupted = False

    def interrupt(self):
        self.interrupted = True

    def recover(self):
        self.interrupted = False


shared_state = State()


def cancel_outputing():
    shared_state.interrupt()
    textbox = reset_textbox()
    return "Stop Done"


with gr.Blocks(css=custom_css) as demo:

    def get_completion(text, model="gpt-4-0613"):
        """
        First it creates an OpenAI Chat completion with necessary parameters
        To enable streaming, we add parameter stream=True
        As we’re using stream=True, the chat completion returns a generator object instead of an AI response.
        Rather than getting the complete response all at once, we could use the generator object to get the response in
        a token-by-token manner on-the-fly.
        Hence, the user don’t have to wait for the entire response to be received, but can see the response get
        populated
        incrementally token-by-token.
        """

        messages = [{"role": "user", "content": text}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0,
            stream=True,
        )
        partial_response = ""
        for stream_response in response:
            token = stream_response["choices"][0]["delta"].get("content", "")
            partial_response += token
            yield markdown_to_html_with_syntax_highlight(partial_response)

    gr.Markdown("## Pair Programmer")
    status_display = gr.Markdown("Success", elem_id="status_display")
    prompt = gr.Textbox(lines=15, label="Input Text", placeholder="Please write some code here")
    with gr.Row():
        improve = gr.Radio(
            choices=[
                "Improve",
                "Rewrite",
                "Pythonic",
                "Pydantic",
                "Simplify",
                "Runnable",
                "Explain",
                "Document",
                "Docstring",
                "Test",
                "Debug",
                "Optimize",
                "Readme",
                "Clear",
            ],
            label="Action",
        )

        submit_button = gr.Button("Submit")
        cancel_button = gr.Button("Stop")

    improve.change(fn=improve_text, inputs=[improve, prompt], outputs=[prompt])
    submit_button.click(
        fn=get_completion,
        inputs=[prompt],
        outputs=gr.HTML(
            lines=30,
            label="Output Text",
            show_copy_button=True,
        ),
    )
    cancel_button.click(cancel_outputing, [], [status_display])


gr.close_all()
# To allow streaming, enable the queue().
demo.queue()
demo.launch(
    share=False,
    server_port=int(os.environ.get("PORT", 7862)),
)
