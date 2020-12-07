# -*- coding: utf-8 -*-
# Telegram bot @juffbot
from itertools import zip_longest
import telebot
import random
import csv

bot_token = '1475053725:AAEhuulBqflD66qD-za0nyx-Rf-N4Gy4ngs'
bot_id = '1475053725'
group_id = '-1001456791597'
admin_id = ['874493573']
applications = False
sponsor = []

bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def open_message(message):
    try:
        if str(message.chat.id) != group_id:
            #print(message.chat.id)
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBpo1fyR73YQ4AAXME5YAyM90c7nwcNBIAArYEAAI_lcwKNTMRbUHaoHseBA')

            # keyboard
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = telebot.types.KeyboardButton('😎 Войти в аккаунт')
            markup.add(item1)

            bot.send_message(message.chat.id,
                             '⚠️Если вы являетесь администратором бота пожалуста войдите в аккаунт!\nПросто нажмите на кнопку снизу или напишите команду /join',
                             reply_markup=markup)
    except Exception as e:
        bot.send_message(message.chat.id, 'Что-то пошло не так, попробуйте обратиться к администратору')
        print(repr(e))


@bot.message_handler(commands=['join'])
def join_message(message):
    try:
        if str(message.from_user.id) in admin_id:
            bot.send_message(message.chat.id, 'Вы вошли в систему! :)')
        else:
            bot.send_message(message.chat.id, 'Вы не админ! -_-')
    except Exception as e:
        bot.send_message(message.chat.id, 'Что-то пошло не так, попробуйте обратиться к администратору')
        print(repr(e))


@bot.message_handler(commands=['add'])
def add_message(message):
    if applications:
        try:
            app = message.text.replace('/add', '').strip().split('+')
            if len(app) == 3:
                if len(app[1].split()) <= 15:
                    channel_id, info, username_channel, here, is_ban = app[0].strip(), app[1].strip(), app[2].strip(), [], False
                    if '@' not in username_channel:
                        username_channel = '@' + username_channel
                    with open('files/banlist.csv', 'r') as banlist_file:
                        reader = csv.reader(banlist_file, delimiter=';')
                        for row in list(reader)[1:]:
                            if row[0] == channel_id:
                                is_ban = True
                    if is_ban is False:
                        if bot.get_chat_member(chat_id=channel_id, user_id=bot_id).status == 'administrator':
                            with open('files/applications.csv', 'r') as app_file:
                                reader = csv.reader(app_file)
                                for row in reader:
                                    here.append(row[0])
                            if channel_id not in here:
                                bot.send_message(message.chat.id,
                                                 f'@{message.from_user.username}\nВаша заявка " {app[2]} - {app[1]} " успешно добавлена✅\nСпасибо за выбор проекта @avto_podbor_tg ❤️')
                                with open('files/applications.csv', 'a') as app_file:
                                    writer = csv.writer(app_file, delimiter=',')
                                    writer.writerow([channel_id, info, username_channel])
                            else:
                                bot.send_message(message.chat.id, 'Ваш канал уже добавлен в подборку! Ожидайте публикации')
                        else:
                            bot.send_message(message.chat.id, 'Заявка отклонена!\nПожалуйста добавте нашего бота @BOT в администраторы канала с возможностью отправлять сообщения!')
                    else:
                        bot.send_message(message.chat.id, 'Канал был забанен за нарушение прав сообщества!')
                else:
                    bot.send_message(message.chat.id, 'Пожалуйста укажите не больше 15 слов в описании канала!')
            else:
                raise ImportError
        except Exception as e:
            bot.send_message(message.chat.id, 'Ваша заявка не верна!\nПожалуйста проверте правильность всех данных!\nА также проверьте что @juffbot является администратором в вашем канале')
            print(repr(e))
    else:
        bot.send_message(message.chat.id,
                         f'Заявки закрыты!')


@bot.message_handler(commands=['addsponsor'])
def add_message(message):
    try:
        global sponsor
        if str(message.chat.id) != group_id:
            if str(message.from_user.id) in admin_id:
                try:
                    app = message.text.replace('/addsponsor', '').strip().split('+')
                    if len(app) == 3:
                        if len(app[1].split()) <= 15:
                            channel_id, info, username_channel = app[0], app[1], app[2]
                            if bot.get_chat_member(chat_id=channel_id, user_id=bot_id).status == 'administrator':
                                sponsor = [channel_id, info, username_channel]
                                bot.send_message(message.chat.id, f'@{message.from_user.username}\nЗаявка спонсора успешно добавлена✅\n️')
                            else:
                                bot.send_message(message.chat.id,
                                                 'Заявка отклонена!\nПожалуйста добавте нашего бота @BOT в администраторы канала с возможностью отправлять сообщения!')
                        else:
                            bot.send_message(message.chat.id, 'Пожалуйста укажите не больше 15 слов в описании канала спонсора!')
                    else:
                        raise ImportError
                except Exception as e:
                    bot.send_message(message.chat.id,
                                     'Ваша заявка не верна!\nПожалуйста проверте правильность всех данных!\n\nА также проверьте что @juffbot является администратором в канале спонсора!')
                    print(repr(e))
    except Exception as e:
        bot.send_message(message.chat.id,
                         'Ваша заявка не верна!\nПожалуйста проверте правильность всех данных!\n\nА также проверьте что @juffbot является администратором в канале спонсора!')
        print(repr(e))


@bot.message_handler(commands=['deletesponsor'])
def add_message(message):
    try:
        global sponsor
        if str(message.chat.id) != group_id:
            if str(message.from_user.id) in admin_id:
                sponsor = []
                bot.send_message(message.chat.id, 'Спонсор был успешно удален!')
    except Exception as e:
        bot.send_message(message.chat.id, "Новых заявок пока нет!")
        print(repr(e))


@bot.message_handler(commands=['list'])
def list_message(message):
    try:
        ans = ''
        with open('files/applications.csv', 'r') as app_file:
            reader = csv.reader(app_file)
            for row in list(reader)[1:]:
                ans += str(row[2]) + ' - ' + str(row[1]) + '\n\n'
        bot.send_message(message.chat.id, ans)
    except Exception as e:
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте обратиться к администратору")
        print(repr(e))


@bot.message_handler(commands=['stop'])
def stop_message(message):
    try:
        global applications
        if str(message.chat.id) != group_id:
            if str(message.from_user.id) in admin_id:
                applications = False
                bot.send_sticker(group_id, 'CAACAgIAAxkBAAEBp7hfy44XppQUV3K6FBGF1VfA1LHouwACvwQAAj-VzAq6ze7VyPp9Ox4E')
                bot.send_message(message.chat.id, 'Закрываю')
                bot.send_message(group_id, 'Прием заявок закрыт')
    except Exception as e:
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте обратиться к администратору")
        print(repr(e))


@bot.message_handler(commands=['open'])
def open_message(message):
    try:
        global applications
        if str(message.chat.id) != group_id:
            if str(message.from_user.id) in admin_id:
                applications = True
                with open('files/applications.csv', 'w') as app_file:
                    writer = csv.writer(app_file, delimiter=',')
                    writer.writerow(["channel_id", "info", "username_channel"])
                bot.send_sticker(group_id, 'CAACAgIAAxkBAAEBp7pfy44bTglS7SbRytKDCcvVSUSOZQACyAQAAj-VzAq606XjksVT5B4E')
                bot.send_message(message.chat.id, 'Открываю')
                bot.send_message(group_id, '‼️ Прием заявок открыт ‼\n\n ✅ В подборках могут принять участие только открытые каналы, с количеством подписчиков от 500 до 2000 .\n✅ Узнать id канала можно в @userinfobot\n\n🔻Шаблон заявки в чате:\n/add Пробел-id канала+название(до 15 слов)+@юзер id канала\n\n🔻Пример:\n/add -10013382714677+Курсы по продажам+@prodаji_ru ️')
    except Exception as e:
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте обратиться к администратору")
        print(repr(e))

@bot.message_handler(commands=['posting'])
def posting_message(message):
    try:
        global sponsor
        if str(message.chat.id) != group_id:
            if str(message.from_user.id) in admin_id:
                with open('files/del_file.csv', 'w') as del_file:
                    writer = csv.writer(del_file, delimiter=';')
                    writer.writerow(['id_channel', 'id_message'])
                x = 4
                channels = {}
                channels_d = []
                channels_s = {}
                with open('files/applications.csv', 'r') as app_file:
                    reader = csv.reader(app_file)
                    for row in list(reader)[1:]:
                        channels[row[0]] = str(row[2]).strip() + ' - ' + str(row[1]).strip()
                        channels_d.append(row[0])
                random.shuffle(channels_d)
                if channels:
                    bot.send_message(message.chat.id, 'Публикую подборки...')
                    bot.send_sticker(group_id, 'CAACAgEAAxkBAAEBpZFfx8EeK_tN4m9E1H5fzSDEt-gUmwACSAoAAr-MkAR1JNc-C1-Z1B4E')
                    bot.send_message(group_id, 'Каналы ушли на публикацию!')
                    if len(channels) == 1:
                        x = 1
                    elif len(channels) == 2:
                        x = 2
                    elif len(channels) == 3:
                        x = 3
                    elif len(channels) == 4:
                        x = 4
                    elif len(channels) == 5:
                        x = 5
                    elif len(channels) < 6:
                        x = 5
                    elif len(channels) < 12:
                        x = 5
                    elif len(channels) < 20:
                        x = 6
                    elif len(channels) < 30:
                        x = 8
                    elif len(channels) > 30:
                        x = 10
                    group_channels_edit = list(zip_longest(*[iter(channels_d)]*x, fillvalue='x'))
                    #print(group_channels_edit)
                    group_channels = []
                    z = 0
                    for i in group_channels_edit:
                        if 'x' not in i:
                            group_channels.append(i)
                        else:
                            r = []
                            for y in i:
                                if y == 'x':
                                    r.append(channels_d[z])
                                    z += 1
                                else:
                                    r.append(y)
                            group_channels.append(r)
                    for i in group_channels:
                        for y in i:
                            r = []
                            for f in i:
                                if f != y:
                                    r.append(f)
                            channels_s[y] = r
                    for i in channels_s:
                        ans = ''
                        for y in channels_s[i]:
                            ans += channels[y] + '\n\n'
                        if sponsor != []:
                            ans += 'попасть в подборку - @avto_podbor_tg'
                            ans = str(sponsor[2]) + ' - ' + str(sponsor[1]) + '\n\n' + ans
                            ans = 'Интересные каналы Telegram. Подпишись, чтобы не потерять\n\n' + ans
                        else:
                            ans += 'попасть в подборку - @avto_podbor_tg'
                            ans = 'Интересные каналы Telegram. Подпишись, чтобы не потерять\n\n' + ans
                        res = bot.send_message(i, ans)
                        with open('files/del_file.csv', 'a') as del_file:
                            writer = csv.writer(del_file, delimiter=';')
                            writer.writerow([i, str(res.message_id)])
                else:
                    bot.send_message(message.chat.id, 'В списке нет новых каналов!')
                    #print('Dickt is empty!')
    except Exception as e:
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте обратиться к администратору")
        print(repr(e))


@bot.message_handler(commands=['ban'])
def ban_message(message):
    try:
        if str(message.chat.id) != group_id:
            if str(message.from_user.id) in admin_id:
                can_ban = True
                bch = message.text.replace('/ban', '').strip().split('+')
                if len(bch) == 3:
                    with open('files/banlist.csv', 'r') as banlist_file:
                        reader = csv.reader(banlist_file, delimiter=';')
                        for row in list(reader)[1:]:
                            if row[0] == bch[0]:
                                can_ban = False
                    if can_ban:
                        with open('files/banlist.csv', 'a') as banlist_file:
                            writer = csv.writer(banlist_file, delimiter=';')
                            writer.writerow([bch[0], bch[1], bch[2]])
                        bot.send_message(message.chat.id, f'Канал {bch[1]} забанен!')
                    else:
                        bot.send_message(message.chat.id, f'Канал {bch[1]} уже забанен!')
                else:
                    bot.send_message(message.chat.id, f'Пожалуйста выполнете все по примеру!')
    except Exception as e:
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте обратиться к администратору")
        print(repr(e))


@bot.message_handler(commands=['unban'])
def unban_message(message):
    try:
        if str(message.chat.id) != group_id:
            if str(message.from_user.id) in admin_id:
                try:
                    human = message.text.replace('/unban', '').strip().split()
                    if len(human) == 1:
                        human = human[0]
                        in_ban = False
                        banlist = []
                        with open('files/banlist.csv', 'r') as banlist_file:
                            reader = csv.reader(banlist_file, delimiter=';')
                            for row in list(reader):
                                banlist.append(row)
                        for i in banlist:
                            if human in i:
                                in_ban = True
                        if in_ban:
                            with open('files/banlist.csv', 'w') as banlist_file:
                                writer = csv.writer(banlist_file, delimiter=';')
                                for row in banlist:
                                    if human not in row:
                                        writer.writerow(row)
                            bot.send_message(message.chat.id, f'Канал {human} прощен! :)')
                        else:
                            bot.send_message(message.chat.id, f'Канал {human} не забанен! :)')
                    else:
                        bot.send_message(message.chat.id, f'Пожалуйста выполнете все по примеру!')
                except Exception as e:
                    print(repr(e))
    except Exception as e:
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте обратиться к администратору")
        print(repr(e))


@bot.message_handler(commands=['banlist'])
def banlist_message(message):
    try:
        if str(message.chat.id) != group_id:
            if str(message.from_user.id) in admin_id:
                try:
                    ans = ''
                    with open('files/banlist.csv', 'r') as banlist_file:
                        reader = csv.reader(banlist_file, delimiter=';')
                        for row in list(reader)[1:]:
                            ans += str(row[1]) + f' ({str(row[0])}) - ' + str(row[2]) + '\n\n'
                    bot.send_message(message.chat.id, 'Вот эти плохеши:')
                    bot.send_message(message.chat.id, ans)
                except Exception as e:
                    print(repr(e))
                    bot.send_message(message.chat.id, 'Список бан листа пуст!')
    except Exception as e:
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте обратиться к администратору")
        print(repr(e))


@bot.message_handler(commands=['delete'])
def delete_message(message):
    try:
        del_info = {}
        with open('files/del_file.csv', "r") as del_file:
            reader = csv.reader(del_file, delimiter=';')
            for row in list(reader)[1:]:
                del_info[row[0]] = row[1]
        for i in del_info:
            bot.delete_message(i, del_info[i])
        bot.send_message(message.chat.id, 'Все подборки были удалены!')
    except Exception as e:
        bot.send_message(message.chat.id, 'Невозможно удалить подборки!')
        print(repr(e))


@bot.message_handler(content_types=['text'])
def text_message(message):
    try:
        if message.text == '😎 Войти в аккаунт':
            if str(message.chat.id) != group_id:
                try:
                    if str(message.from_user.id) in admin_id:
                        bot.send_message(message.chat.id, 'Вы вошли в систему! :)')
                    else:
                        bot.send_message(message.chat.id, 'Вы не админ! -_-')
                except Exception as e:
                    print(repr(e))
        if message.text == '/delite':
            pass
        #print(message.text)
    except Exception as e:
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуйте обратиться к администратору")
        print(repr(e))


bot.polling()
