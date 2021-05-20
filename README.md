<h4 align="center">Alcoshopers Coub bot</h4>

<p align="center">Alcoshopers Coub bot - простой и быстрый поиск музыки из coub в приложении Telegram</p>
<p align="center">Ссылка на Alcoshopers Coub bot в телеграм: <a href="https://t.me/AlcoshopersCoubBot"><span>@AlcoshopersCoubBot</span></a></p>

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
