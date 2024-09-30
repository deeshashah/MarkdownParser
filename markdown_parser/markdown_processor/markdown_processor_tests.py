import unittest
import markdown_processor as mp

class TestMarkdownProcessor(unittest.TestCase):

    def setUp(self):
        self.converter = mp.MarkdownParser("")

    """
    Expected functionality works correctly
    """
    def test_heading_conversion(self):
        self.converter.markdown_text = "# Heading 1"
        self.assertEqual(self.converter.parse(), "<h1>Heading 1</h1>")

        self.converter.markdown_text = "## Heading 2"
        self.assertEqual(self.converter.parse(), "<h2>Heading 2</h2>")

    """
    Multiple hashes together fall over to a paragraph.
    """
    def test_extra_hash_heading_conversion(self):
        self.converter.markdown_text = "######## Heading 1"
        self.assertEqual(self.converter.parse(), "<p>######## Heading 1</p>")

    """
    Preceding whitespaces are ignored
    """
    def test_whitespace_before_heading(self):
        self.converter.markdown_text = "    ### Heading 3"
        self.assertEqual(self.converter.parse(), "<h3>Heading 3</h3>")

    """
    If a different char then # appears after series of hashes, it falls over to paragraph
    """
    def test_random_char_after_hashes(self):
        self.converter.markdown_text = "###, Heading 3"
        self.assertEqual(self.converter.parse(), "<p>###, Heading 3</p>")

    """
    If a different char then # appears after series of hashes, it falls over to paragraph
    """
    def test_not_heading(self):
        self.converter.markdown_text = "##\## Heading 3"
        self.assertEqual(self.converter.parse(), "<p>##\## Heading 3</p>")

    """
    Everything after a hash (<=6) series followed by space falls to a heading
    """
    def test_heading(self):
        self.converter.markdown_text = "## \## Heading 2"
        self.assertEqual(self.converter.parse(), "<h2>\## Heading 2</h2>")

    """
    Hyperlink works as expected in a heading.
    """
    def test_heading_with_hyperlink(self):
        self.converter.markdown_text = "## This is a header [with a link](http://yahoo.com)"
        self.assertEqual(self.converter.parse(), "<h2>This is a header <a href=\"http://yahoo.com\">with a link</a></h2>")


    # Paragraph test cases
    """
    The base functionality works correctly
    """
    def test_paragraph_conversion(self):
        self.converter.markdown_text = "This is a paragraph."
        self.assertEqual(self.converter.parse(),
                         "<p>This is a paragraph.</p>")

    """
    Whitespaces before a paragraph are preserved
    """
    def test_whitespace_before_paragraph_conversion(self):
        self.converter.markdown_text = "     This is a paragraph."
        self.assertEqual(self.converter.parse(),
                         "<p>     This is a paragraph.</p>")

    """
    Whitespaces after a paragraph are preserved
    """
    def test_whitespace_after_paragraph_conversion(self):
        self.converter.markdown_text = "     This is a paragraph.     "
        self.assertEqual(self.converter.parse(),
                         "<p>     This is a paragraph.     </p>")

    """
    Link conversions to <a></a> within a paragraph is working correctly.
    """
    def test_link_conversion(self):
        self.converter.markdown_text = "This is a [link](http://example.com)."
        self.assertEqual(
            self.converter.parse(),
            "<p>This is a <a href=\"http://example.com\">link</a>.</p>")

    """
    Multiple Link conversions to <a></a> within a paragraph is working correctly.
    """
    def test_multiple_links_conversion(self):
        self.converter.markdown_text = "This is a [link](http://example.com) which takes us to [recipe](http://recipe.com)."
        self.assertEqual(
            self.converter.parse(),
            "<p>This is a <a href=\"http://example.com\">link</a> which takes us to <a href=\"http://recipe.com\">recipe</a>.</p>")

    """
    Invalid link formats are not considered as actual links and fall over to plain text in a paragraph
    """
    def test_invalid_link_format(self):
        self.converter.markdown_text = "Invalid link [Intuit](not-a-url)"
        self.assertEqual(
            self.converter.parse(),
            "<p>Invalid link [Intuit](not-a-url)</p>")
    """
    Combination of a markdown text blob works correctly
    """
    def test_combined_input(self):
        markdown_input = """# Sample Document

Hello!

This is sample markdown for the [Mailchimp](https://www.mailchimp.com) homework assignment.

## Another Header

This is a paragraph [with an inline link](http://google.com). Neat, eh?
"""
        expected_output = """<h1>Sample Document</h1>
<p>Hello!</p>
<p>This is sample markdown for the <a href="https://www.mailchimp.com">Mailchimp</a> homework assignment.</p>
<h2>Another Header</h2>
<p>This is a paragraph <a href="http://google.com">with an inline link</a>. Neat, eh?</p>"""
        self.converter.markdown_text = markdown_input
        self.assertEqual(self.converter.parse(), expected_output)

    """
    Blank lines are parsed correctly
    """
    def test_blank_lines(self):
        self.converter.markdown_text = "\n\n# Heading\n\nContent\n\n"
        expected_output = "<h1>Heading</h1>\n<p>Content</p>"
        self.assertEqual(self.converter.parse(), expected_output)

    """
    Large input text is processed and returns the correcly results.
    """
    def test_large_input(self):
        # Test with a large input
        large_input = "# Large Heading\n" + ("This is a line. " * 1000).strip()
        expected_output = "<h1>Large Heading</h1>\n<p>This is a line. " + (
            "This is a line. " * 999).strip() + "</p>"
        self.converter.markdown_text = large_input
        self.assertEqual(self.converter.parse(), expected_output)


if __name__ == "__main__":
    unittest.main()