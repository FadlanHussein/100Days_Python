import os
import markdown

def convert_markdown_to_html(markdown_text):
    # Mengonversi markdown ke HTML, termasuk ekstensi tabel dan codeblock
    html = markdown.markdown(markdown_text, extensions=['tables', 'fenced_code'])
    return html

def read_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def save_html_file(html_content, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html_content)
    print(f"HTML file saved successfully to: {file_path}")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "markdown.md")
    output_path = os.path.join(base_dir, "output.html")

    if not os.path.exists(input_path):
        print(f"File '{input_path}' not found!")
        return

    markdown_text = read_markdown_file(input_path)
    html_content = convert_markdown_to_html(markdown_text)
    save_html_file(html_content, output_path)

if __name__ == "__main__":
    main()
