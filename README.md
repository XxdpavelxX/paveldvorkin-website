# paveldvorkin-website
My personal website


## Django setup Documentation: 
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment



## Run app uwsgi: 
uwsgi --http :8000 --module locallibrary.wsgi (Run from /locallibrary repo)

## Run app with nginx:
nginx -c /Users/paveldvorkin/paveldvorkin-website/nginx/nginx.conf
### Follow nginx logs
tail -f /usr/local/var/log/nginx/error.log

## Documentation
https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html
nginx (on mac): https://medium.com/@ThomasTan/installing-nginx-in-mac-os-x-maverick-with-homebrew-d8867b7e8a5a
deploying instance: https://medium.com/@srijan.pydev_21998/complete-guide-to-deploy-django-applications-on-aws-ubuntu-16-04-instance-with-uwsgi-and-nginx-b9929da7b716