# text_analyzer.py
import string

class Text_Analyzer:
    def __init__(self, file_name):
        """
        Constructor: Initialize object of Text_Analyzer

        Args:
            file_name (str): The name of the file to analyze
        """
        # Store file_name argument into _file_name
        self._file_name = file_name
        
    def file_exist(self):
        """
        Checks if the file exist. If it does, prompt user with a successful message.
        If it does not exist, prompt user with an error.
        """
        try:
            # Open file and return True if successful, False if not
            with open(self._file_name, "r") as f:
                print(f"(System) {self._file_name} successfully opened.\n")
                return True
        except FileNotFoundError:
            print(f"(System) Error, the file '{self._file_name}' was not found.\n")
            return False
        except Exception as e:
            print(f"(System) Error reading file: {e}\n")
            return False

    def read_file(self):
        """
        Reads the file and stores the files lines and entire text contents

        Vars:
            Internal:
                _file_contents (list): Stores the files lines into a list
                _text_contents (str): Stores the text contents into a string
        """
        try:
            # Open file and store lines as _file_contents
            with open(self._file_name) as r:
                self._file_contents = r.readlines()
            # Open file and store file as _text_contents
            with open(self._file_name) as r:
                self._text_contents = r.read()
        except Exception as e:
            print(f"(System) Error reading file: {e}\n")

    def line_count(self):
        """
        Returns the amount of lines in the file as an integer.

        Vars:
            Internal:
                _count (int): Store the amount of lines
        """
        _count = 0 # Variable to store line count
        # For each line, add to count by 1
        for i in enumerate(self._file_contents):
            _count += 1
        return _count
    
    def char_count(self, whitespaces):
        """
        Returns the amount of characters in the file as an integer, options for counting
        with or without whitespaces.

        Args:
            whitespaces (boolean):  True results in counting whitespaces, False
                                    results in not counting whitespaces.

        Vars:
            Internal:
                _count (int): Store the amount of characters
        """
        _count = 0 # Variable to store character count
        # If counting whitespaces is True, include whitespaces as a count
        if whitespaces:
            for char in self._text_contents:
                _count += 1
            return _count
        # If whitespace is False, exclude whitespaces as a count
        else:
            for char in self._text_contents:
                if not char.isspace():
                    _count += 1
            return _count
        
    def word_count(self):
        """
        Takes contents of text file and splits it into individual words 
        and removes punctuation. Then proceeds to count the words and returns
        the length of the list (amount of words).

        Vars:
            Internal:
                _word_list (list): Stores the text contents of the file into individual words in a list
                _clean_word_list (list): Stores the cleaned up words into a list (lowercase and no punctuation)
                _lowercase (str): Stores the word from the list as a lowercase word
                _remove_punctuation (str): Stores the lowercase word with removed punctuation
        """
        # Split text contents into individual words and store in _word_list
        _word_list = self._text_contents.split()

        # Create empty list inorder to hold cleaned words
        self._clean_word_list = []
        
        # Loop through words in _word_list and strip punctuation and convert to lower case
        for words in _word_list:
            _lowercase = words.lower()
            _remove_punctuation = _lowercase.strip(string.punctuation)
            self._clean_word_list.append(_remove_punctuation)

        # Return the length of the cleaned list
        return len(self._clean_word_list)
    
    def word_freq(self):
        """
        Takes the clean word list generated from module word_count() and
        adds words to a dictionary to count the frequency of words used

        Vars:
            Internal:
                _word_counts (dict.): Dictionary for storing the words as a key, and the
                                      number of times it appears as a value.
        """
        # Dictionary for storing word frequency
        _word_counts = {}

        # Run word count to generate clean word list
        self.word_count()

        # Loop through the clean word list
        for words in self._clean_word_list:
            # If word does not exist in dictionary, add word and set value to 1
            if _word_counts.get(words) == None:
                _word_counts[words] = 1
            # If word exisit, increase value by 1
            else:
                _word_counts[words] += 1

        # Loop through dictionary and print its key and value
        for key in _word_counts.keys():
            value = _word_counts[key]
            print(f"Word: '{key}' appears {value} times in the file.")