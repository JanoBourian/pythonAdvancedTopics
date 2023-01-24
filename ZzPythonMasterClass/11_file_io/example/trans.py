from translate import Translator


try:
    with open('test_to.txt', mode='r') as my_file:
        translator = Translator(to_lang="es")
        text = my_file.read()
        translation = translator.translate(text)
        with open('result.txt', mode='w') as result:
            result.write(translation)
except FileNotFoundError as err:
    print("Not Found!")
