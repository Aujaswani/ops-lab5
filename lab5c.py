#!/usr/bin/env python3

def add(number1, number2):
    """
    Add two numbers together. Returns 'error: could not add numbers' on exception.
    """
    try:
        return int(number1) + int(number2)
    except (ValueError, TypeError):
        return 'error: could not add numbers'

def read_file(filename):
    """
    Reads a file, returns a list of all lines with newlines preserved.
    Returns 'error: could not read file' on exception.
    """
    try:
        with open(filename, 'r') as f:
            return [line for line in f]  # Preserve newlines
    except Exception:
        return 'error: could not read file'

def append_file_string(file_name, string_of_lines):
    """
    Appends the string_of_lines to the end of the file.
    """
    try:
        with open(file_name, 'a') as f:
            f.write(string_of_lines)
    except Exception:
        pass

def write_file_list(file_name, list_of_lines):
    """
    Writes all items from list_of_lines to the file.
    """
    try:
        with open(file_name, 'w') as f:
            for line in list_of_lines:
                f.write(line + '\n')
    except Exception:
        pass

def copy_file_add_line_numbers(file_name_read, file_name_write):
    """
    Reads data from file_name_read, writes to file_name_write with line numbers.
    """
    try:
        with open(file_name_read, 'r') as f_read, open(file_name_write, 'w') as f_write:
            for idx, line in enumerate(f_read, start=1):
                f_write.write(f"{idx}:{line}")
    except Exception:
        pass

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    
    append_file_string(file1, string1)
    print(read_file(file1))
    
    write_file_list(file2, list1)
    print(read_file(file2))
    
    copy_file_add_line_numbers(file2, file3)
    print(read_file(file3))
    
    print(add(10, 5))
    print(add('10', 5))
    print(add('abc', 5))
    print(read_file('seneca2.txt'))
    print(read_file('file10000.txt'))
