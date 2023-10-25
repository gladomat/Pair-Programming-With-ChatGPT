improve_code_template = """
I don't think this code is the best, can you help me?

{question}

Please explain in detail, what you did to improve it.
"""

rewrite_code_template = """
I don't think this code is the best way to do it in Python, can you help me?

{question}

Please explore multiple ways of solving the problem, and explain each.
"""

pythonic_recommend_template = """
I don't think this code is the best way to do it in Python, can you help me?

{question}

Please explore multiple ways of solving the problem, 
and tell me which is the  most Pythonic.
"""

simplify_code_template = """
Can you please simplify this in Python? You are an expert in Pythonic code.

{question}

Please comment each line in detail, and explain in detail what you did to modify it, and why.
"""

runnable_script_template = """
Can you please turn this script into a runnable program from the command line?? \n
I want to pass in the question as a command line argument, \n
and get the answer back as a result. \n
Also write the full bash command for the script. \n
You are an expert in Pythonic code.

{question}

Please comment each line in detail, \n
and explain in detail what you did to modify it, and why.
"""

explain_code_template = """
Can you please explain how this code works?

{question}

Use a lot of detail and make it as clear as possible.
"""

document_code_template = """
Please write technical documentation for this code and \n
make it easy for a non developer to understand:

{question}

Output the results in markdown.
"""

docstring_code_template = """
Please write a docstring for this code and \n
add variables coded as sphinx variables:

{question}
"""

test_code_template = """
Can you please create test cases in code for this Python code?

{question}

Explain in detail what these test cases are designed to achieve.
"""

debug_code_template = """
Can you please help me to debug this code?

{question}

Explain in detail what you found and why it was a bug.
"""

efficient_code_template = """
Can you please make this code more efficient?

{question}

Explain in detail what you did to make it more efficient.
"""

readme_creation_template = """
Can you please write a README.MD file based on the following code?

{question}
"""