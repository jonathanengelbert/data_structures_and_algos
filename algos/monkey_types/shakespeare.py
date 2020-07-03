import string
import random

def generate_phrase(strLen):
   characters = string.ascii_lowercase + ' '
   res = ''
   for i in range(strLen):
      res += characters[random.randrange(27)]
   return res

def score_phrase(phrase, target):
    if len(phrase) != len(target):
        print('THE INPUT PHRASES HAVE DIFFERENT LENGTHS. THEY WILL NEVER MATCH')
        return
    score = 0
    i = 0

    while i < len(target):
        if phrase[i] == target[i]:
            score += 1
        i += 1

    return score

def monkeyTypes():
    best_score = 0
    best_phrase = ''
    i = 0
    while best_score  != 28:
        monkey_output = generate_phrase(28)
        current_score = score_phrase(monkey_output, 'methinks it is like a weasel')

        i += 1
        if current_score > best_score:
            best_score = current_score
            best_phrase = monkey_output


            accuracy_rate = (best_score / 28) * 100
            print("THE BEST PHRASE IS: ", best_phrase)
            print("THE BEST SCORE IS: ", best_score, " OR {accuracy_rate}".format(accuracy_rate = accuracy_rate))
            print("OUT OF {iteration} ITERATIONS".format(iteration = i))
            print('ITERATION {i}'.format(i=i))

    print('It took {iterations} to find the string'.format(iterations = i) )

monkeyTypes()



