#-------------------------Disruptive Data Summer School-------------------------#
#------------------------Script for Project 4 resolution------------------------#
#----------------------------Author: Francesco Fabbi----------------------------#

#First of all, we need to open the file of interest, in reading mode, in order
#to get all the words within
file = open('Words - Foglio1.csv', 'r')
word_list = file.readlines() #This method returns a list of all the words
print("List of words (original):", '\n', word_list)
print('\n')
#We now sort this list because we want to reorder the words from A to Z (crescent alphabetical way). However, we want to do it in an insensitive case way!
#That's why we add the "key" value in the function "sort()", to let it perform comparisons between the all lower-cases for the words contained in the list
word_list.sort(key = str.lower)

file.close()                 #File is closed, since we don't need it anymore
print("List of words (modified):", '\n', word_list)
print('\n')
filew = open('Words Reorganized.csv', 'w') #This is the new file we're going to create
num_words = len(word_list)                 #Variable to count the number of words in file
total_words_length = 0                     #Variable useful to calculate the average length
for el in word_list:                       #Inside this "for cycle", we write the new file and evaluate the total words length
    
#It's important to stress out the fact that the last world in the original file doesn't contain the return character '\n'. Therefore, in order to not obtain
#two concatenated words in the new file, we have to add the return character when we write that particular word
    if not '\n' in el:
        filew.write(el+'\n')               
        total_words_length += len(el)
    else:
        filew.write(el)
#All the words in the list we defined at the beginning have the return character '\n' which we do not consider in the average word length computation
        total_words_length += len(el)-1
        
#Now we can close the new file because the writing process is completed, and return the number of words and the average word length
filew.close()                               
print("Num of words: ", num_words, '\n')
print("Average words length (not considering return character): ", total_words_length/num_words, "  Approximated: ", int(total_words_length/num_words), '\n')
print("Check the file 'Words Reorganized.csv' to evaluate the result of the writing process")
