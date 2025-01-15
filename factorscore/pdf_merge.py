from pypdf import PdfWriter
from ner_predict import file_resolve


def gen_all_merged_pdf(parent_folder):
    folders = file_resolve.literal_folder(parent_folder)
    for folder in folders:
        #merge_top3(folder)
        merge_top1(folder)

def merge_top3(parent_folder):
    merger = PdfWriter()
    pdf_files_path = file_resolve.literal_folder_files(parent_folder)
    folder_name = parent_folder.split('/')[-1]
    # Iterate through the PDF files and append them to the merger
    for pdf in pdf_files_path:
        if not pdf.split('/')[-1].startswith('.'):
            print(pdf)
            merger.append(pdf)

    # Write the merged PDF to a new file named "merged-pdf.pdf"
    merger.write(f"{parent_folder}/{folder_name}_merged_top3.pdf")
    # Close the merger object
    merger.close()

def merge_top1(parent_folder):
    merger = PdfWriter()
    pdf_files_path = file_resolve.literal_folder_files(parent_folder)

    folder_name = parent_folder.split('/')[-1]
    # Iterate through the PDF files and append them to the merger
    for pdf in pdf_files_path:
        if (pdf.endswith('_1.pdf') or pdf.endswith('-1.pdf')) and not pdf.split('/')[-1].startswith('.'):
            merger.append(pdf)

    # Write the merged PDF to a new file named "merged-pdf.pdf"
    merger.write(f"{parent_folder}/{folder_name}_merged_top1.pdf")
    # Close the merger object
    merger.close()


if __name__ == '__main__':
    folder = "/Users/liunian/Downloads/personal/论文相关/医疗实验/1-20/1-amphibian"
    #merge_top3(folder)
    #merge_top1(folder)
    parent_folder = "/Users/liunian/Downloads/personal/论文相关/医疗实验/factscore/12.11/"
    gen_all_merged_pdf(parent_folder)