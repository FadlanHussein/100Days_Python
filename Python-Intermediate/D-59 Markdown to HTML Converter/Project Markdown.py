import os
import markdown

def read_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def convert_markdown_to_html(markdown_text):
    # Convert markdown to html with support for tables and code blocks
    return markdown.markdown(markdown_text, extensions=['tables', 'fenced_code'])

def wrap_in_html_template(content):
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markdown to HTML</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
            color: #24292e;
        }}
        h1, h2, h3 {{
            color: #333;
            border-bottom: 1px solid #eaecef;
            padding-bottom: 0.3em;
        }}
        a {{
            color: #1a73e8;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        code {{
            background-color: #f6f8fa;
            padding: 0.2em 0.4em;
            border-radius: 3px;
            font-family: monospace;
        }}
        pre {{
            background-color: #f6f8fa;
            padding: 16px;
            border-radius: 6px;
            overflow: auto;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin-top: 10px;
            margin-bottom: 10px;
        }}
        th, td {{
            border: 1px solid #dfe2e5;
            padding: 6px 13px;
            text-align: left;
        }}
        th {{
            background-color: #f6f8fa;
        }}
        blockquote {{
            margin: 0;
            padding: 0 1em;
            color: #6a737d;
            border-left: 0.25em solid #dfe2e5;
        }}
    </style>
</head>
<body>
{content}
</body>
</html>"""
    return html_template

def write_html_file(html_content, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(html_content)
    print(f"[OK] HTML file successfully created: {output_path}")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "markdown.md")
    output_path = os.path.join(base_dir, "example.html")

    if not os.path.exists(input_path):
        print(f"Error: '{input_path}' not found.")
        return

    # 1. Baca Markdown
    markdown_text = read_markdown_file(input_path)
    
    # 2. Konversi ke HTML
    html_content = convert_markdown_to_html(markdown_text)
    
    # 3. Bungkus dengan Template CSS & HTML
    html_with_template = wrap_in_html_template(html_content)
    
    # 4. Simpan ke File Output HTML
    write_html_file(html_with_template, output_path)

if __name__ == "__main__":
    main()
