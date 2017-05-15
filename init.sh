sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx -s reload

sudo ln -sf /home/box/web/etc/hello.py   /etc/gunicorn.d/hello.py
sudo gunicorn -c /etc/gunicorn.d/hello.py hello:application
















