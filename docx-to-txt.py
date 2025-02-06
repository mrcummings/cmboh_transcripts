import os
from docx import Document

def docx_to_txt(docx_path, txt_path):
    doc = Document(docx_path)
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        for para in doc.paragraphs:
            txt_file.write(para.text + '\n')

def convert_all_docx_to_txt(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith('.docx'):
            docx_path = os.path.join(input_folder, filename)
            txt_filename = os.path.splitext(filename)[0] + '.txt'
            txt_path = os.path.join(output_folder, txt_filename)
            docx_to_txt(docx_path, txt_path)
            print(f'Converted {filename} to {txt_filename}')

if __name__ == "__main__":
    input_folder = 'transcripts-docx'
    output_folder = 'transcripts-txt'
    convert_all_docx_to_txt(input_folder, output_folder)