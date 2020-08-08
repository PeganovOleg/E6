# E6

само приложение в файле app.py

В папке doker лежат файлы для сборки образов flask и memcached
их нужно переименовать просто в  Dockerfile
***********flask*************
создаем докер для Flask:
запустить команду 
$ sudo docker build -t my_flask_app:v0.1 my_flask_app/
потом смотрим созданный образ
$sudo docker images
запускаем докер из контейнера
sudo docker run -d -p 5000:5000 my_flask_app:v0.1
для остановки
sudo docker stop "id образа"

*********memcached**********
оздаем докер для memcached:
запустить команду 
$ sudo docker build -t my_caches:v0.1 
потом смотрим созданный образ
$sudo docker images
запускаем докер из контейнера
sudo docker run -d -p 11211:11211
для остановки 
sudo docker stop "id образа"

************************************************
После создания докеров использовать файл docker-compose.yaml
запустить
docker-compose build
в директории, где находится docker-compose.yaml. 
После того, как необходимые образы собраны, можно их запустить.
Это можно сделать с помощью команды
docker-compose up.
Проверить, что контейнеры успешно запущены, можно с помощью команды docker ps


