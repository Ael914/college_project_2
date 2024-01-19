import requests


def create_titles_and_markup_by_data(data:list):
    from telebot.types import ReplyKeyboardMarkup,KeyboardButton
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    titles = [el['title'] for el in data]
    for title in titles:
        markup.add(KeyboardButton(title))
    return (titles, markup)	
def get_subjects():
    data = requests.get("ru/api/subjects/").json()
    return create_titles_and_markup_by_data(data)
def get_courses():
    data = requests.get("ru/api/courses/").json()
    return create_titles_and_markup_by_data(data)