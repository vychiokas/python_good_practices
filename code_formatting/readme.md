# Code formatting

**Robert C. Martin, that says that code is read ten times more than it's written**

1. Readability: Proper formatting makes code easier to read and understand. When code is well-formatted, it is easier to identify different parts of the code, such as functions, loops, and conditionals. This is especially important when working on larger projects or when collaborating with other developers.

1. Debugging: Proper formatting can make it easier to spot errors in your code. For example, if your code is poorly formatted and a syntax error occurs, it may be harder to locate the error than if the code was properly formatted.

1. Consistency: A consistent code style across your project makes it easier to maintain and modify. If all of the code in a project is formatted consistently, it is easier to identify patterns and make changes across the project as a whole.

1. Community Standards: There are widely accepted standards for formatting Python code, such as PEP 8, which is the official Python style guide. Following these standards makes your code more understandable to other developers who may be working on your project or who may be using your code as a library.

Overall, code formatting is important in Python because it helps to ensure that your code is readable, maintainable, and consistent with community standards.

## Popular code formatters

1. Black: Black is a popular and highly-regarded code formatter for Python. It reformats code in a highly opinionated way to ensure that it is consistent and easy to read. Black is often used in combination with other tools, such as pre-commit, to ensure that code is automatically formatted before it is committed.

1. Prettier: Prettier is a code formatter that supports multiple programming languages, including Python. It is highly configurable and can be used to format code according to a wide range of preferences.

1. autopep8: autopep8 is a Python code formatter that is based on the PEP 8 style guide. It can automatically format code to conform to PEP 8 standards, including indentation, line length, and import order.

1. yapf: yapf is a Python code formatter that focuses on making code more readable and consistent. It can be highly customized and supports a wide range of formatting options.

1. isort: isort is a Python library that can be used to sort and format import statements in a Python codebase. It can automatically group imports by type and optimize the order in which they are listed.

Each of these code formatters has its own strengths and weaknesses, so it's important to choose the one that best fits your needs and preferences.


## Black
Black project github [page](https://github.com/psf/black)  
The following organizations use Black: Facebook, Dropbox, KeepTruckin, Mozilla, Quora, Duolingo, QuantumBlack, Tesla, Archer Aviation.


1. Consistency: Black enforces a strict and consistent code style across your entire codebase, which helps to reduce inconsistencies and makes it easier to read and maintain the code.

1. Automation: Black automates the process of formatting your code, which saves time and ensures that code is always formatted correctly. You don't need to spend time manually formatting your code, which frees up time for other tasks.

1. Opinionated formatting: Black is highly opinionated and takes care of many formatting decisions for you. This means you don't have to spend time deciding on things like line length, indentation, and spacing.

1. Comprehensibility: The highly-formatted code produced by Black is often easier to read and understand, making it easier for others to work with and maintain your code.

1. Integration: Black can be integrated with other tools, such as pre-commit hooks and continuous integration pipelines, to automatically format code as part of your development workflow.

Overall, using Black can help you produce more consistent, readable, and maintainable code with less effort, which can save time and reduce errors in your codebase.


### How to use Black in your projects?  

[black documentation](https://black.readthedocs.io/en/stable/index.html)

1. Install Black: You can install Black using pip, Python's package manager. Open a command prompt and run the following command:  
```bash
pip install black
```

1. Configure Black: By default, Black formats code using its built-in settings. However, you can customize Black's behavior by creating a configuration file. The configuration file should be named pyproject.toml and placed in the root directory of your project.

Here's an example configuration file that specifies a line length of 80 characters:

```toml
[tool.black]
line-length = 80
```
You can customize other settings like indentation level and string quote style as well. Check the Black documentation for more details.

1. Format your code: Once you have installed and configured Black, you can use it to format your Python code. To format a single file, open a command prompt in the directory containing the file and run:

Unix based system:  
```bash
black myfile.py
```  
Windows:  
```bash
python -m black myfile.py
``` 
1. Or simply format entire directory recursivley run:
   
Unix based system:  
```bash
black .
```  
Windows:  
```bash
python -m black .
```


What is more it is also possible to simply check if you code is Black compliant:
```bash
python -m black --check <filename>
```
Or even check what would have been changed:

```bash
python -m black --diff <filename>
```

## pre-commit

There is also a possibility to easily automate this stuff with [pre-commit](https://github.com/pre-commit/pre-commit): [instructions](https://medium.com/gousto-engineering-techbrunch/automate-python-code-formatting-with-black-and-pre-commit-ebc69dcc5e03)


if for some reason you wish to not format a certain line you can add a comment: `#fmt: off/on`
## Additional links:

[automatically use black with Vscode](https://dev.to/adamlombard/how-to-use-the-black-python-code-formatter-in-vscode-3lo0)