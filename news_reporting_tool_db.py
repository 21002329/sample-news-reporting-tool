# Database code for the News reporting tool.

import psycopg2

DBNAME = 'news'


def get_articles_all_time_top_three():
    """Return most popular three articles of all time."""
    conn = psycopg2.connect(database=DBNAME)
    c = conn.cursor()
    stmt = '''select a.title, count(*) from articles a, log b \
        where substring(b.path from 10) = a.slug group by a.title \
        order by count(*) desc limit 3;'''
    c.execute(stmt)
    return c.fetchall()
    conn.close()


def get_authors_most_popular():
    """Return authors with article count, most popular on top."""
    conn = psycopg2.connect(database=DBNAME)
    c = conn.cursor()
    stmt = '''select d.name, c.count \
        from (select a.author, count(*) \
            from articles a, log b \
            where substring(b.path from 10) = a.slug \
            group by a.author) c, authors d \
        where c.author = d.id order by c.count desc;'''
    c.execute(stmt)
    return c.fetchall()
    conn.close()


def get_dates_w_excessive_req_errors():
    """Return dates when more than 1% of requests lead to errors."""
    conn = psycopg2.connect(database=DBNAME)
    c = conn.cursor()
    stmt = '''select a.date, (a.count::float / b.count) * 100 perc \
        from (select time::date date, count(*) \
            from log \
            where substring(status from 1 for 1) in ('4', '5') \
            group by date) a, \
            (select time::date date, count(*) \
            from log group by date) b \
        where a.date = b.date and (a.count::float / b.count) * 100 > 1.0;'''
    c.execute(stmt)
    return c.fetchall()
    conn.close()
