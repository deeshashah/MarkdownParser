import re
from typing import List
import unittest

MAX_ALLOWED_HEADING = 6

class MarkdownParser:

    def __init__(self, markdown_text: str):
        self.markdown_text = markdown_text

    def parse(self) -> str:
        """Convert the Markdown text to HTML."""

        lines = self.markdown_text.splitlines()
        html_lines = []

        for line in lines:
            index = 0
            while index < len(line) and line[index].isspace():
                index += 1
            if index < len(line) and line[index] == '#':
                html_lines.append(self.convert_heading(line, index))
            elif index < len(line):
                html_lines.append(self.convert_paragraph(line, 0))

        return '\n'.join(html_lines)

    def convert_heading(self, line: str, start_index: int) -> str:
        """Convert a Markdown heading to HTML."""

        heading_level = 0
        while start_index < len(line) and line[
                start_index] == '#' and heading_level <= MAX_ALLOWED_HEADING:
            heading_level += 1
            start_index += 1
        # If more hashes than 6 or if no whitespace after hashes, we treat is as a paragraph
        if heading_level > MAX_ALLOWED_HEADING or (
                not line[start_index].isspace()):
            return self.convert_paragraph(line, 0)
        
        # Skip any leading whitespace after the hashes
        while start_index < len(line) and line[start_index].isspace():
            start_index += 1
        heading_text = line[start_index:]  # Everything after the heading level
    
        # Process HTTPS links in the heading text
        heading_text = self.process_links(heading_text)
        return f"<h{heading_level}>{heading_text}</h{heading_level}>"

    def convert_paragraph(self, line: str, start_index: int) -> str:
        """Convert a line to a paragraph, processing any links."""

        # Get the text for the paragraph starting from the current index
        paragraph_text = line[start_index:]
        processed_line = self.process_links(paragraph_text)
        return f"<p>{processed_line}</p>"

    def process_links(self, text: str) -> str:
        """Convert Markdown links to HTML links."""

        link_pattern = r'\[([^\]]+)\]\((https?://[^\s)]+)\)'
        return re.sub(link_pattern, r'<a href="\2">\1</a>', text)