student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()

#TODO 1. Create a dictionary in this format:
df = pandas.read_csv("nato_phonetic_alphabet.csv")
# for (index, row) in df.iterrows():
#     print(row.letter)
dict = {row.letter:row.code for (index, row) in df.iterrows()}
print(dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

sentance = input("whats the word you would like to spell out: ")
list_sentance = list(sentance)
# list = []
#
# for letter in list_sentance:
list = [row.code for letter in list_sentance for (index, row) in df.iterrows() if row.letter == letter.upper() ]
#list = [row.code for letter in list_sentance if row.letter == letter]
print(f"Your spelling is: \n{list}")