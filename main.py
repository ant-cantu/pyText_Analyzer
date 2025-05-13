# main.py
import text_analyzer as t_a

print("*** Text Analyzer Test Program ***\n")

while True:
    file_name = input("Please enter the file name: ")
    # file_name = "sample_text.txt"

    # Initialize an object of the Text_Analyzer class
    file = t_a.Text_Analyzer(file_name)

    # Call file_exist() module to check if the file exist
    if file.file_exist():
        # Read the contents of the file into a list of lines
        file.read_file()

        # Print total line count
        print(f"Total line count from file: {file.line_count()}\n")

        # Print total character count
        print(f"Total character count from file: {file.char_count(True)}\n")

        # Print total character count
        print(f"Total character count excluding whitespace from file: {file.char_count(False)}\n")

        # Print total word count
        print(f"Total word count for the file: {file.word_count()}\n")

        # Call module word_freq() which calculates word frequencies
        file.word_freq()