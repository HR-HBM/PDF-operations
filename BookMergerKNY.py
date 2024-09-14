from pypdf import PdfMerger

pdfs = ['KNY1compressed.pdf', 'KNY2compressed.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("KNYMergedSection1-2.pdf")
merger.close()