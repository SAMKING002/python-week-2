# Create input.txt with sample content
with open("input.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("Here is the second line.\n")
    file.write("The third line contains more words.\n")
    file.write("Fourth line is also here.\n")
    file.write("Finally, the fifth line wraps it up.\n")

# Read the contents of input.txt
with open("input.txt", "r") as file:
    content = file.read()

# Count the number of words
word_count = len(content.split())

# Convert text to uppercase
uppercase_content = content.upper()

# Write to output.txt
with open("output.txt", "w") as output_file:
    output_file.write(uppercase_content)
    output_file.write(f"\n\nTotal word count: {word_count}")

# Print success message
print("Processing complete. 'output.txt' has been created successfully.")
