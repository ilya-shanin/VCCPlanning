# Сервис для мониторинга сеансов ВКС
Веб-сервис предназначен для предоставления сотрудникам актуальной информации о проходящих и запланированных сеансах видео-конференц связи.
# Инструкции по установке (на хостинг)
1.	Подоберите хостинг-провайдера с поддержкой фреймворка Django.
2.	Зарегистрировать домен (если его еще нет).
3.	В настройках домена выбрать веб-сервер с поддержкой протокола wsgi/uwsgi. Например, это может быть uWSGI или Gunicorn.
4.	Выполнить настройку среды и установить необходимые модули на сервер. Чтобы это сделать требуется подключиться к серверу по протоколу SSH. Для этого может потребоваться дополнительное программное обеспечение. (При прохождении практики использовался SSH-клиент PuTTY).
5.	Создать виртуальное окружение для python. Рекомендуется использовать python 3.8.0 Виртуальное окружение можно создать при помощи пакета python virtualenv (команда ‘pip install «наименование пакета» --user’ для установки, параметр user гарантирует, что вам не понадобятся дополнительные права для установки пакета).
6.	Выполните команду virtualenv --system-site-packages «наименование окружения». Это позволит задействовать внутри окружения модули, установленные на сервере. Чтобы активировать виртуальное окружение: source ~/«наимеование окружения»/bin/activate.
7.	Теперь, находясь в виртуальном окружении, установите необходимые для работы модули: six, Pillow, Django, pathlib2, mysqlclient (для работы с MySQL), python-dotenv.
В корневом каталоге сайта создайте site.wsgi (либо укажите путь к существующему входному файлу в .htaccess). Замените username на логин вашего аккаунта, domain.ru — на доменное имя вашего сайта, envname — имя виртуальной среды, myproject — имя проекта:  
```python
import os, sys  
activate_this = '/home/username/envname/bin/activate_this.py'  
with open(activate_this) as f:  
    exec(f.read(), {'__file__': activate_this})  
sys.path.insert(0, os.path.join('/home/username/domains/domain.ru/myproject'))  
os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'  
from django.core.wsgi import get_wsgi_application  
application = get_wsgi_application()  
```  
8.	Активируйте WSGI в файле .htaccess (для apache). Аналогичные инструкции также есть для nginx, обычно они предоставляются хостингом:
``` 
DirectoryIndex site.wsgi
Options +ExecCGI
AddHandler wsgi-script .wsgi
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ /site.wsgi/$1 [QSA,PT,L]
```
9.	С помощью файлового менеджера хостинга или FTP-клиента, присоединившись к серверу, загрузите файлы проекта в директорию домена.
10.	Измените настройки проекта. В файле .env установите DEBUG=False, это выключит детальное отображение ошибок на сайте. Заполните настройки для подключения к вашей базе данных и почтовому клиенту. Удалите локальную БД, которая использовалась для разработки (v3c_db.sqlite3). В файле settings.py в параметр ALLOWED_HOSTS запишите название вашего домена.
11.	С помощью SSH-клиента в директории загруженного проекта выполните следующие команды:
```
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
```
# Обслуживание статических файлов
Статические файлы здесь обслуживаются через приложение Django, что не является очень эффективным способом. Рекомендуется использовать для этого веб-сервер.
Пример для Apache:
```
Alias /static /home/username/domains/domain.ru/projectname/static_collected  
<Directory "/home/username/domains/domain.ru/projectname/static_collected">  
    Require all granted  
</Directory>  
Alias /media /home/username/domains/domain.ru/projectname/media  
<Directory "/home/username/domains/domain.ru/projectname/media">  
    Require all granted  
</Directory> 
```
