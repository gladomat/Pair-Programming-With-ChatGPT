# Pair Programming with ChatGPT

This repository contains a Python notebook that demonstrates how to use the OpenAI API, particularly the ChatGPT model, as a pair-programming partner. The notebook provides various templates to interact with ChatGPT for different programming tasks such as improving existing code, exploring multiple ways to rewrite code, simplifying code, writing test cases, making code more efficient, and debugging.

## Prerequisites

- You need an API key from OpenAI. Store it in a `.env` file in the format:

```
OPENAI_API_KEY=sk-...
```

## Dependencies

- `openai`: For interacting with the OpenAI API.
- `tiktoken`: To count how many tokens are in a text string without making an API call.
- `dotenv`: To load environment variables from a `.env` file.
- `IPython`: For displaying Markdown and other rich output formats in Jupyter.

## How to Use

1. Clone the repository.
2. Install the required dependencies.
3. Add your OpenAI API key to the `.env` file.
4. Run the code:
    
    ```bash
   python pair_programmer/app.py
    ```

## Templates Provided

1. **Improve Existing Code**: Provide a code snippet and get suggestions on how to improve it.
2. **Ask for Multiple Ways of Rewriting Your Code**: Provide a code snippet and get multiple ways to achieve the same functionality.
3. **Recommend the Most Pythonic Way**: Provide a code snippet and get the most Pythonic way to write it.
4. **Simplify Code**: Provide a complex code snippet and get a simplified version of it.
5. **Write Test Cases**: Provide a code snippet and get test cases for it.
6. **Make Code More Efficient**: Provide a code snippet and get a more efficient version of it.
7. **Debug Code**: Provide a buggy code snippet and get debugging help.
8. **Explain Code**: Provide a code snippet and get a detailed explanation of how it works.
9. **Document Code**: Provide a code snippet and get documentation for it.
10. **Write Docstrings**: Provide a code snippet and get docstrings for the functions or classes.
11. **Optimize Code**: Provide a code snippet and get an optimized version of it.
12. **Create Readme**: Write a `Readme.md` file based on the pasted code.


## Note

The notebook uses the `gpt-4-0613` model from OpenAI for completions. You can change the model by modifying the `model` parameter in the `get_completion` function.
