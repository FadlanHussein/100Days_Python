import os
import markdown

def read_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def convert_markdown_to_html(markdown_text):
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
        }}
        h1, h2, h3 {{
            color: #333;
        }}
        a {{
            color: #1a73e8;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
        }}
        th {{
            background-color: #f2f2f2;
        }}
        pre {{
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
        }}
        code {{
            background-color: #f4f4f4;
            padding: 2px 5px;
            border-radius: 3px;
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

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    default_in = os.path.join(base_dir, "markdown.md")
    default_out = os.path.join(base_dir, "example.html")

    markdown_file = input("Enter the path to your Markdown file (default: markdown.md): ").strip() or default_in
    output_file = input("Enter the path to save the HTML file (default: example.html): ").strip() or default_out

    # Handle jika user memasukkan nama file tanpa path lengkap
    if not os.path.isabs(markdown_file) and not os.path.exists(markdown_file):
        rel_in = os.path.join(base_dir, markdown_file)
        if os.path.exists(rel_in):
            markdown_file = rel_in

    if not os.path.isabs(output_file):
        output_file = os.path.join(base_dir, output_file)

    try:
        markdown_text = read_markdown_file(markdown_file)
        html_content = convert_markdown_to_html(markdown_text)
        html_with_template = wrap_in_html_template(html_content)
        write_html_file(html_with_template, output_file)
        print(f"HTML file has been generated and saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
