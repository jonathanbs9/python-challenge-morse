morse_code = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", 
    "g": "--.", "h": "....", "i": "..", "j": "·---", "k": "-.-", "l": ".-..", 
    "m": "--", "n": "-.", "ñ": "--.--", "o": "---", "p": ".__.", "q": "--.-",
    "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
    "x": "-..-", "y": "-.--", "z": "--..",
    
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", 
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    
    ".": ".-.-.-", ",": "-.-.--", "?": "..--..", "\"": ".-..-."
}
text_codified = ""
word = input("Ingrese una palabra o texto a codificar: ")
for c in word:
    if c != " " and c.lower() in morse_code:
        text_codified += morse_code[c.lower()]+ " "
    else:
        text_codified += c
    
print("Texto codificado: {}".format(text_codified))