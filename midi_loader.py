# for listing down the file names
import os
from midi_reader import read_midi

# Array Processing
import numpy as np

# specify the path
path = 'schubert/'

# read all the filenames
files = [i for i in os.listdir(path) if i.endswith(".mid")]

# reading each midi file
notes_array = np.array([read_midi(path + i) for i in files])

print(notes_array)

"""
    UNDERSTANDING THE DATA
"""
# converting 2D array into 1D array
notes_ = [element for note_ in notes_array for element in note_]

print(notes_)

# No. of unique notes
unique_notes = list(set(notes_))
print("unique")
print(len(unique_notes))

"""
    Notes Distribution
"""

# importing library
from collections import Counter

# computing frequency of each note
freq = dict(Counter(notes_))

# library for visualiation
import matplotlib.pyplot as plt

# consider only the frequencies
no = [count for _, count in freq.items()]


print(freq)


# set the figure size
plt.figure(figsize=(5, 5))

# plot
plt.hist(no)

plt.show()

""" note distribution"""
frequent_notes = [note_ for note_, count in freq.items() if count>=5]
print(len(frequent_notes))

new_music = []

for notes in notes_array:
    temp = []
    for note_ in notes:
        if note_ in frequent_notes:
            temp.append(note_)
    new_music.append(temp)


new_music = np.array(new_music)