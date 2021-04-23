"""
Palindrome class realization.
"""

from math import ceil
from linkedstack import LinkedStack   # or from linkedstack import LinkedStack

class Palindrome:
    '''
    Palindrome class.
    '''
    def read_file(self, path):
        """
        Retruns a list of words from the file.

        Args:
            path ([str]): [path to the file].

        Returns:
            [list]: [a list of words from the file].
        """
        words = []
        with open(path, 'r', encoding='utf-8') as vocabulary:
            for word in vocabulary.readlines():
                if '+cs=' in word:
                    new_word = word[word.find('+cs=')+4:].split()[0].strip()
                    print(new_word)

                else:
                    new_word = word.split()[0].strip()

                words.append(new_word)

        return words

    @staticmethod
    def check_paindrome(word):
        """
        Checks if the word is a palindrome.

        Args:
            word ([str]): [a word to check].

        Returns:
            [bool]: [boolean value if the given word is a palindrome].
        """
        word_stack = LinkedStack()
        lenght = len(word)
        ceiled_half = ceil(lenght/2)
        for index in range(ceiled_half):
            word_stack.push(word[index])

        for index in range(ceiled_half-1, -1, -1):
            letter_stack = word_stack.pop()
            word_letter = word[-1-index]
            if letter_stack != word_letter:
                return False

        return True

    def find_palindromes_vocabulary(self, vocabulary):
        """
        Returns a list of palindromes from the given list.

        Args:
            vocabulary ([list]): [a list of words].

        Returns:
            [list]: [a list of palindromes from the given list.]
        """
        palindromes = []
        for word in vocabulary:
            if self.check_paindrome(word):
                palindromes.append(word)

        return palindromes

    def find_palindromes(self, file_voc, file_stor):
        """
        Finds palindromes in the given file

        Args:
            voc_list ([str]): [path to a file with words].
            file_name ([str]): [path to a file in which the words should be written in].

        Returns:
            [list]: [a list of palindromes from the given file].
        """
        voc_list = self.read_file(file_voc)
        palindromes = self.find_palindromes_vocabulary(voc_list)
        self.write_to_file(palindromes, file_stor)
        return palindromes

    def write_to_file(self, palindromes, file_name):
        """
        Writes a list of words into the file.

        Args:
            palindromes ([list]): [a list of palindromes from the given file].
            file_name ([str]): [path to a file in which the words should be written in].
        """
        with open(file_name, 'w', encoding = 'utf-8') as file:
            for word in palindromes:
                file.write(word + '\n')

if __name__ == '__main__':
    palindrome = Palindrome()
    palindrome.find_palindromes("base.lst", "palindrome_uk.txt")
    palindrome.find_palindromes("words.txt", "palindrome_en.txt")
