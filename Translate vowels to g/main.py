def Translate(vowels):
    translation = ""
    for letter in vowels:
        if letter.lower( ) in "aeiou":
            if letter.isupper():
                translation +="G"
            else:
                translation +="g"
        else:
            translation += letter
    return translation
print(Translate(input("Enter a phrase: ")))