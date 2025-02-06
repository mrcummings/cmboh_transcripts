import os

def txt_to_vtt(txt_path, vtt_path):
    with open(txt_path, 'r', encoding='utf-8') as txt_file:
        lines = txt_file.readlines()
    
    with open(vtt_path, 'w', encoding='utf-8') as vtt_file:
        vtt_file.write("WEBVTT\n\n")
        for i, line in enumerate(lines):
            start_time = f"00:00:{i:02d}.000"
            end_time = f"00:00:{i+1:02d}.000"
            vtt_file.write(f"{start_time} --> {end_time}\n")
            vtt_file.write(line.strip() + "\n\n")

def convert_all_txt_to_vtt(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            txt_path = os.path.join(input_folder, filename)
            vtt_filename = os.path.splitext(filename)[0] + '.vtt'
            vtt_path = os.path.join(output_folder, vtt_filename)
            txt_to_vtt(txt_path, vtt_path)
            print(f'Converted {filename} to {vtt_filename}')

if __name__ == "__main__":
    input_folder = 'transcripts-txt'
    output_folder = 'transcripts-vtt'
    convert_all_txt_to_vtt(input_folder, output_folder)