import random
import pyttsx3
import time

speak = pyttsx3.init()
engine = pyttsx3.init()
speak.say("choose language")
speak.runAndWait()
hebrew = 5
english = 1
language = input("language( hebrew or english ): ")


if language == "hebrew":
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[5].id)

    # hello
    hello = ["שלום שלום שלום",
             "שלום, חברה ",
             "מה קורה, אני כאן",
             "היי"]
    random1 = random.randrange(0, len(hello))
    speak.say(hello[random1])
    speak.runAndWait()

    # what you love to eat
    lovedfood = ["מהו, האוכל שהכי, אהוב, אליך",
                 "ספר לי, מה אתה, אוהב לאכול ",
                 "מהו, המאכל, שאתה, לא יכול, לחיות, בלדיו",
                 "האם יש, לך, מאכל, אהוב, אם כן, מהו"]
    random2 = random.randrange(0, len(lovedfood))
    engine.say(lovedfood[random2])
    engine.runAndWait()

    food_input = input(lovedfood[random2])

    engine.say(food_input + ", זה הכי, טוב")
    engine.runAndWait()

    engine.say("רוצה לשחק, ב״לגלות מספרים״")
    engine.runAndWait()

    yesno = input("yes or no")
    if yesno == "yes":
        play = random.randrange(0, 10)
        while 1:


            engine.say("מהו המספר שלך:")
            engine.runAndWait()
            number = int(input("המספר שלך: "))

            if number == play:
                engine.say("נכון!, כל הכבוד")
            engine.runAndWait()

            if number < play:
                engine.say("המספר, שכתבתה, קטן, מדי")
            engine.runAndWait()

            if number > play:
                engine.say("המספר, שכתבתה, גדול, מדי")
            engine.runAndWait()













if language == "english":
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)


# hello
    hello = ["hello im, ai, madded, by, ran2k",
         "hello my dear friends",
         "hi hi hi",
         "whatsapp"]
    random1 = random.randrange(0, len(hello))
    speak.say(hello[random1])
    speak.runAndWait()


# what you love to eat
    lovedfood = ["what you love, to eat?",
             "tell me, about, you, feeding",
             "what, you, loved, food",
             "what, is, your, loved, food"]
    random2 = random.randrange(0, len(lovedfood))
    engine.say(lovedfood[random2])
    engine.runAndWait()

    food_input = input(lovedfood[random2])

    engine.say(food_input + ", is the best")
    engine.runAndWait()

    engine.say("Want to  play the digits?")
    engine.runAndWait()

    yesno = input("yes or no :")
    if yesno == "yes":
        play = random.randrange(0, 10)
        while 1:

            engine.say("what is your number:")
            engine.runAndWait()
            number = int(input("You number: "))

            if number < play:
                engine.say("you number is too small")
            engine.runAndWait()

            if number > play:
                engine.say("you number is too hight")
            engine.runAndWait()

            if number == play:
                engine.say("you guess it")
                play = random.randrange(0, 10)
        engine.runAndWait()







