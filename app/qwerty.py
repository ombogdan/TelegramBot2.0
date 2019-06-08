from time import sleep
import telebot
from telebot import types

token = '817354541:AAHixzjqjSQeRiEPX_04dP7ONoirjT9RfXk'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(m):
    msg = bot.send_message(m.chat.id, "Привіт")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Почати гру!']])

    bot.send_message(m.chat.id, "Уявіть, що ви - археолог. Під час розкопок давньої піраміди "
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
        msg = bot.send_message(m.chat.id, "Тут добавить ше якийсь текст")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Направо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Прямо']])
        bot.send_message(m.chat.id, 'Перед тобою коридор. Обери куди йти',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, fourth)



def fourth(m):
    if m.text == 'Направо':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Тут буде якийсь текст")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Направо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Йти далі']])
        bot.send_message(m.chat.id, 'Ти попав на роздоріжжя іти прямо чи на право',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, fourth_right)

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Ви в коридорі Зустрічаєте невеликий підйом")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Краще іти по коридору']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Я краще піду по підйому']])
        bot.send_message(m.chat.id, 'Будете іти по підйому чи прямо по коридору?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, direct)


def fourth_right(m):
    if m.text == 'Йти далі':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Ми йдем зустрычаэм кнопку всы дыла")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Натиснути']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Йти далі по коридору']])
        bot.send_message(m.chat.id, 'Нажать кнопку чи іти через затоплений коридор?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, fourth_right_1)

    elif m.text == 'Направо':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Ви попали знов  в початковy точку підземелля")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Направо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Прямо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['На ліво хз чи правильно написав']])
        bot.send_message(m.chat.id, 'Куди мені іти?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, fourth)


def fourth_right_1(m):
    if m.text == 'Натиснути':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Нажаль при натисненні на вас впали блоки і вам капець")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Почати заново']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in
                       ['Тут треба добавить ссилку дьоми ы текст записатись на реальний квест']])
        bot.send_message(m.chat.id, 'Ви можете пройти квест заново або спробувати його в реальному житті',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, start)

    elif m.text == 'Йти далі по коридору':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Далі багато води  але зустрічаєте сходинки")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Пливти']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Краще піти на сходинки']])
        bot.send_message(m.chat.id, 'Шо мені робить?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, fourth_right_2)


# НАПИСАТЬ ФУНКЦІЮ ТА ШО ДО СХОДИНОК
def fourth_right_2(m):
    if m.text == 'Краще піти на сходинки':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "ЗУСТРІЧАЄТЕ ВІкНО ")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Піти далі']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Залізти в вікно']])
        bot.send_message(m.chat.id, 'куди б ви пішли??',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, direct_windows_and_go_one)  # функція вікна



    elif m.text == 'Пливти':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Вас зїли піранії")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Почати заново']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Тут тоже вставить ссилку на дьомин квест']])
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
        msg = bot.send_message(m.chat.id, "Тут буде якийсь текст")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Відкрити']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Іти на світло']])
        bot.send_message(m.chat.id, 'Зустрічаєм двері',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, direct_door)


def direct_door(m):
    if m.text == 'Відкрити':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Перед нами сходинки і маленьке вікно")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Залізти в вікно']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Просто пройду далі']])
        bot.send_message(m.chat.id, 'Куди ти хочеш іти?',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, direct_windows)  # функція нва одному рівні з вікном

    elif m.text == 'Іти на світло':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Додумать")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Додумать']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Додумать']])
        bot.send_message(m.chat.id, 'Додумать',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg)


def direct_windows(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    msg = bot.send_message(m.chat.id, "Ви бачите перед собюоюю кодовий замок з екраном")
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
        msg = bot.send_message(m.chat.id, "Тут буде якийсь текст")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Попробувать ввести код']])
        bot.send_message(m.chat.id, 'Ви зустрічаєте кодовий замок',
                         reply_markup=keyboard)
        bot.register_next_step_handler(msg, direct_windows)

    elif m.text == 'Залізти в вікно':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(m.chat.id, "Тут буде якийсь текст")
        sleep(1)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Попробувать ввести код']])
        bot.send_message(m.chat.id, 'Ви зустрічаєте кодовий замок',
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
