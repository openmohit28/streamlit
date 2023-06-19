# This is a sample Python script.
import streamlit


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def run(**kwargs):
    _input = streamlit.slider("Pick a number", min_value=10, max_value=100, value=20, step=10)
    print(_input)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
