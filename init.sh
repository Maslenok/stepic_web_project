sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx -s reload


#sudo rm -r /etc/gunicorn.d/*
#sudo gunicorn hello:application
#sudo ln -sf /home/box/web/etc/hello.py   /etc/gunicorn.d/hello.py
#sudo ln -sf /home/box/web/etc/django_ask.py   /etc/gunicorn.d/django_ask.py

#sudo /etc/init.d/gunicorn restart
#sudo gunicorn -c /etc/gunicorn.d/hello.conf hello:application
#sudo gunicorn -c /home/box/web/etc/django_ask.py ask.wsgi:application
















