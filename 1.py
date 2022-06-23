#你的python代码
import fileinput
import eng_to_ipa as p 
import pyttsx3

engine = pyttsx3.init()
print("Please put your sentences in data.txt line by line.")
for line in fileinput.input(files =('data.txt')):
    if line[0] != '-':
        sentence = line.split('.')[0]
        phonetics = p.convert(sentence)
        print(sentence)
        print(phonetics)
        engine.say(sentence)
        engine.runAndWait()
        a = input(".....................................................Press Enter")
        continue
