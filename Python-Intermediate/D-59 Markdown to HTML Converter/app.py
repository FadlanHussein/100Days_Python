import markdown

def convert_markdown_to_html(markdown_text):
    html = markdown.markdown(markdown_text)
    return html

markdown_text = "# Hello World\nThis is a **bold** statement."
html_content = convert_markdown_to_html(markdown_text)
print(html_content)
