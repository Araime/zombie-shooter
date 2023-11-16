## Zombie shooter

Демо-версия игры про зомби. Реакция врагов на выстрелы, подбор оружия, радар.

## Установка

### Скачать

Python3 должен быть уже установлен.
[Скачать](https://github.com/Araime/zombie-shooter/archive/master.zip) этот 
репозиторий себе на компьютер.

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html)
для изоляции проекта.

#### Быстрая настройка venv

Начиная с Python версии 3.3, виртуальное окружение идёт в комплекте в виде модуля
venv. Чтобы его установить и активировать нужно выполнить следующие действия в
командной строке:  

Указать скачанный репозиторий в качестве каталога.
```sh
cd C:\Users\ваш_пользователь\Downloads\папка_репозитория
```
Установить виртуальное окружение в выбранном каталоге.
```sh
Python -m venv env
```
В репозитории появится папка виртуального окружения env  

<a href="https://imgbb.com/"><img src="https://i.ibb.co/Hn4C6PD/image.png" alt="image" border="0"></a>

Активировать виртуальное окружение.
```sh
env\scripts\activate
```
Если всё сделано правильно, вы увидите в командной строке (env) слева от пути 
каталога.  

<a href="https://imgbb.com/"><img src="https://i.ibb.co/MZ72r22/2.png" alt="2" border="0"></a>

#### Установить зависимости

Используйте `pip` для установки 
зависимостей:

```sh
pip install -r requirements.txt
```

### Запуск

```sh
python main.py
```

## Запуск на Windows 10/11 pro как exe-файл

### Подготовка

Установите библиотеку [pyinstaller](https://pypi.org/project/pyinstaller/).

```sh
pip install pyinstaller
```

### Создание exe-файла

Сначала создать предварительный exe-файл.

```sh
pyinstaller -w -F main.py
```

После сборки exe-файла в корне репозитория создается папка dist, в которой будет
лежать готовое приложение.

Затем в появившемся в корне файле main.spec изменить следующие параметры:  
`1.` в `datas = [ ]` добавить `('img', 'img'), ('maps', 'maps'), ('music', 'music'), ('snd', 'snd'),`,
путь к папкам с изображениями, звуками, картами.  
`2.` в `name = ' '` указать любое имя приложения.  
`3.` в конце раздела exe, после entitlements_file добавить строчку
`icon=['icon.ico'],`.

Теперь в pyinstaller можно просто указать файл main.spec:

```sh
pyinstaller main.spec
```
Окончательный exe-файл собран и лежит в папке dist.

## Credits

[Sprites](https://kenney.nl/assets/top-down-shooter) - Kenney.

## Цель проекта

Данный репозиторий создан с целью изучения возможности создания игр
на Python.
