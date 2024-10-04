from translate import Translator

translator = Translator(to_lang='ja')
try:
    with open('Original_Text.txt', mode='r') as file:
        text = file.read()
        translation = translator.translate(text)
        with open('Translated_Text.txt', mode='w',encoding='utf-8') as file2:
            file2.write(translation)
except FileNotFoundError as err:
    print('File not found...')
