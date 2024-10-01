### Django Markdown to HTML Parser


This project builds a UI form which takes in some markdown text as input and outputs the markdown format as well as the HTML version of it. 

<img width="767" alt="Screen Shot 2024-09-30 at 5 25 08 PM" src="https://github.com/user-attachments/assets/ea28b1ff-ed96-4c7c-a944-c49464dbf191">

<img width="767" alt="Screen Shot 2024-09-30 at 5 25 27 PM" src="https://github.com/user-attachments/assets/e2884cf9-1968-4b79-a5f3-706f4af0052e">



### Instructions

Follow these steps to get your development environment set up:

1. Clone the repository:

```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```


3. Install the requirements:

```bash
Copy code
pip install -r requirements.txt
```

4. Run the development environment
```bash
python manage.py runserver
```

Usage
Describe how to use your application after installation. Include examples and screenshots if necessary.

Navigate to http://127.0.0.1:8000/markdown_parser/markdown/ in your browser to interact with the system.


Provide instructions on how to run tests:

Simply run the following to run tests. 

```bash
python3 markdown_processor_tests.py
```


#### Assumptions

1. If number of hashes exceeds 6, then multiple assumptions can be made: 
    a. Renders H6 heading followed by the remaining hashes and text. 
    b. Renders by default the lowest header (H6) followed by the hash
    c. Renders it as a paragraph. (Chosing this)

2. Ignore any of the trailing white spaces. 


Test Cases

A) The Headers Scenario

1. Empty Input. 
2. Doing what it needs to.  
3. Initial and Trailing white spaces (Ignored). (Assumption)
4. \# comes somewhere in between, multiple Headers on One Line
5. Consider escapes as something to be ignored. 
6. ### \# Hello --> Test This
7. Test where white space is missing after # --> Consider it as a paragraph.
8. Multiple Hashes > 6
9. Headers with a link. 



B) Links

1. Headers with a link. 
2. Paragraphs with a link.
3. Invalid links --> Fallover to a paragraph. 
4. Assumption --> Only http and https are considered as valid input links. 

C) Paragraphs

1. Doing what it is expected to do. 
2. Trailing white spaces not ignored at beginning. 
3. Works with hyperlinks
