README
==================

Getting Started
---------------

клоним репу
- kuzmenko-pavel@GT72-2QD ~/Project/TMP $ git clone https://github.com/Kuzmenko-Pavel/parse-text-img.git

переходим в склоненое
- kuzmenko-pavel@GT72-2QD ~/Project/TMP $ cd parse-text-img

создаем окружение под python3.6 (для этого с OS должен быть установлен python3.6)
- kuzmenko-pavel@GT72-2QD ~/Project/TMP/parse-text-img $ virtualenv -p python3.6 --no-site-packages env

активируем окружение питона
- kuzmenko-pavel@GT72-2QD ~/Project/TMP/parse-text-img $ source env/bin/activate

устанавливаем зависимости
- (env) kuzmenko-pavel@GT72-2QD ~/Project/TMP/parse-text-img $ pip install -r requirements.txt 

запускаем скрипт
- (env) kuzmenko-pavel@GT72-2QD ~/Project/TMP/parse-text-img $ python img_text_parser.py

скрипт бажный, выход в нем только по зактырию терминала, фиксанул чтобы был просто запускаемый пример

Если не стоит в системе python3.6 и система ubuntu 16.04
---------------
- sudo add-apt-repository ppa:deadsnakes/ppa
- sudo apt-get update
- sudo apt-get install python3.6 python3.6-dev