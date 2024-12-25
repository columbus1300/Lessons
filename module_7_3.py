class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    punctuation_marks = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for i in punctuation_marks:
                        line = line.replace(i, '')

                    words.extend(line.split())
                    all_words[file.name] = words
        return all_words

    def find(self, word):
        place = {}
        for k, v in self.get_all_words().items():
            if word.lower() in v:
                place[k] = v.index(word.lower()) + 1
        return place

    def count(self, word):
        counter = {}
        for k, v in self.get_all_words().items():
            counter[k] = v.count(word.lower())
        return counter


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
