import tkinter as tk
import re

window = tk.Tk()
window.title("Typing test by Biobrick aka Jari Suomela")

TEST_TEXT = """The test will start when you press enter.
You have 60 seconds to type all this text or if you reach
the character lenght I mean the sum of all the characters the test will stop.
The current speed is the net speed of your typing in words per minute (WPM) 
Beware this text may have
spelling problems or grammatic errors since English is my second language. 
I did not even use spellcheck.
This is a typing test program made by Jari Suomela
I'm a Python coder and I would like to get work as Python programmer.
You can reach me by email: suomela.jari@gmail.com or visit my portfolio
at jarisuomelaportfolio.com."""

TEST_TEXT = " ".join(TEST_TEXT.split())


def nothing():
    pass


def start_the_test(event):
    if event.keysym == "Return":
        global count_down
        if count_down is False:
            count_down = True
            window.after(100, func=count)


def get_text_input(event):
    global last_character
    global typed_text

    if event.keysym == "Shift_R" or event.keysym == "Shift_L":
        pass
    else:
        if event.char == "\b":
            text = entry_id.get()
            text = text + event.char
            text = text[:-1]
            typed_text = typed_text[:-1]
            entry_id.delete(0, tk.END)
            try:
                entry_id.insert(0, typed_text[-13:])
            except Exception:
                entry_id.insert(0, typed_text)
            return typed_text
        else:
            text = entry_id.get()
            text = text + event.char
            text = text[:-1]
            text = " ".join(text.split())
            typed_text += event.char
            typed_text = " ".join(typed_text.split())
            entry_id.delete(0, tk.END)
            if event.char == " ":
                text = text + " "
                typed_text += " "

                if typed_text[0] == " ":
                    typed_text = typed_text[1:]

            try:
                entry_id.insert(0, typed_text[-13:])
            except Exception:
                entry_id.insert(0, typed_text)

            return typed_text


def count():
    global time
    global char_correct
    global characters_total
   
    entry_id.focus_set()
    time += 0.1
    time_in_seconds = time
    time_in_seconds = round(time_in_seconds, 2)
    chaching_clock.configure(text=time_in_seconds)
    id_for_count = window.after(100, func=count)
    any_key = window.bind("<Key>", func=get_typed_text)
    backspace_key = window.bind("<BackSpace>", func=get_typed_text)
    space_key = window.bind("<space>", func=get_typed_text)
    window.bind("Shift_L", func=nothing)
    window.bind("Shift_R", func=nothing)
    entry_id.configure(state="normal")
    speed = round(int(char_correct[0]) / 5 / (time_in_seconds / 60))
    display_current_speed.configure(text=f"The current speed is  {speed}")

    if len(TEST_TEXT) <= characters_total:
        time += 100

    if time_in_seconds >= 60:
        window.after_cancel(id_for_count)
        window.unbind("<Key>", any_key)
        window.unbind("<BackSpace>", backspace_key)
        window.unbind("<space>", space_key)
        entry_id.configure(state="readonly")
        char_correct = how_many_characters_correct["text"]
        char_correct = re.findall(r"\d+", char_correct)


def get_typed_text(event):
    """Gets typed text in the field and passes it to a label"""
    global char_correct
    global characters_total
    if event.keysym == "Shift_R" or event.keysym == "Shift_L":
        pass
    else:
        text = get_text_input(event)
        text_in_words = text.split(" ")
        if not text_in_words:
            text_in_words.append("")

        label_tk.configure(text=text)

        global current_word_text
        global list_of_words
        try:
            list_of_words = text.split(" ")
            current_word = len(list_of_words) - 1
            if event.char == " " and not text_in_words:
                current_word_text = TEST_TEXT.split(" ")[current_word + 1]
            else:
                current_word_text = TEST_TEXT.split(" ")[current_word]

            current_word_label.configure(text=current_word_text)
        except IndexError:
            pass

        try:
            check_spaces = text.count(" ")
            text_in_words = text + " "

            text_in_words = text_in_words.split(" ")
            words_to_be_checked = text_in_words
            list_of_words = TEST_TEXT.split(" ")
            count_for_correct = 0
            characters_total = len(text)
            chracters_correct = 0
            for i in range(0, len(text_in_words) - 1):
                if list_of_words[i] == words_to_be_checked[i]:
                    count_for_correct += 1
                    chracters_correct += len(list_of_words[i])
                else:
                    for key, char in enumerate(list_of_words[i]):
                        if key < len(words_to_be_checked[i]):
                            if char == words_to_be_checked[i][key]:
                                chracters_correct += 1

        except IndexError:
            pass
        if len(text) > 1:
            chracters_correct += check_spaces
        how_many_correct.configure(text=f"Total words correct {count_for_correct}")
        how_many_total_characters.configure(text=f"Total character {characters_total}")
        how_many_characters_correct.configure(
            text=f"Total characters correct {chracters_correct}"
        )
        char_correct = how_many_characters_correct["text"]
        char_correct = re.findall(r"\d+", char_correct)


time = 0
count_down = False
current_word_text = 0
last_character = ""
typed_text = ""
char_correct = [
    0,
]
characters_total = 0
window.geometry("1000x1000")
window.config(background="skyblue")
chaching_clock = tk.Label(text="Clock", font=("Arial", 20), background="skyblue")
chaching_clock.pack()
test_label_text = tk.Label(
    text=TEST_TEXT, wraplength="750", font=("Arial", 20), background="skyblue"
)
test_label_text.pack()
entry_id = tk.Entry(font=("Arial", "25"), background="skyblue")
entry_id.pack()

list_of_words = TEST_TEXT.split(" ")

current_word_label = tk.Label(
    text=list_of_words[0], font=("Arial", 25), background="skyblue"
)
current_word_label.pack()

how_many_correct = tk.Label(
    text="Total words correct 0", font=("Arial", 20), background="skyblue"
)
how_many_correct.pack()


how_many_characters_correct = tk.Label(
    text="Total characters correct 0", font=("Arial", 20), background="skyblue"
)
how_many_total_characters = tk.Label(
    text="Total characters 0", font=("Arial", 20), background="skyblue"
)
how_many_characters_correct.pack()
how_many_total_characters.pack()

window.bind("<Return>", func=start_the_test)
display_current_speed = tk.Label(
    text="The current speed is 0", font=("Arial", 20), background="skyblue"
)
display_current_speed.pack()

entry_id.configure(state="readonly")
label_tk = tk.Label(
    text="Written text", wraplength="750", font=("Arial", 20), background="skyblue"
)
label_tk.pack()


window.mainloop()
