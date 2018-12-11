from chatterbot import ChatBot
from tkinter import *
import time
import os
from chatterbot.trainers import ListTrainer



bot = ChatBot(
"Chatter Bot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    input_adapter='chatterbot.input.VariableInputTypeAdapter',
    output_adapter='chatterbot.output.OutputAdapter',
    database='../database.db',
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": "chatterbot.response_selection.get_first_response"
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.6,
            'default_response': 'Sorry, I do not undetstand.'
        }
    ],
    trainer='chatterbot.trainers.ListTrainer'
)


#for files in os.listdir('data/english/'):
#	data = open('data/english/' + files, 'r').readlines()
#	bot.train(data)

for file in os.listdir('data/sopd/'):
    data = open('data/sopd/' + file, 'r').readlines()
    bot.train(data)


def command():
    global answer
    user_input = input.get()
    response = bot.get_response(user_input)
    answer['text']=str(response.text)


screen = Tk()
menu = StringVar()

screen.geometry('1280x640')
screen.title('Chatterbot')

title = Label(screen,text='COMP5511 AI Chatterbot')
title.pack()

input = Entry(screen,textvariable=menu)
input.pack()



bottone = Button(screen,text='Talk to Me!',command=command)
bottone.pack()

answer = Label(screen, text="")
answer.pack()

screen.mainloop()