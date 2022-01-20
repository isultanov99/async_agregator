# JSON Agregator

## Description — Описание

---
The `Flask` app accesses three HTTP data sources asynchronously using `aiohttp`, `asyncio` HTTP client.\
The combined and sorted by `id` result is available at `/get-data/`.\
Any source error or timeout > 2 s. is ignored and considered as absence of data.
---
Приложение `Flask` асинхронно обращается к трем источникам данных HTTP, используя `aiohttp`, HTTP клиент `asyncio`.\
Объединенный и отсортированный по `id` результат доступен в `/get-data/`.\
Любая ошибка источника или таймаут больше двух секунд игнорируется и считается отсутствием данных.
## Getting Started — Начало работы

---
Linux/MacOS
```bash
$ git clone https://github.com/isultanov99/async_agregator.git
$ cd async_agregator/
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
Windows

```powershell
git clone https://github.com/isultanov99/async_agregator.git
cd async_agregator/
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

## Configure and running the app — Настройка и запуск приложения

---
To select source links change three variables: `URL1, URL2, URL3` in `app.py` file. At the current moment three test files at `/static/` folder are used.\
Finally, launch app:
```bash
$ python app.py
```
and go to [http://localhost:5000/get-data](http://localhost:5000/get-data)

---
Чтобы выбрать ссылки c источниками, измените три переменные: `URL1, URL2, URL3` в файле `app.py`. На данный момент используются три тестовых файла в папке `/static/`.\
Наконец, запустите приложение:
```bash
$ python app.py
```
и перейдите по ссылке [http://localhost:5000/get-data](http://localhost:5000/get-data)