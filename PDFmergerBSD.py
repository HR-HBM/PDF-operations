import os
import re
from pypdf import PdfMerger

# Directory containing the PDF files (same directory as the script)
pdf_directory = os.path.dirname(os.path.abspath(__file__))

# Pattern to match PDF files in the sequence
pattern = re.compile(r'BSD(\d+)\.pdf')

# List all PDF files in the directory
all_files = os.listdir(pdf_directory)

# Filter and sort files based on the pattern
pdf_files = sorted(
    (f for f in all_files if pattern.match(f)),
    key=lambda f: int(pattern.match(f).group(1))
)

# Full paths for the files to be merged
pdf_files = [os.path.join(pdf_directory, f) for f in pdf_files]

# Merge PDFs
merger = PdfMerger()

for pdf in pdf_files:
    merger.append(pdf)

# Output merged PDF
output_path = os.path.join(pdf_directory, 'BSDBook1.pdf')
merger.write(output_path)
merger.close()

print(f"PDFs successfully merged into {output_path}")
