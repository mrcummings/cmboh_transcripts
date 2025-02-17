import os

# note: still not properly removing empty lines from files

def clean_transcript_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Find the index of the timestamp line
    timestamp_index = next(i for i, line in enumerate(lines) if line.startswith("[00:00:00]"))
    
    # Separate metadata and transcript lines
    metadata_lines = lines[:timestamp_index]
    transcript_lines = lines[timestamp_index:]
    
    # Remove empty lines from metadata
    cleaned_metadata_lines = [line for line in metadata_lines if line.strip()]
    
    # Ensure one empty line between metadata and transcript
    cleaned_lines = cleaned_metadata_lines + ['\n'] + transcript_lines
    
    # Remove any empty lines immediately after the first timestamp
    if cleaned_lines[timestamp_index + 1].strip() == '':
        cleaned_lines.pop(timestamp_index + 1)
    
    # Remove any trailing empty lines at the end of the file
    while cleaned_lines and cleaned_lines[-1].strip() == '':
        cleaned_lines.pop()
    
    # Write cleaned content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(cleaned_lines)

def clean_all_transcripts(input_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            file_path = os.path.join(input_folder, filename)
            clean_transcript_file(file_path)
            print(f'Cleaned {filename}')

if __name__ == "__main__":
    input_folder = 'transcripts-txt'
    clean_all_transcripts(input_folder)