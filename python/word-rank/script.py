# coding=utf-8

# input: array with multiple strings
# expected output: rank of the 3 most often repeated words in given set of strings and number of times they occured, case insensitive

sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

# Example result:
# 1. "mam" - 12
# 2. "tak" - 5
# 3. "z" - 2


def countWords(sentences, howMany):
    wordDict = {}
    i = 0

    for sentence in sentences:
        sentence = sentence.lower().replace(',', '').replace('.', '').replace('?', '').replace('!', '').split()
        for word in set(sentence):
            wordDict.update({word: wordDict.get(word)+sentence.count(word) if wordDict.get(word) else sentence.count(word)})

    for word in sorted(wordDict.items(), key=lambda x: x[1], reverse=True):
        i += 1
        print(f'{i}. {word[0]} - {word[1]}')
        if i == howMany:
            break
    return wordDict


countWords(sentences, 3)
