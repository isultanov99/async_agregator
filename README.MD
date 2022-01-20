# JSON Agregator

## Description — Описание

The `Flask` app accesses three HTTP data sources asynchronously using `aiohttp`, `asyncio` HTTP client.\
The combined and sorted by `id` result is available at `/get-data/`.\
Any source error or timeout > 2 s. is ignored and considered as absence of data.

---
Приложение `Flask` асинхронно обращается к трем источникам данных HTTP, используя `aiohttp`, HTTP клиент `asyncio`.\
Объединенный и отсортированный по `id` результат доступен в `/get-data/`.\
Любая ошибка источника или таймаут больше двух секунд игнорируется и считается отсутствием данных.

## Getting Started — Начало работы

macOS (Tested on macOS Mojave 10.14 and Big Sur 11.6)
```bash
$ git clone https://github.com/isultanov99/async_agregator.git
$ cd async_agregator/
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Linux (Tested on Ubuntu 21.10 and WSL Ubuntu 18.04)
```bash
$ git clone https://github.com/isultanov99/async_agregator.git
$ cd async_agregator/
$ pip install virtualenv
$ python -m virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Windows (Tested on Windows 10 ver. 20H1)

```cmd
git clone https://github.com/isultanov99/async_agregator.git
cd async_agregator
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

## Configure and running the app — Настройка и запуск приложения

To select source links change three variables: `URL1, URL2, URL3` in `app.py` file. At the current moment three test files at `/static/` folder are used.\
Finally, launch app:
```bash
$ python app.py
```
and go to [http://localhost:5000/get-data](http://localhost:5000/get-data) \
If you are running into `import` errors, try `pip3` and `python3` instead of `pip` and `python`.

---
Чтобы выбрать ссылки c источниками, измените три переменные: `URL1, URL2, URL3` в файле `app.py`. На данный момент используются три тестовых файла в папке `/static/`.\
Наконец, запустите приложение:
```bash
$ python app.py
```
и перейдите по ссылке [http://localhost:5000/get-data](http://localhost:5000/get-data) \
Если вы столкнулись с `import` ошибками, попробуйте `pip3` и `python3` вместо `pip` и `python`.

