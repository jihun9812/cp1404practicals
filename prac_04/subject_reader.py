"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)

def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subjects = []
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        subjects.append(parts)
    input_file.close()
    return subjects


def display_subject_details(subjects):
    "Display subjects details in the desired format"
    for subject in subjects:
        print(f'{subject[0]} is taught by {subject[1]} and has {subject[2]} students')


main()