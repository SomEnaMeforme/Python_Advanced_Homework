###   Телефоны какого цвета чаще всего покупают?
Violet
Краткое описание решения:
* Выполнен запрос к базе данных: _select max(sold_count), phone_color from table_checkout_
* Выведена соответствующая строчка таблицы, телефоны данного цвета покупали 1120 раз, это максимальное значение
### Какие телефоны чаще покупают: красные или синие?
Красные
Краткое описание решения:
* Выполнен запрос к базе данных: _select*from table_checkout where phone_color='Red' or phone_color='Blue'_
* Выведена соответствующие строчки таблицы, из которых видно, что телефоны красного цвета купили 64 раза, а телефоны синего цвета всего 36 раз.  
### Какой самый непопулярный цвет телефона? 
Goldenrod
Краткое описание решения:
* Выполнен запрос к базе данных: _select min(sold_count), phone_color from table_checkout_
* Выведена соответствующая строчка таблицы, телефоны данного цвета покупали всего 2 раза, это минимальное значение