def create_template(function_name, docstring, parameters):
    params = ', '.join(parameters)
    with open('file.py','w') as tp:
        tp.write(f"def {function_name}({params}):\n    \"\"\"{docstring}\"\"\"\n    return None\n")

create_template('',"",["",""])