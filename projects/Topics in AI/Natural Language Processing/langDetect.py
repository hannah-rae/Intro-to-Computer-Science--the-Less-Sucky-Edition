import nltk
from nltk.corpus import stopwords

def scoreFunction(wholetext):
    """Get text, find most common words and compare with known
    stopwords. Return dictionary of values"""

    langStopwords = {}
    scorelist = {}

    # These are the available languages with stopwords from NLTK
    NLTKlanguages=["dutch","finnish","german","italian",
    "portuguese","spanish","turkish","danish","english",
    "french","hungarian","norwegian","russian","swedish"]

    # Fill the dictionary of languages, to avoid  unnecessary function calls
    for lang in NLTKlanguages:
        langStopwords[lang] = stopwords.words(lang)

    # Split all the text in tokens and convert to lowercase.
    tokens = nltk.tokenize.word_tokenize(wholetext)
    for t in tokens:
        t = t.lower()

    # Determine the frequency distribution of words, looking for the
    # most common words
    freq_dist = nltk.FreqDist(tokens)

    # This is the only interesting piece, and not by much. Pick a
    # language, and check if each of the 20 most common words is in
    # the language stopwords. If it's there, add 1 to this language
    # for each word matched. So the maximal score is 20. Why 20? No
    # specific reason, looks like a good number of words.
    for lang in NLTKlanguages:
        scorelist[lang] = 0
        for word in freq_dist.keys()[0:20]:
            if word in langStopwords[lang]:
                scorelist[lang] += 1
    return scorelist

def whichLanguage(scorelist):
    """This function just returns the language name, from a given
    "scorelist" dictionary as defined above."""
    maximum = 0
    for item in scorelist:
        value = scorelist[item]
        if maximum < value:
            maximum = value
            lang = item
    return lang

while (True):
    text = raw_input("Enter some text, and I'll tell you the language.\n")
    scores = scoreFunction(text)
    print whichLanguage(scores)
