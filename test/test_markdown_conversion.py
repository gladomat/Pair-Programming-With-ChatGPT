import unittest
from ..pair_programmer.utils import markdown_to_html_with_syntax_highlight, convert_to_markdown

class TestMarkdownToHtmlWithSyntaxHighlight(unittest.TestCase):

    def test_basic_markdown_conversion(self):
        input_md = "This is a *simple* markdown text."
        expected_output = "<p>This is a <em>simple</em> markdown text.</p>"
        self.assertEqual(markdown_to_html_with_syntax_highlight(input_md), expected_output)

    def test_code_block_with_specified_language(self):
        input_md = "```python\nprint('Hello, World!')\n```"
        # Expected output should contain highlighted Python code.
        # This is a simplified check as the exact output depends on the syntax highlighter's format.
        self.assertIn('<pre><code class="python">', markdown_to_html_with_syntax_highlight(input_md))


class TestConvertToMarkdown(unittest.TestCase):

    def test_plain_text_conversion(self):
        input_text = "This is a simple text."
        expected_output = "This&nbsp;is&nbsp;a&nbsp;simple&nbsp;text.&nbsp;&nbsp;\n"
        self.assertEqual(convert_to_markdown(input_text), expected_output)

    def test_text_with_dollar_signs(self):
        input_text = "Price is $100."
        expected_output = "Price&nbsp;is&nbsp;&#36;100.&nbsp;&nbsp;\n"
        self.assertEqual(convert_to_markdown(input_text), expected_output)


if __name__ == '__main__':
    unittest.main()
