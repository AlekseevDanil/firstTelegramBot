# Небольшое описание бота и как все установить на хостинг (на примере хостинга VDS)

_Немного описание бота_:
Мой первый product Бот в Телеграм
Бот умеет: Открывайть/закрывать заявки на сбор групп; Банить пользователей; Имеет админку; Умее показывать список забаненых + причина и многое другое! :)

_Запускаем все на сервере:_

1.Очень важно подготовить сервер к запуску бота
Итак, подготавливаем сам сервер, в VDS в вашем сервере переходим во вкладку Консоль. Если у вас требует войти в систему:
логин: root
пароль: ваш пароль от системы (к примеру wQxiPAa9)
2. Устанавливаем пакеты:
*Пометка:* Если у вас будет вопрос с таким выбором [y/n] ОТВЕЧАЕМ y

Сейчас я перечислю команды которые нужно перечислить в консоль (копируем и вставляем):

*sudo apt-get install gnome-terminal    (Устанавливаем ГНОМ терминал)
*sudo apt install python3               (скачиваем python 3.x)
*sudo apt install python3-pip           (скачиваем установщик пакетов питона PIP)
*pip3 install pyTelegramBotAPI          (устанавливаем библиотеку для коректной работы на сервере)
*sudo apt install git                   (устанавливаем git)
*git clone https://github.com/forjuffbot/firtTeleBot.git       (скачиваем все файлы бота на сервер)
*sudo apt install nodejs                (устанавливаем nodejs)
*sudo apt install npm                   (устанавливаем npm)
*npm install pm2 -g                     (устанавливаем pm2, для работы бота в фоне)
*cd /Имя папки с ботом                  (переходим в папку с ботом)
*pm2 start firtTelegramBot.py --interpreter=python3                 (замените firtTelegramBot.py на имя исполняемого файла бота)

_ВСЕ ГОТОВО!_
Поздравляю! У вас получилось установить бота на сервер! Желаю вам дальнейших успехов! :)
