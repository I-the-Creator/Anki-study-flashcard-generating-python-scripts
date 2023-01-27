# import genanki
# import csv

# style = """
# /* Congratulations! It looks like you have decided to betray my style and play around with the styling of the css for your flashcards
# I have provided some examples of things you can do to change how they look below :) */
# .card {
#   font-family: Arial;
#   font-size: 20px;
#   text-align: center;
#   color: black;
#   background-color: white;
# }
# .something {
#   font-size: 70px;
#   margin-bottom: 0;
# }
# .something_else {
#   font-size: 16px;
#   color: gray;
#   margin-top: 0;
# }
# .something_definition_like {
#   color: blue;
# }
# """

# my_deck = genanki.Deck(2059400110, 'Physics_flashcards_25/1/22')

# my_model = genanki.Model(
#     1607392310,
#     'Simple Model',
#     fields=[
#         {'name': 'Question'},
#         {'name': 'Answer'},
#     ],
#     templates=[
#         {
#             'name': 'Card 1',
#             'qfmt': '<div class="question">{{Question}}</div>',
#             'afmt': '{{FrontSide}}<hr id="answer"><div class="answer">{{Answer}}</div>',
#         }
#     ],
#     css = style)

# with open('questions_answers.csv', newline='', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',', quotechar='"')
#     next(reader) # Skip the first row
#     for row in reader:
#         my_note = genanki.Note(model=my_model, fields=[row[0], row[1]])
#         my_deck.add_note(my_note)

# genanki.Package(my_deck).write_to_file('output.apkg')

import csv
import genanki

style = """
/* Congratulations! It looks like you have decided to betray my style and play around with the styling of the css for your flashcards
I have provided some examples of things you can do to change how they look below :) */
.card {
  font-family: Arial;
  font-size: 20px;
  text-align: center;
  color: black;
  background-color: white;
}
.something {
  font-size: 70px;
  margin-bottom: 0;
}
.something_else {
  font-size: 16px;
  color: gray;
  margin-top: 0;
}
.something_definition_like {
  color: blue;
}
"""

deck_name = "Physics_flashcards"
model_id = 1607392310 # replace with your model ID

# Open the existing deck
my_deck = genanki.Deck(model_id, deck_name)

my_model = genanki.Model(
    model_id,
    'Simple Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '<div class="question">{{Question}}</div>',
            'afmt': '{{FrontSide}}<hr id="answer"><div class="answer">{{Answer}}</div>',
        }
    ],
    css = style)

with open('questions_answers.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader) # Skip the first row
    for row in reader:
        my_note = genanki.Note(model=my_model, fields=[row[0], row[1]])
        my_deck.add_note(my_note)

# Create the Anki package and add the deck and media files
package = genanki.Package(my_deck)

# Write the package to a file
package.write_to_file('Physics_flashcards.apkg')
