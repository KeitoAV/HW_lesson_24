# Lesson 24. Homework. Типизация и дополнительные темы.

Нужно дополнить домашнее задание с предыдущего урока.

## Задача
### *Регулярные выражения*

Добавить команду - regex.
Запрос возвращает только логи получения картинок png.

Пример запроса:

payload = {

   'file_name': 'apache_logs.txt',

   'cmd1': 'regex',

   'value1': 'images\/(\w+|(\w+-\w+)|.{1,})\.png',

   'cmd2': 'sort',

   'value2': 'asc'

}

### *Типизация*

Команда mypy app.py должна выполняться без ошибок.





