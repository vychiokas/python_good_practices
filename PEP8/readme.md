# PEP8

## What is PEP8
PEP 8 is a set of guidelines for writing Python code that aims to improve the readability and maintainability of your code. Following PEP 8 can make your code more consistent and easier to understand for yourself and others who may need to read or modify it in the future.


As any programming language has naming standards and standards for the ways it does certain things - Python is not an exception. With the naming standards we communicate better with other developers on what certain things must be and what they should not. It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. The primary focus of PEP 8 is to improve the readability and consistency of Python code.

PEP stands for Python Enhancement Proposal, and there are several of them. A PEP is a document that describes new features proposed for Python and documents aspects of Python, like design and style, for the community.


## Why is PEP8 Important  
Simply as the [Zen of Python](https://peps.python.org/pep-0020/#the-zen-of-python) states: Readability counts. There are many benefits of standardizing the way people write code:
1. Readability: Code that follows PEP 8 guidelines is easier to read and understand, which makes it easier to maintain and modify in the future.

1. Consistency: Following PEP 8 helps to ensure that your code is consistent with other Python code that follows the same guidelines, making it easier for others to understand and collaborate with.

1. Compatibility: Code that follows PEP 8 guidelines is more likely to be compatible with various tools and libraries that are designed to work with Python code.

1. Best practices: PEP 8 guidelines are based on best practices for writing Python code, which means following them can help you write better, more efficient code.
These all sound like synonyms and of course they are, but let's see a few examples where the naming standards .

**NOTE** :

Never 🛑  use l, O single letter names as they might be mistakes for 1 and 0:
```python
O = 2  # This may look like you're trying to reassign 2 to zero
```

## Naming conventions

It is never too much of revisiting naming conventions as it really separates a good python programmer from great one. You might understand how language works but if you do not follow the naming conventions, nobody will understand you code to full extent.


| Attempt | #1    | #2    |
| :---   | :--- | :--- |
| Function| Use a lowercase word or words. Separate words by underscores to improve readability.| function, my_function|
| Variable| Use a lowercase single letter, word, or words. Separate words with underscores to improve readability.| variable, my_variable   |
| Class| Start each word with a capital letter. Do not separate words with underscores. This style is called camel case or pascal case.   | Model, MyClass|
| Method| Use a lowercase word or words. Separate words with underscores to improve readability. | class_method, method  |
| Constant| Use an uppercase single letter, word, or words. Separate words with underscores to improve readability.  | CONSTANT, MY_CONSTANT, MY_LONG_CONSTANT |
| Module | Use a short, lowercase word or words. Separate words with underscores to improve readability.  | module.py, my_module.py|
| Package| Use a short, lowercase word or words. Do not separate words with underscores.  | package, mypackage  |


Let's look at example. What is the purpose of this code?  
```python
def get_them(self):
    a_list = []
    for x in self.the_list:
        if x[0] == 4:
            a_list.append(x)
    return a_list
```


It's a pretty simple method but taken apart from the rest of the class; it doesn't speak by itself. This code is too implicit. Can you name the things that are not right here?  
Some of them are: namings, types, magic constants etc.

Now, let's do some simple refactoring.  

```python
def get_pending_pull_requests(self):
    pending_pull_requests = []
    for pull_request in self.embarked_pull_requests:
        if pull_request[STATUS_VALUE] == PENDING:
             pending_pull_requests.append(pull_request)
    return pending_pull_requests
```


We did some simple alterations here. We renamed some variables, found a good name for the method, and extracted some constants. Now the method seems pretty straightforward, right? We can do one more simple change to make a code even more readable.  


```python
def get_pending_pull_requests(self) -> List[PullRequest]:
    pending_pull_requests: List[PullRequest] = []
    for pull_request in self.embarked_pull_requests:
        if pull_request.is_pending:
             pending_pull_requests.append(pull_request)
    return pending_pull_requests
```


## Variable naming

Sometimes it ain't that easy to come up with good variable naming and thus many jokes are written about it:

![IMG](/pictures/variable_name.png)

Why is this important? Readability.

Imagine getting to read code like this:

```python
x = input()
y, z = x.split()
print(z, y, sep=', ')
```

Is it easy to understand what is happening? What is the aim of the code? What is it supposed to do?
Now compare it with:


```python
name = input()
first_name, last_name = name.split()
print(last_name, first_name, sep=', ')
```

Which Zen of Python line does this reflect the best?
Discuss.

The same rules apply to everything, functions, classes etc.
**Do not** 🛑  go around abbreviating names like an example below, because this just brings chaos and misinterpretation of what was actually meant:

```python
def db(x: int) -> int:
  return x * 2
```

after some time it might not be obvious what _db_ does, it was when you were writing the function and using it, but after a week or two, you see usage of _db_ in your code and it is not that obvious anymore. Instead you can do something like:

```python
def multiply_by_two(x: int) -> int:
    return x * 2
```


Imagine now reviewing the code of your colleague:
```python
pi = 3.14
CustomerName = "John Doe"
CUSTOMER_AGE = 15
```


if later on these variable were used in the code, what would be the expectations of the developers for these variables? How would You do it?
Discuss by looking into naming conventions table above.


## Conventions

Rely on conventions to find suitable names.

* `Class` and `object` names should be a noun or noun phrases, like PullRequest, MergeAction or BranchUpdater. Avoid terms like Manager, Processor, Data or Info in the name, they are too vague.
* `Method` and `function` names should contain a verb or verb phrase, like add_pull, remove_pull or send_merge_signal. You can prefix accessors with get (or create a @propetry), mutators with set and predicates with is, can or has. A long descriptive name is better than short, enigmatic names or a long explanatory comment.


## Maximum line length

PEP 8 suggests lines should be limited to 79 characters. This is because it allows you to have multiple files open next to one another, while also avoiding line wrapping. Nowadays it is accepted to have between 120-140 characters length in one line. For Example for pylinter not to complain we can create a file in the project directory called ***.pylintrc***

## Imports

Wildcard imports (from <module> import *) should be avoided, as they make it unclear which names are present in the namespace, confusing both readers and many automated tools. There is one defensible use case for a wildcard import, which is to republish an internal interface as part of a public API (for example, overwriting a pure Python implementation of an interface with the definitions from an optional accelerator module and exactly which definitions will be overwritten isn’t known in advance).



## Whitespace around Binary Operators
Surround the following binary operators with a single space on either side:

* Assignment operators (=, +=, -=, and so forth)
* Comparisons (==, !=, >, <. >=, <=) and (is, is not, in, not in)
* Booleans (and, not, or) 

BAD:
```python
a=5
something=5>4
name="John"
```

GOOD:
```python
a = 5
something = 5 > 4
name = "John"
```


In conclusion there are plenty of rules it might be a bit overwhelming to start writing python code as it should be written if one was not used to do it. But there are plenty of tools that can help you: linters, formatters etc. We will review them in other topics.


## Avoid magic constants/ hardcoding at all costs

In programming, a magic constant is a value that is hard-coded into the program and is not defined by a named constant or variable. Magic constants are considered bad practice because they make the code difficult to read and maintain.

BAD: 

```python
def calculate_area(radius):
    return 3.14159 * radius * radius

```

GOOD:
```python
PI = 3.14159

def calculate_area(radius: float) -> float:
    return PI * radius * radius

```