# views.py

from django.shortcuts import render
from .markdown_processor import markdown_processor as mp

import re

def markdown_to_html(request):
    if request.method == 'POST':
        markdown_text = request.POST.get('markdown_text', '')
        html_output = mp.MarkdownParser(markdown_text).parse()
        return render(request, 'markdown_result.html', {'html_output': html_output})

    return render(request, 'markdown_form.html')
