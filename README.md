# Как изменить файл для нового бота и как все установить на хостинг (на примере хостинга vds)

_Изменяем файл для нового бота_:

1. Очень важно подготовить все фалы перед добавление бота
У вас должна быть папка к примеру juffbot (имя папки может быть любым, в ней будет храниться проект) и в ней должна храниться папка files (ПУСТАЯ, программа сама создаст все нужные файлы в ней и ОБЯЗАТЕЛЬНО с именем _files_), а рядом должен быть файл python (run_juffbot.py имя тоже может быть любым, но расширение должно стоять .py).
2. Изменияем файл run_juffbot.py
После того, как мы создали окружение (все нужные папки) для нашего бота, переходим к редактированию самого файла...
В нем вы увидите строчки:

bot_token = '1320444471:AAGFW3VCl-eyVGjkcxNTixHwglp1QoV6D-4'
bot_id = '1320444471'
group_id = '-1001431089595'

первая строка "bot_token" означает токен вашего бота, вторая строка "bot_id" означает id самого бота, третья строка  "group_id" это id группы

Вы можете их изменять ГЛАВНОЕ брать все в кавычки 'ваш_токен' или "ваш_токен"
так же в коде есть названия канлов @juffbot их тоже можно изменять по примеру в файлах

Сохраняем файл и вуаля, все работает! :)

_Запускаем все на сервере:_

1.Очень важно подготовить сервер к запуску бота
Итак, подготавливаем сам сервер, в VDS в вашем сервере переходим во вкладку Консоль. Если у вас требует войти в систему:
логин: root
пароль: ваш пароль от системы (к примеру wQxiPAa9)
2. Устанавливаем пакеты:
*Пометка:* Если у вас будет вопрос с таким выбором [y/n] ОТВЕЧАЕМ y

Сейчас я перечислю команды которые нужно перечислить в консоль (копируем и вставляем):

sudo apt-get install gnome-terminal
sudo apt install python3.8
sudo apt install python3-pip
pip3 install pyTelegramBotAPI



