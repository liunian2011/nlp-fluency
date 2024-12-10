from pypdf import PdfWriter

merger = PdfWriter()

pdf_files = ["documentprocessing.pdf", "data.pdf"]

# Iterate through the PDF files and append them to the merger
for pdf in pdf_files:
    merger.append(pdf)

# Write the merged PDF to a new file named "merged-pdf.pdf"
merger.write("merged-top3.pdf")

# Close the merger object
merger.close()