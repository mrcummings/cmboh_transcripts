import os
import re

def convert_timestamp(timestamp):
    """Convert a timestamp in the format [HH:MM:SS] to HH:MM:SS"""
    return timestamp.strip('[]')

def get_next_timestamp(lines, current_index):
    """Get the next timestamp from the lines starting from the current index"""
    for i in range(current_index + 1, len(lines)):
        match = re.match(r'\[(\d{2}:\d{2}:\d{2})\]', lines[i])
        if match:
            return match.group(1)
    return None

def txt_to_vtt(txt_path, vtt_path):
    with open(txt_path, 'r', encoding='utf-8') as txt_file:
        lines = txt_file.readlines()
    
    with open(vtt_path, 'w', encoding='utf-8') as vtt_file:
        vtt_file.write("WEBVTT\n\n")
        
        # Extract metadata and transcript lines
        metadata_lines = lines[:7]
        transcript_lines = lines[8:]
        
        # Write metadata to VTT file
        for line in metadata_lines:
            if line.strip():
                vtt_file.write(line.strip() + "\n")
        vtt_file.write("\n")
        
        for i, line in enumerate(transcript_lines):
            match = re.match(r'\[(\d{2}:\d{2}:\d{2})\]', line)
            if match:
                start_time = match.group(1)
                next_timestamp = get_next_timestamp(transcript_lines, i)
                if next_timestamp:
                    end_time = convert_timestamp(next_timestamp)
                else:
                    end_time = "99:59:59"  # Use a large end time for the last segment
                vtt_file.write(f"\n{start_time} --> {end_time}\n")
                vtt_file.write(line[len(match.group(0)):].strip() + "\n")
            else:
                vtt_file.write(line.strip() + "\n")

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