from time import sleep
import telebot
from telebot import types

token = '845897790:AAHH8UAvEhdUecQTi4bXuNpIdcaZ1nkXbRc'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(m):

    msg = bot.send_message(m.chat.id, "Привіт це текстовий квест від ЧДТУ: 'Підземелля'")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Почати гру!']])

    bot.send_message(m.chat.id, "Уявіть, що Ви - археолог. Під час розкопок давньої піраміди "
                                "Ви провалилися під піщані дюни і опинились в підземеллі "
                                "самої піраміди.",
                     reply_markup=keyboard)
    bot.register_next_step_handler(msg, second)




def second(m):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Тобі потрібно вибратись звідси")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Зрозуміло']])
        bot.send_message(m.chat.id, 'Ти це людина яка провалилась',
                         reply_markup=keyboard)

        bot.register_next_step_handler(msg, third)



def third(m):

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Вдалої пригоди і пам'ятайте ви повинні вижити")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Направо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Прямо']])
        bot.send_message(m.chat.id, 'Перед тобою коридор. Обери куди йти',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, fourth)



def fourth(m):
    if m.text == 'Направо':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Ти зустрічаєш дивне роздоріжжя")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Направо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Йти далі']])
        bot.send_message(m.chat.id, 'Куди краще піти?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, fourth_right)

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Дорога підіймається")
        sleep(1)
        bot.send_message(m.chat.id, "О так це підйом")
        sleep(1)
        bot.send_message(m.chat.id, "Але можна піти далі і по коридору")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Краще іти по коридору']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Я краще піду по підйому']])
        bot.send_message(m.chat.id, 'Куди краще піти?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, direct)


def fourth_right(m):
    if m.text == 'Йти далі':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "На стіні дуже дивна цеглина. А ні, це кнопка.")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Натиснути']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Йти далі по коридору']])
        bot.send_message(m.chat.id, 'Як гадаєш, натиснути?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, fourth_right_1)

    elif m.text == 'Направо':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Ви попали знов  в початковy точку підземелля")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Направо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Прямо']])
        bot.send_message(m.chat.id, 'Куди мені іти?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, fourth)


def fourth_right_1(m):
    if m.text == 'Натиснути':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "О ні! Нажаль на вас впали блоки")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Почати заново']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in
                       ['Тут ссилка на квест']])
        bot.send_message(m.chat.id, 'Ви можете пройти квест заново або спробувати його в реальному житті',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, start)

    elif m.text == 'Йти далі по коридору':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Далі багато води  але попереду сходинки")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Пливти']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Краще піти на сходинки']])
        bot.send_message(m.chat.id, 'Шо робити?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, fourth_right_2)


# НАПИСАТЬ ФУНКЦІЮ ТА ШО ДО СХОДИНОК
def fourth_right_2(m):
    if m.text == 'Краще піти на сходинки':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Багато води. Видно дно")
        sleep(1)
        bot.send_message(m.chat.id, "Там глибоко")
        sleep(2)
        bot.send_message(m.chat.id, "Здається попереду світло")
        sleep(1)
        bot.send_message(m.chat.id, "І видно невеликий отвір")
        sleep(2)
        bot.send_message(m.chat.id, "Може це вихід?")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Піти далі']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Залізти в отвір']])
        bot.send_message(m.chat.id, 'Спробувати пролізти?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, direct_windows_and_go_one)  # функція вікна



    elif m.text == 'Пливти':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Вас зїли піранії")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Почати заново']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Тут ссилка на квест']])
        bot.send_message(m.chat.id, 'Ви можете пройти квест заново або спробувати його в реальному житті',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, start)


# ТУТ ЗАКІНЧЦЄТЬСЯ ВСІ ФУНКЦІЇ ЯКІ ВЕДУТЬ НА ПРАВО

def direct(m):
    if m.text == 'Я краще піду по підйому':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Далі багато води  але видно сходинки")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Пливти']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Краще піти на сходинки']])
        bot.send_message(m.chat.id, 'Шо мені робить?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, fourth_right_2)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "З дальніх стін видніється світло")
        sleep(1)
        bot.send_message(m.chat.id, "А попереду двері")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Відкрити двері']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Іти на світло']])
        bot.send_message(m.chat.id, 'Що ж обрати?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, direct_door)


def direct_door(m):
    if m.text == 'Відкрити двері':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Перед нами сходинки і маленьке отвір")
        sleep(1)
        bot.send_message(m.chat.id, "Але в нього можна пролізти")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Залізти в отвір']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Просто пройти далі']])
        bot.send_message(m.chat.id, 'Куди ти хочеш іти?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, direct_windows)  # функція нва одному рівні з вікном

    elif m.text == 'Іти на світло':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Перед тобою хитка стінка з цегли")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Звалити її']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Краще пошукати інший вихід']])
        bot.send_message(m.chat.id, 'Але за нею видно якесь світло',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, direct_wall)

def direct_wall(m): # тут можна дописать якшо в тебе є ломік це продумать треба
    if m.text == 'Звалити її':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Ти бачиш перед собою в темноті щось схоже на гробницю")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Підійти']])
        bot.send_message(m.chat.id, 'В кінці щось видніється',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, direct_windows)

    elif m.text == 'Краще пошукати інший вихід':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Але далі просто стіна і немає нічого ")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Звалити']])
        bot.send_message(m.chat.id, 'Прийдеться звалити стіну',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, direct_windows)


def direct_windows(m):
    if m.text == 'Піти далі':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Ти бачиш перед собою в темноті щось схоже на гробницю")
        sleep(2)
        bot.send_message(m.chat.id, "На ньому є якийсь напис")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Підійти']])
        bot.send_message(m.chat.id, 'В кінці щось видніється',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, direct_code_lock)

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Ти бачиш перед собою кодовий замок з екраном")
        sleep(1)
        bot.send_message(m.chat.id, "На ньому є якийсь напис")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Тутанхамона']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Рамзеса 1']])
        bot.send_message(m.chat.id, 'Гробницю якого фараона знайшли не розкраденою в 1922 році',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, direct_code_lock)


def direct_windows_and_go_one(m):
    if m.text == 'Піти далі':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Хмм що це?")
        sleep(1)
        bot.send_message(m.chat.id, "Здається замок")
        sleep(2)
        bot.send_message(m.chat.id, "О так тут є якийсь код")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Попробувать розгадати код']])
        bot.send_message(m.chat.id, 'Треба розгадати код',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, direct_windows)

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Хмм що це?")
        sleep(1)
        bot.send_message(m.chat.id, "Здається замок")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Попробувать ввести код']])
        bot.send_message(m.chat.id, 'О так тут є якийсь код',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, direct_windows)


def direct_code_lock(m):
    if m.text == 'Тутанхамона':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Вітаю ви залишились живі")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Почати заново']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Тут ссилка на квест']])
        bot.send_message(m.chat.id, 'Пройти квест заново чи можливо хочете записатись на реальний квест?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, start)

    elif m.text == 'Рамзеса 1':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Нажаль ви відповіли не правильно")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Почати заново']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Тут ссилка на квест']])
        bot.send_message(m.chat.id, 'Почати квест заново чи можливо хочете записатись на реальний квест?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, start)


if __name__ == "__main__":
    bot.polling(none_stop=True)
