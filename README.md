<h4 align="center">Coub-Assistant-Telegram-bot</h4>

<p align="center">Coub Assistant - это сервис, который поможет вам легко и быстро найти музыку из Coub. А с помощью Telegram бота пользоваться сервисом будет еще проще</p>
<p align="center">Официальный сайт: <a href="https://coubassistant.com/"><span>coubassistant.com</span></a></p>
<p align="center">Ссылка на Coub-Assistant-Telegram-bot в телеграм: <a href="https://t.me/coub_assistant_bot"><span>@coub_assistant_bot</span></a></p>
<!-- <a align="center" href="https://coubassistant.com/"><span>Официальный сайт coubassistant.com</span></a> -->

<hr align="center"/>

<p align="center">
	<img src="https://img.shields.io/pypi/pyversions/apache-airflow.svg">
</p>



## Как запустить:

Первым делом клонируем проект и переходим в директорию проекта
```
git clone git@github.com:ignatiy/Coub-Assistant-Telegram-bot.git
cd Coub-Assistant-Telegram-bot/
```

Создаем виртуальное окружение
```
python3 -m venv env
```

Активируем его
```
source env/bin/activate
```

Устанавливаем зависимости проекта
```
pip3 install -r requirements.txt
```

Деактивируем виртуальное окружение. Больше оно нам не понадобится
```
deactivate
```

В файле `app/config.py` указываем свой токен полученный у BotFather.

Редактируем `coub.service`. Меняем пути в `WorkingDirectory`, `Environment` и `ExecStart` на свои.

Добавляем в автозагрузку
```
$ sudo ln -s Coub-Assistant-Telegram-bot/app/coub.service /etc/systemd/system/
```
Включаем
```
$ sudo systemctl enable coub
```
