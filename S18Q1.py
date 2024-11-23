import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

def remove_stop_words(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        passage = file.read()

    stop_words = set(stopwords.words('english'))
    words = word_tokenize(passage)

    filtered_words = [word for word in words if word.lower() not in stop_words]

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(" ".join(filtered_words))

if __name__ == "__main__":
    input_file = "input.txt"  # Replace with the path to your input text file
    output_file = "output.txt"  # Replace with the desired output file path

    remove_stop_words(input_file, output_file)
