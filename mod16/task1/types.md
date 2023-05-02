### Типы связей таблиц:
* movie_cast -> actors (act_id):  многие к одному
* movie_cast -> movie (mov_id):  многие к одному
* oscar_awarded -> movie (mov_id):  многие к одному 
* movie_direction -> movie (mov_id):  многие к одному
* movie_direction -> director (dir_id):  многие к многим