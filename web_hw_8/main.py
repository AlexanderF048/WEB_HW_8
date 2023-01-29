from bson import ObjectId
import redis

from json_load import get_authors_json, get_quotes_json
from db_models import Authors, Quotes
from search import find_it
from db_connection import db  # To allow script to connect to db - shouldn`t be used in main.py

if __name__ == "__main__":

    red = redis.Redis(host="127.0.0.1", port=6379, password=None)  # С активированным poetry shell НЕТ ПОДКЛЮЧЕНИЯ!

    red.set('foo', 'bar')

    test = red.get('fott')
    print(test)

    while True:

        input_data = input("Please, insert your query::: ")
        try:
            pre_data = input_data.split(':')
            print(pre_data)

            if ',' in pre_data[1]:
                work_data = []
                work_data.append(pre_data[0])
                for i in pre_data[1].split(','):
                    work_data.append(i)

                print(work_data)
            else:
                work_data = pre_data
                print(work_data)

            if len(work_data) == 0 or len(work_data) == 1:
                print('test1')
                raise Exception()
            elif len(work_data) == 2:
                print('test2')
                try_flow = red.get(work_data[0] + work_data[1])
                if try_flow:
                    print(try_flow)
                else:
                    find_it(work_data[0], work_data[1], red)
            elif 5 > len(work_data) > 2:
                print('test3')
                print(work_data[1:])
                find_it(work_data[0], work_data[1:])
            else:
                raise Exception()
        except:
            print('Try again...')
