# I made a hangman that uses Turtle to draw the picture. I originally tried to 
# make all of my Turtle-related functions in a separate file and import it into this
# file, but it told me that 'the module is unrecognizable', and the answers online didn't 
# make sense to me.

# When you lose, I want it to show you the answer. However, the word gets edited later on
# so that the program will check for all repeat letters. In line 121 I tried to have
# 'a nonmodified word' be the same as the word and print it again at the end on line 183

# The last thing I want to change is the long list of code starting on line 160
# for the different things to draw
# each time a life is lost. Is there a way to write it so that I don't have to manually write
# a separate action for each life?


import random
import turtle

# TURTLE SETTINGS
window = turtle.Screen()
pen = turtle.Turtle()
pen.speed(10)
pen.width(7)
pen.hideturtle()


class Draw:
    def hang_stand(self):
        pen.up()
        pen.right(90)
        pen.forward(200)
        pen.left(90)
        pen.down()
        pen.color('black')
        pen.forward(200)
        pen.right(180)
        pen.forward(100)
        pen.right(90)
        pen.forward(400)
        pen.left(90)
        pen.forward(200)
        pen.left(90)
        pen.forward(50)

    def head(self):
        pen.color('red')
        pen.right(90)
        for i in range(36):
            pen.forward(10)
            pen.left(10)

    def body(self):
        pen.up()
        pen.left(90)
        pen.forward(120)
        pen.down()
        pen.forward(150)

    def arm1(self):
        pen.left(180)
        pen.forward(125)
        pen.left(135)
        pen.forward(100)

    def arm2(self):
        pen.right(180)
        pen.forward(100)
        pen.right(90)
        pen.forward(100)

    def leg1(self):
        pen.left(180)
        pen.forward(100)
        pen.left(135)
        pen.forward(125)
        pen.right(180)
        pen.left(135)
        pen.forward(100)

    def leg2(self):
        pen.right(180)
        pen.forward(100)
        pen.right(90)
        pen.forward(100)


draw = Draw()


def __choose_word():
    word_bank = ['dodo bird', 'hammerhead', 'ratatouille', 'spell check', 'unicycle',
                 'ice cream', 'water bottle', 'australia', 'terminate']
    word = random.choice(word_bank)
    word = list(word)
    return word


def __replace_character(old_character, new_character, list1, list2):
    try:
        letter_position = list1.index(old_character)
        list2[letter_position] = new_character
        list2 = list(list2)
        return list2
    except ValueError:
        pass


def __check_special_characters(word, blanks):
    special_characters = [' ', "'", ".", ',']
    for character in special_characters:
        while character in word:
            __replace_character(character, character, word, blanks)
            letter_position = word.index(character)
            word[letter_position] = '#'


def guess_letter():
    draw.hang_stand()

    word = __choose_word()
    nonmodified_word = word
    blanks = "-" * len(word)
    blanks = list(blanks)

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    __check_special_characters(word, blanks)
    print(''.join(blanks))

    print("")
    print("To see what letters are still available, type 'options'.")

    life_count = 0
    while life_count != 6:

        # win condition
        try:
            blanks.index('-')
        except ValueError:
            print("")
            print("WINNER")
            break

        print("")
        print("Enter a letter.")
        guess = input("> ")

        if guess == 'options':
            print(''.join(alphabet))
        elif guess in alphabet:
            if guess in word:
                while guess in word:
                    __replace_character(guess, guess, word, blanks)
                    letter_position = word.index(guess)
                    word[letter_position] = '#'
                print(''.join(blanks))
            else:
                print(f"'{guess}' is not in word.")
                if life_count == 0:
                    draw.head()
                elif life_count == 1:
                    draw.body()
                elif life_count == 2:
                    draw.arm1()
                elif life_count == 3:
                    draw.arm2()
                elif life_count == 4:
                    draw.leg1()
                else:
                    draw.leg2()
                life_count += 1
                print(''.join(blanks))
            __replace_character(guess, '-', alphabet, alphabet)
        else:
            print("Non-valid input or re-used letter. Please enter a new letter.")
            print(''.join(blanks))

    # lose condition
    if life_count == 6:
        print("")
        print("GAME OVER")
        print(f"ANSWER: {nonmodified_word}")


guess_letter()
window.exitonclick()
