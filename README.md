
Record Counter Scripts
===

It can count number of records in tables, in databases.

<!-- ![1](media/***.jpg) -->

## Description

When you wanna know how many records exist in some tables, you ought to use this command.

```sql
SELECT * FROM information_schema.TABLES where table_schema = 'table name';
```

This is totally meaningless. Since the numbers which it gives you are only approximate. Use my scripts.

## Dependency

```bash
pip install pymysql
```

## Usage
