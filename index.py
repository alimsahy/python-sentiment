negations = ["not", "no", "don't", "didn't", "wasn't", "weren't", "can't",
             "couldn't", "isn't", "aren't", "haven't", "hasn't", "hadn't"]
# The list of punctuations to trim punctuations from words

punctuations = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

afinnFile = open("AFINN-en-165.txt")
scores = {}

for line in afinnFile:
    term, score = line.split('\t')
    scores[term] = int(score)

afinnFile.close()
sentence = input("Enter sentence: ")
split = sentence.split(' ')

total_polarity = 0
output_sentence = ""
nextPositive = False

for eachWord in split:
    if eachWord.strip(punctuations) in scores:
        if nextPositive:
            if int(scores[eachWord.strip(punctuations)]) < 0:
                total_polarity = int(total_polarity) + abs(int(scores[eachWord.strip(punctuations)]))
                nextPositive = False
                eachWord = eachWord.upper()
                output_sentence = output_sentence + eachWord + " "
            else:
                total_polarity = int(total_polarity) - abs(int(scores[eachWord.strip(punctuations)]))
                nextPositive = False
                eachWord = eachWord.upper()
                output_sentence = output_sentence + eachWord + " "
        else:
            total_polarity = int(total_polarity) + int(scores[eachWord.strip(punctuations)])
            eachWord = eachWord.upper()
            output_sentence = output_sentence + eachWord + " "
    else:
        if eachWord in negations:
            nextPositive = True
            eachWord = eachWord.upper()
            output_sentence = output_sentence + eachWord + " "
        else:
            output_sentence = output_sentence + eachWord + " "


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

print(output_sentence)
print(total_polarity)

