def remove_duplicates():
    # Read all lines from the file
    with open('todas.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Remove duplicates using a set while preserving order
    seen = set()
    unique_lines = []
    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace
        if line and line not in seen:  # Only add non-empty lines that haven't been seen
            seen.add(line)
            unique_lines.append(line)
    
    # Write back unique lines to the file
    with open('todas.txt', 'w', encoding='utf-8') as file:
        for line in unique_lines:
            file.write(line + '\n')

if __name__ == '__main__':
    remove_duplicates()
    print("Duplicate lines have been removed from todas.txt") 