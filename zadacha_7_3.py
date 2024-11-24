
import string
#files = {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'],
        #'file3.txt': ['word5', 'word6', 'word7']}

class WordsFinder:

    def __init__(self, *files):
        self.file_names = files

    def get_all_words(self):
        all_words = {}
        for filename in self.file_names:
            with open(filename, 'r', encoding='utf-8') as file:
                file.seek(0)
                stroka = file.read()
                punctuation_chars = string.punctuation  # Набор символов !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
                for punctuation in punctuation_chars:
                    stroka = stroka.replace(punctuation, ' ')
                    words = stroka.split()
                    all_words[filename] = words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        results = {}
        for filename, words in all_words.items():
            if word in words:
                try:
                    index = words.index(word) + 1
                except ValueError:
                    index = None
                results[filename] = index
        return results

    def count(self, word):
        all_words = self.get_all_words()
        results = {}
        for filename, words in all_words.items():
            cnt = words.count(word)
            results[filename] = cnt
        return results




# Пример использования
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('text'))  # Найти первое вхождение слова 'text'
print(finder2.count('text'))  # Количество вхождений слова 'text'










#finder2 = WordsFinder('test_file.txt')
#print(finder2.get_all_words()) # Все слова
#print(finder2.find('TEXT')) # 3 слово по счёту
#print(finder2.count('teXT')) # 4 слова teXT в тексте всего
