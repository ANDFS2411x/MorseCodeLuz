from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Diccionario Morse
MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'}

def text_to_morse(text):
    return ' '.join(MORSE_CODE_DICT.get(letter.upper(), '') for letter in text)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        morse_code = text_to_morse(text)
        return render_template('index.html', morse_code=morse_code)
    return render_template('index.html', morse_code='')

if __name__ == '__main__':
    app.run(debug=True)
