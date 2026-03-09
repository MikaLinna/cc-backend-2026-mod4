# cc-backend-2026-mod4

This uses python 3.12

# start
flask --app api run --debug 
waitress-serve --host 127.0.0.1 api:app
python app.py

# info sites
https://iamjeremie.me/post/2025-02/parsing-json-payload-on-rest-api-call-with-flask/
* https://flask.palletsprojects.com/en/stable/deploying/gunicorn/ (not udes...)
https://flask.palletsprojects.com/en/stable/deploying/waitress/

# other software maybe needed
https://gunicorn.org/ (WSGI WEb-server WSL/Linux)
https://pypi.org/project/waitress/ (WSGI WEb-server Windows)

# scikit-leean==1.6.1
In Google Colab sklearn version is 1.6.1
install packages: threadpoolctl, numpy, joblib, scipy, scikit-learn
