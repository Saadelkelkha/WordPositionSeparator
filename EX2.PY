# Get user input for a word
mot = str(input("Type a word: "))

# Initialize empty strings for even and odd position characters
motp = ""  # String for characters at even positions
moti = ""  # String for characters at odd positions

# Iterate through each character in the word
for i in range(len(mot)):
    # Check if the index is even
    if i % 2 == 0:
        # Concatenate character to motp for even positions
        motp += mot[i]
    else:
        # Concatenate character to moti for odd positions
        moti += mot[i]

# Print characters at even positions
print("Characters at even positions:", motp)

# Print characters at odd positions
print("Characters at odd positions:", moti)
