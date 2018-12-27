
Record Counter Scripts
===

It can count number of records in tables, in databases.

<!-- ![1](media/***.jpg) -->

## Description

## Dependency

```bash
pip install pymysql
```

## Usage

Write your database's settings in the scripts, then run.

## MySQL

When you wanna know how many records exist in some tables, you ought to use this command.

```sql
SELECT * FROM information_schema.TABLES where table_schema = 'table name';
```

This is totally meaningless. Since the numbers which it gives you are only approximate. Use my scripts.

## SQLserver

As I don't find out how to connect with SQLserver, I gave up to create a version for SQLserver, by the way.

## Sqlite

No problems. Feel free to run.
