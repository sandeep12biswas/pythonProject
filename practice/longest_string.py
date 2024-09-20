sample_story = '''Once upon a time, there was a beginner programmer named Alice who was eager to learn Python. She tried to learn from books, but found it difficult to grasp the concepts. One day, she stumbled upon an online course.
Alice was thrilled. The course was taught by a well-known programmer who made the lessons interesting and easy to understand. The course covered everything a beginner programmer needed, and Alice was finally able to understand how to code in Python.'''

longest_string = ''

for char in sample_story.split():
   # print(f"Length of {char} is {len(char)}")
    if len(longest_string) < len(char):
        longest_string = char


print(f"The longest string in this sentence is {longest_string}")