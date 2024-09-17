import os
import tokenize
import keyword
from io import StringIO


# Define the input and output directories
input_dir = 'input'  # Directory with the input files
output_dir = 'output'  # Directory where the output files will be written
offset = 500

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


def adjust_brace_position(s: str, brace) -> str:
    # Check if brace is in the string
    brace_index = s.find(brace)
    
    if brace_index == -1:
        # No brace found, return the string as is
        return s
    
    # Calculate how many spaces are needed to make '{' at the 50th position
    spaces_needed = offset - brace_index
    
    # If the brace is already at or beyond the 50th position, return the string
    if spaces_needed <= 0:
        return s
    
    # Insert the necessary spaces before the brace
    adjusted_string = s[:brace_index] + ' ' * spaces_needed + s[brace_index:]
    
    return adjusted_string


def move_char_to_previous_line(newline, oldline, char):
    if char in newline:
        newline = newline.replace(char, '', 1)

        # Check if oldline ends with a newline character
        if oldline.endswith('\n'):
            # Insert the character before the newline character
            oldline = oldline[:-1] + char + '\n'
        else:
            oldline += char
    return newline, oldline

def move_char_to_previous_line_with_whitespace(newline, oldline, char):

    non_whitespace = sum(1 for char in newline if not char.isspace())

    try:
        print("NWS: = " + str(non_whitespace) + " : " + newline, end='')
    except:
        pass

    if char in newline:
        newline = newline.replace(char, '', 1)

        # Check if oldline ends with a newline character
        if oldline.endswith('\n'):
            # Insert the character before the newline character
            oldline = oldline[:-1] + char + '\n'
        else:
            oldline += char
    return newline, oldline

def move_end_char_to_previous_line(newline, oldline, char):
    if char in newline:
        newline = newline.replace(char, '', 1)

        # Check if oldline ends with a newline character
        if oldline.endswith('\n'):
            # Insert the character before the newline character
            oldline = oldline[:-1] + char + '\n'
        else:
            oldline += char
    return newline, oldline


def move_two_char_to_end(line, char1, char2):
    # Check if the line ends with a newline character
    if line.endswith('\n'):
        newline = '\n'
        line = line[:-1]  # Remove the newline for processing
    else:
        newline = ''

    contains_char1 = char1 in line
    contains_char2 = char2 in line

    # If the line contains neither char1 nor char2, return the line as is
    if not (contains_char1 or contains_char2):
        return line + newline

    # If the line contains char1 XOR char2
    elif contains_char1 != contains_char2:
        # Move the character to the end of the line (before the newline)
        if contains_char1:
            # Remove the first occurrence of char1
            line = line.replace(char1, '', 1)
            # Append char1 to the end
            line += char1
        else:
            # Remove the first occurrence of char2
            line = line.replace(char2, '', 1)
            # Append char2 to the end
            line += char2
        return line + newline

    # If the line contains both char1 and char2
    elif contains_char1 and contains_char2:
        # Remove the first occurrence of both char1 and char2
        line = line.replace(char1, '', 1)
        line = line.replace(char2, '', 1)
        # Append both char1 and char2 to the end, maintaining the order
        line += char1 + char2
        return line + newline

    # For any other case (should not occur), return the line as is
    else:
        return line + newline


def find_first_char(line, char1, char2):
    index1 = line.find(char1)
    index2 = line.find(char2)
    
    if index1 == -1 and index2 == -1:
        return None
    elif index1 == -1:
        return char2
    elif index2 == -1:
        return char1
    else:
        return char1 if index1 <= index2 else char2



# Loop through all the files in the input directory
for filename in os.listdir(input_dir):
    input_file_path = os.path.join(input_dir, filename)

    # Ensure we're only processing files (skip directories, etc.)
    if os.path.isfile(input_file_path):
        output_file_path = os.path.join(output_dir, filename)

        # Open the input file for reading
        with open(input_file_path, 'r') as infile:
            # Read the file line by line
            lines = infile.readlines()

        # Open the corresponding output file for writing
        with open(output_file_path, 'w') as outfile:
            newline = ""
            oldline_to_write = ""
            line_num = 0

            for line in lines:
                newline = line
                print("#" + str(line_num) + ": ", end="")

                newline, oldline_to_write = move_char_to_previous_line(newline, oldline_to_write, '}')
                line_empty = (sum(1 for char in newline if not char.isspace()) == 0)


                if '}' in line and line_empty:
                    pass
                else:
                    newline = move_two_char_to_end(newline, ';', '}')
                    first_char = find_first_char(newline, ';', '}')
                    newline = adjust_brace_position(newline, '{')

                    if first_char == ';' :
                        newline = adjust_brace_position(newline, ';')
                    
                    newline = adjust_brace_position(newline, '}')
                    
                    print(newline, end="")

                    # Write each line to the output file
                    outfile.write(oldline_to_write)
                    oldline_to_write = newline
                

                line_num+=1

print("Files have been copied to the 'output' folder with the same content.")