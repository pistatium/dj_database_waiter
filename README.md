# dj_database_waiter
Script to keep waiting until Django's DB is ready.

This is useful when you want to wait for DB connection, such as when using DockerCompose.

## Required

* Python3.6.1+
* Django

## Install
```
pip install -e .
```

## Usage

```
$ dj_database_waiter myproject.settings

Failed to connect database. :(2003, "Can't connect to MySQL server on 'db' ([Errno -2] Name or service not known)")
Retrying... (1/60)
Failed to connect database. :(2003, "Can't connect to MySQL server on 'db' ([Errno -2] Name or service not known)")
Retrying... (2/60)

# Database is ready
```
