# I made a hangman that uses Turtle to draw the picture. I originally tried to 
# make all of my Turtle-related functions in a separate file and import it into this
# file, but it told me that 'the module is unrecognizable', and the answers online didn't 
# make sense to me.
# Mark: Hmm, if you try again and upload what doesn't work I can help you troubleshoot.

# When you lose, I want it to show you the answer. However, the word gets edited later on
# so that the program will check for all repeat letters. In line 121 I tried to have
# 'a nonmodified word' be the same as the word and print it again at the end on line 183
# Mark: See below for the fix

# The last thing I want to change is the long list of code starting on line 160
# for the different things to draw
# each time a life is lost. Is there a way to write it so that I don't have to manually write
# a separate action for each life?
# Mark: See below


import random
import turtle

# TURTLE SETTINGS
window = turtle.Screen()
pen = turtle.Turtle()
pen.speed(10)
pen.width(7)
pen.hideturtle()


class Draw:
    # If you're using PyCharm you might be seeing a warning here that says
    # "method 'hang_stand' may be 'static'". This is because the methods
    # defined here don't actually depend on the Draw instance. That is,
    # if you defined
    #
    # draw1 = Draw()
    # draw2 = Draw()
    #
    # and then called
    # draw1.hang_stand()
    # draw2.hang_stand()
    #
    # They would have the exact same result every single time because the
    # instance "draw1" versus "draw2" doesn't affect the functions. Therefore,
    # you can actually remove "self" from all of the functions in this class
    # which would make them "static". All "static" means is that they're *always
    # intialized* so you could call
    # Draw.hang_stand() without defining a Draw() instance at all.
    # Note: Having static methods isn't a bad thing! It still makes sense to organize
    # all of these functions under the Draw class since they share similar functionality,
    # they just don't depend on the instance. If you wanted to make them depend on
    # the instance and non-static you could add a "init" method (which allows classes
    # to take in "initialization" arguments) like
    #
    # def __init__(self, pen_color):
    #   self.pen_color = pen_color
    #
    # Then in the other methods, e.g. hang_stand you could do
    # def hang_stand(self):
    #   ...
    #   pen.color(self.pen_color)
    #   ...
    #
    # Then the hang_stand method wouldn't be static and *would* depend on an instance of
    # Draw() because it needs self.pen_color to be defined before it can be called.

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

# Unless I'm mistaken this is only called in the guess_letter
# function, so instead of defining draw as a global variable
# you could just have guess_letter take in a Draw() instance
# as an argument
draw = Draw()


# Yay! I like you followed conventions with the underscores to "hide" functions
# from users :D
def __choose_word():
    word_bank = ['dodo bird', 'hammerhead', 'ratatouille', 'spell check', 'unicycle',
                 'ice cream', 'water bottle', 'australia', 'terminate']
    # You can combine this into a single line. It's still readable enough
    word = list(random.choice(word_bank))
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

    # This fixes your problem with the answer getting corrupted/messed up
    # When you wrap word in list() you're actually creating a new list that's
    # an exact copy of word. When you only use "nonmodified_word = word"
    # what you're really saying is "I want this variable 'nonmodified_word'
    # to point to the *memory location* word. This means you modify 'word'
    # later, *you're also modifying 'nonmodified_word'*. By using list(),
    # you say "I want variable 'nonmodified_word' to have the same contents
    # that are stored in the memory location assigned to 'word', but copy them
    # into their own memory space.
    nonmodified_word = list(word)
    # The way you defined blanks is actually perfectly fine, but
    # if you wanted to use a "list comprehension" (shorthand for
    # defining lists) [https://www.pythonforbeginners.com/basics/list-comprehensions-in-python]
    # we could write this:
    blanks = ["-" for character in word]
    # I don't think I mentioned this, but you can think of strings
    # in Python really as just "lists of characters". In fact, many
    # operations you perform on lists are also perfectly valid on strings.
    # In the list comprehension above, we iterate through each character in
    # "word" and for each character we put "-" in our new list "blanks."

    # blanks = "-" * len(word)
    # blanks = list(blanks)

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    __check_special_characters(word, blanks)
    print(''.join(blanks))

    print("\nTo see what letters are still available, type 'options'.")

    # *Very very extremely minor nitpick*, but I think it would make more
    # sense to count down if you're going to use "life" terminlogy lol
    # If you used "incorrect_guesses" then that would make sense to count up
    life_count = 0
    while life_count != 6:

        # win condition
        try:
            blanks.index('-')
        except ValueError:
            print("\nWINNER")
            break

        print("\nEnter a letter.")
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

                # I think the way you set up the different actions
                # is already the best and most logical approach. It's tedious
                # for the programmer, but it's clear and immediately obvious
                # what's happening. You should almost always prefer simplicity
                # even if it's slightly more verbose.
                # There are definitely clever/hacky ways you could make it more
                # concise, but that would be unecessary and probably less efficient
                # computationally

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
        # The special character \n inserts a "new line." So if we insert
        # it at the beginning of our string "GAME OVER" will be printed
        # with a space above it and we don't need the print("")
        print("\nGAME OVER")
        print(f"ANSWER: {nonmodified_word}")


guess_letter()
window.exitonclick()
