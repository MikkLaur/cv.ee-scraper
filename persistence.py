import os
import sqlite3
from time import strptime, strftime, localtime
from sys import exit


DIRECTORY = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(DIRECTORY, 'scrapesqlite.db')


class Columns:
  company, job_title, location, url, logo_url, post_date, end_date = range(7)


def log_error(error_name, message):
  timestamp = timestamp = strftime("%Y.%m.%d-%H:%M:%S", localtime())
  print(timestamp, error_name + ":", message)

  with open(DIRECTORY + '/logs/error-' + error_name + '_' + timestamp, 'w') as handle:
    handle.write(str(message))


def create_connection():
  try:
    conn = sqlite3.connect(DB_PATH)
    return conn
  except Error as e:
    log_error('create_connection', e)

  return None


def save(adverts):
  insertion_statement = '''
    INSERT OR REPLACE INTO adverts(company, job_title, location, url, logo_url, post_date, end_date)
    VALUES (?,?,?,?,?,?,?)
  '''

  conn = create_connection()
  if conn == None:
    log_error('save', 'No connection')
    return

  try:
    c = conn.cursor()
    c.executemany(insertion_statement, adverts)

  except sqlite3.Error as e:
    print('Saving error!')
    log_error('save', e)

  finally:
    conn.commit()
    conn.close()


def load():
  select_statement = '''
  SELECT * FROM adverts ORDER BY post_date DESC
  '''

  conn = create_connection()
  if conn == None:
    log_error('load', 'No connection to database.')
    return

  try:
    c = conn.cursor()
    c.execute(select_statement)

    return c.fetchall()

  except sqlite3.Error as e:
    print('Loading failed!')
    log_error('load', e)

    return ()

  finally:
    conn.commit()
    conn.close()


def main():
  conn = create_connection()
  if conn == None:
    log_error('main', 'No connection to database. Exiting.')
    exit(1)

  try:
    c = conn.cursor()
    print("Creating table... ")
    c.execute('''
      CREATE TABLE IF NOT EXISTS adverts (
        company TEXT,
        job_title TEXT,
        location TEXT,
        url TEXT,
        logo_url TEXT,
        post_date TEXT,
        end_date TEXT,
        PRIMARY KEY (company, job_title))
      ''')
    print("Table created!")

  except sqlite3.Error as e:
    print('Table creation failed!')
    log_error('main', e)

  finally:
    conn.commit()
    conn.close()


if __name__ == '__main__':
  main()

