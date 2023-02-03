from datetime import datetime

def logger(data, info=None):
    dt = datetime.now()
    with open('Seminar008/log.csv', 'a', encoding='utf-8') as p:
        p.write(f'{dt}; {info}; {data}\n')