export pwd=A123qweasd!
sudo pkill gunicorn
sudo systemctl reload nginx
gunicorn -b 0.0.0.0:8080 wsgi:app --daemon
echo Started!
su ubuntu
