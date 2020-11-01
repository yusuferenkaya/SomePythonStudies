"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1


def singleline_diff(line1, line2):
    """
       Inputs:
         line1 - first single line string
         line2 - second single line string
       Output:
         Returns the index where the first difference between
         line1 and line2 occurs.

         Returns IDENTICAL if the two lines are the same.
       """
    shorter, longer = line1, line2
    if len(line2) < len(line1):
        shorter, longer = line2, line1
    index = 0
    for _ in range(len(shorter)):
        if shorter[index] == longer[index]:
            index += 1
        else:
            return index
    if len(shorter) != len(longer):
        return index
    return IDENTICAL


def singleline_diff_format(line1, line2, idx):
    """
        Inputs:
          line1 - first single line string
          line2 - second single line string
          idx   - index at which to indicate difference
        Output:
          Returns a three line formatted string showing the location
          of the first difference between line1 and line2.

          If either input line contains a newline or carriage return,
          then returns an empty string.

          If idx is not a valid index, then returns an empty string.
        """
    longer, shorter = line2, line1
    if len(line2) < len(line1):
        longer, shorter = line1, line2
    if len(longer) <= idx or idx > len(longer) + 1 or "\n" in line1 or "\n" in line2 or idx < 0:
        return ""

    return "{}\n".format(line1) + "="*idx + "^\n" + "{}\n".format(line2)


def multiline_diff(lines1, lines2):
    """
        Inputs:
          lines1 - list of single line strings
          lines2 - list of single line strings
        Output:
          Returns a tuple containing the line number (starting from 0) and
          the index in that line where the first difference between lines1
          and lines2 occurs.

          Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
        """
    shorter, longer = lines1, lines2

    if len(lines2) < len(lines1):
        shorter, longer = lines2, lines1
    for i in range(len(shorter)):
        if shorter[i] != longer[i]:
            letter_index = singleline_diff(shorter[i], longer[i])
            return i, letter_index
        elif len(shorter) != len(longer):
            return len(shorter), 0
    if len(shorter) == 0:
        return 0, 0

    return IDENTICAL, IDENTICAL


def get_file_lines(filename):
    """
        Inputs:
          filename - name of file to read
        Output:
          Returns a list of lines from the file named filename.  Each
          line will be a single line string with no newline ('\n') or
          return ('\r') characters.

          If the file does not exist or is not readable, then the
          behavior of this function is undefined.
        """
    openfile = open(filename, "r")
    line_list = []
    for line in openfile:
        line = line.strip()
        line_list.append(line)
    openfile.close()
    return line_list


def file_diff_format(filename1, filename2):
    """
        Inputs:
          filename1 - name of first file
          filename2 - name of second file
        Output:
          Returns a four line string showing the location of the first
          difference between the two files named by the inputs.

          If the files are identical, the function instead returns the
          string "No differences\n".

          If either file does not exist or is not readable, then the
          behavior of this function is undefined.
        """
    file1 = get_file_lines(filename1)
    file2 = get_file_lines(filename2)
    if file1 == file2:
        return "No differences\n"
    difference = multiline_diff(file1, file2)
    line_index, letter_index = difference[0], difference[1]
    single_diff = singleline_diff_format(file1[line_index], file2[line_index], letter_index)
    return "Line " + str(line_index) + ":\n" + single_diff
