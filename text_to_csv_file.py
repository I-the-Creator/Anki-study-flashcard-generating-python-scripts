import csv

# Open the text file
with open('test.txt', 'r') as file:
    data = file.read()

# Split the text into a list of individual questions and answers
qa_list = data.split('Question: ')[1:]

# Initialize an empty list to store the extracted Q&A pairs
qa_pairs = []

# Iterate through the list, extracting the question and answer from each item
for item in qa_list:
    question, answer = item.split('Answer: ')
    question = question.strip() # remove newlines before question
    answer = answer.strip() # remove newlines after answer
    qa_pairs.append([question, answer])

# Open a CSV file to write the Q&A pairs
with open('questions_answers.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Question', 'Answer'])
    writer.writerows(qa_pairs)
