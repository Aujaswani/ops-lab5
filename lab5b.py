#!/usr/bin/env python3

def read_file_string(file_name):
    """Reads the content of a file and returns it as a string."""
    with open(file_name, 'r') as file:
        return file.read()

def read_file_list(file_name):
    """Reads the content of a file and returns it as a list of lines, stripping the newline character."""
    with open(file_name, 'r') as file:
        return [line.strip() for line in file.readlines()]  # Strip the newline from each line

def append_file_string(file_name, string_of_lines):
    """Appends a string to the file."""
    with open(file_name, 'a') as file:
        file.write(string_of_lines)

def write_file_list(file_name, list_of_lines):
    """Writes each item in a list to a file, one item per line."""
    with open(file_name, 'w') as file:
        for line in list_of_lines:
            file.write(line + '\n')

def copy_file_add_line_numbers(file_name_read, file_name_write):
    """Copies content from one file to another, adding line numbers."""
    with open(file_name_read, 'r') as file_read:
        lines = file_read.readlines()
    
    with open(file_name_write, 'w') as file_write:
        for i, line in enumerate(lines, start=1):
            file_write.write(f"{i}:{line}")
    
if __name__ == '__main__':
    # Define file names and data
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    
    # Perform operations as per the instructions
    append_file_string(file1, string1)
    print(read_file_string(file1))  # Print content of file1 after appending

    write_file_list(file2, list1)
    print(read_file_string(file2))  # Print content of file2 after writing list

    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))  # Print content of file3 after copying with line numbers
