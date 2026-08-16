import os
from pypdf import PdfMerger

merger = PdfMerger()
current_dir = os.path.dirname(__file__)

pdf_files = ["sample1.pdf", "sample2.pdf", "sample3.pdf"]

# loop untuk menggabungkan file
for pdf in pdf_files:
    pdf_path = os.path.join(current_dir, pdf)
    merger.append(pdf_path)

output_path = os.path.join(current_dir, "merged_output.pdf")
merger.write(output_path)
merger.close()

print(f"Berhasil menggabungkan PDF ke {output_path}")
