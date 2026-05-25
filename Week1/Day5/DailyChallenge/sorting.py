# Challenge 1 : Sorting


# Instructions
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension

sentence = input("suite de mot : ")

list_sentence = sentence.split(',')

o_list_sentence = sorted(list_sentence)

res = ",".join(o_list_sentence)

print(res)

