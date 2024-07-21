"""
CP1404/CP5632 Practical
File and class example - reads file, stores in objects of custom class
"""

from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    # Open the file for reading
    in_file = open('languages.csv', 'r')
    # File format is: Language,Typing,Reflection,Year,PointerArithmetic
    # 'Consume' the first line (header) - we don't need its contents
    in_file.readline()
    # All other lines are language data
    for line in in_file:
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split(',')
        # Reflection and PointerArithmetic are stored as strings (Yes/No) and we want a Boolean
        reflection = parts[2] == "Yes"
        pointer_arithmetic = parts[4] == "Yes"
        # Construct a ProgrammingLanguage object using the elements
        # year should be an int
        language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), pointer_arithmetic)
        # Add the language we've just constructed to the list
        languages.append(language)
    # Close the file as soon as we've finished reading it
    in_file.close()

    # Loop through and display all languages (using their str method)
    for language in languages:
        print(language)


main()
