import sys

def makeCypher(encriptedWord, testWord, cypher):
    for i in range(len(encriptedWord)):
        if encriptedWord[i] in cypher.keys():
            if cypher[encriptedWord[i]] != testWord[i]:
                return False
        else:
            cypher[encriptedWord[i]] = testWord[i]
    return True

def generateLists(inpFile):
    words = []
    with open(inpFile) as fl:
        for i in range(int(fl.readline().strip())):
            words.append(fl.readline().strip())
        for i in fl:
            codedWords = i.strip().split()
    return words, codedWords

def decrypt(words, codedWords, cypher):
    codedWords.sort(key=len, reverse=True)
    for cw in codedWords:
        lenCw = len(cw)
        possibleWords = filter(lambda x: len(x) == lenCw, words)
        if len(possibleWords) == 0:
            raise Exception("Dictionary incomplete, encripted word {0} has no equivalent word size on dictionary".format(cw))
        for pw in possibleWords:
            if makeCypher(cw,pw,cypher):
                print "Cypher Ok so far"
            else:
                print "Cypher Failed"

def main(args):
    cypher = {}
    words, codedWords = generateLists(args[0])
#    words = ["blue", "one", "origin"]
#    codedWords = ["abdn"]
    decrypt(words, codedWords, cypher)
    print cypher

if __name__ == "__main__":
    main(sys.argv[1:])
