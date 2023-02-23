import translate

# Creating an example file
with open("text.txt", mode="w") as file:
    file.write("Hello world. I love python!")

# Printing translation to Japanese
with open("text.txt") as file:
    translator = translate.Translator(to_lang="ja")
    translation = translator.translate(file.read())
    print(translation)
    with open("translation.txt", mode="w") as trans_file:
        trans_file.write(translation)