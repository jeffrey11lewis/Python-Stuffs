print('Enter a list of words:')
def buildDictionary(words):



    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return frequencies

if __name__ == '__main__':
    words = input().split()
    your_dictionary = buildDictionary(words)
    sorted_keys = sorted(your_dictionary.keys())
    for key in sorted_keys:
        print(key + ': ' + str(your_dictionary[key]))

