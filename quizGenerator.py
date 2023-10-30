import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'Kalifornia': 'Sacramento', 'Kolorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Floryda': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaje': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Luizjana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'Nowy Meksyk': 'Santa Fe', 'Nowy Jork': 'Albany', 'Karolina Północna':
'Raleigh', 'Dakota Północna': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma':
'Oklahoma City', 'Oregon': 'Salem', 'Pensylwania': 'Harrisburg',
'Rhode Island': 'Providence', 'Karolina Południowa': 'Columbia',
'Dakota Południowa': 'Pierre', 'Tennessee': 'Nashville', 'Teksas': 'Austin',
'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Wirginia': 'Richmond',
'Waszyngton': 'Olympia', 'Wirginia Zachodnia': 'Charleston', 'Wisconsin':
'Madison', 'Wyoming': 'Cheyenne'}
numberOfQuizes = 35
numberOfStates = 50
numberOfAnswers = 4
states = list(capitals.keys())
for quizNum in range(numberOfQuizes):
    #utworzenie quizow i odpowiedzi w pliku txt
    quizFile = open(f'capitalsquiz{quizNum+1}.txt', 'w')
    answerKeyFile = open(f'capitalsquiz_answers{quizNum+1}.txt', 'w')

    #zapis naglowków quizu
    quizFile.write('Imię i nazwisko:\n\nData:\n\nKlasa:\n\n')
    quizFile.write((' '*20) + f'Quiz stolic stanów (Quiz {quizNum+1})')
    quizFile.write('\n\n')

    #losowe ustalenie kolejnosci
    random.shuffle(states)

    #iteracja przez 50 stanów i przygotowanie odpowiedzi
    for questionNum in range(numberOfStates):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        #zapis pytań i odpowiedzi do pliku
        quizFile.write(f'{questionNum+1}. Co jest stolicą stanu {states[questionNum]}?\n')
        for i in range(numberOfAnswers):
            quizFile.write(f"   {'ABCD}'[i]}. {answerOptions[i]}\n")
        quizFile.write('\n')

        answerKeyFile.write(f"{questionNum + 1}."
                            f"{'ABCD'[answerOptions.index(correctAnswer)]} \n")
    quizFile.close()
    answerKeyFile.close()






