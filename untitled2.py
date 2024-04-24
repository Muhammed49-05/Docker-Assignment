import nltk
from nltk.corpus import stopwords
from collections import Counter

# Step 1: Read the contents of the "random_paragraphs.txt" file
file_path = r"C:\Users\Eng Gamal\Documents\paragraphs.txt"
with open(file_path, "r") as file:
    text = file.read()

# Step 2: Remove stop words from the text
nltk.download('stopwords')
stop_words = set(stopwords.words("english"))
words = nltk.word_tokenize(text)
filtered_words = [word for word in words if word.lower() not in stop_words]

# Step 3: Count the frequency of each word in the processed text
word_frequency = Counter(filtered_words)

# Step 4: Display the word frequency count to the console
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")
