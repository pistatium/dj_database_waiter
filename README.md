# dj_database_waiter
Script to keep waiting until Django's DB is ready.

This is useful when you want to wait for DB connection, such as when using DockerCompose.

## Required

* Python3.6.1+
* Django

## Install
```
pip3 install dj_database_waiter
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


__DB の準備が出来るまで Django の起動を待つコマンド作ってみた__
https://qiita.com/kimihiro_n/items/d42e066a2e495f0c4866
