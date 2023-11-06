improve_code_template = """
I don't think this code is the best, can you help me?

{question}

Please change the code and explain in detail, what you did to improve it. This is very important for my career.
"""

rewrite_code_template = """
I don't think this code is the best way to do it in Python, can you help me?

{question}

Please explore multiple ways of solving the problem, give examples, and explain each. This is very important for my career.
"""

pythonic_recommend_template = """
I don't think this code is the best way to do it in Python, can you help me?

{question}

Please explore multiple ways of solving the problem, 
and tell me which is the  most Pythonic, and change the code accordingly. This is very important for my career.
"""

simplify_code_template = """
Can you please simplify this in Python? You are an expert in Pythonic code.

{question}

Please comment each line in detail, and explain in detail what you did to modify it, and why. This is very important for my career.
"""

runnable_script_template = """
Can you please turn this script into a runnable program from the command line?? \n
I want to pass in the question as a command line argument, \n
and get the answer back as a result. \n
Also write the full bash command for the script. \n
You are an expert in Pythonic code.

{question}

Please comment each line in detail, \n
and explain in detail what you did to modify it, and why. This is very important for my career.
"""

explain_code_template = """
Can you please explain how this code works?

{question}

Use a lot of detail and make it as clear as possible. This is very important for my career.
"""

document_code_template = """
Please write technical documentation for this code and \n
make it easy for a non developer to understand:

{question}

Output the results in markdown. This is very important for my career.
"""

docstring_code_template = """
Please write a docstring, that has a line length of maximum 80 characters, for this code and add variables coded as sphinx variables:

{question}

 This is very important for my career.
"""

test_code_template = """
Can you please create test cases in code for this Python code?

{question}

Explain in detail what these test cases are designed to achieve. This is very important for my career.
"""

debug_code_template = """
Can you please help me to debug this code?

{question}

Explain in detail what you found and why it was a bug. This is very important for my career.
"""

efficient_code_template = """
Can you please make this code more efficient?

{question}

Explain in detail what you did to make it more efficient. This is very important for my career.
"""

readme_creation_template = """
Can you please write a README.MD file based on the following code?

{question}

 This is very important for my career.
"""