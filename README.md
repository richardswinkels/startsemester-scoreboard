# Install guide

## Clone project

```
git clone git@github.com:richardswinkels/startsemester-scoreboard.git
```

## Setup venv

Mac or Linux

```
$ python3 -m venv .venv
```

Windows

```
py -3 -m venv .venv
```

## Activate venv

MacOS or Linux

```
. .venv/bin/activate
```

Windows

```
.venv\Scripts\activate
```

## Install dependencies

```
pip install -r requirements.txt
```

## Serving your app

### Development server

```
flask run --debug
```

### Production server
```
waitress-serve --host=0.0.0.0 --port=8000 app:app
```