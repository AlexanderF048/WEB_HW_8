import json
import pprint
import redis


from db_models import Authors, Quotes
from db_connection import db


# input_data = input("Please, insert your query::: ")

def find_it(command, data, red_inst=None):
    match command:
        case 'name':
            try:
                query_single_autor = Authors.objects(fullname=data).first()
                # print(query_single_autor.to_mongo())
                auth_id = query_single_autor._data['id']
                # print(auth_id)

                value_for_redis = []

                query_name = Quotes.objects(author=auth_id)
                for query_response in query_name:
                    uno_response = query_response.to_json()
                    duo_response = uno_response.encode('utf-8', errors='ignore').decode('utf-8')

                    pprint.pprint(duo_response, indent=1, width=100, sort_dicts=True)
                    value_for_redis.append(duo_response)


                red_inst.set(command+data, 'REDIS OUTPUT:::::::'+value_for_redis, ex=180)

            except:
                print('No COMMAND/AUTOR !!!')
        case 'tag':
            try:
                query_single_tag = Quotes.objects(tags=data)
                for query_response in query_single_tag:
                    print(query_response.to_mongo())
            except:
                print('No COMMAND/SINGLE TAG !!!')
        case 'tags':
            try:

                query_single_tag = Quotes.objects(tags__in=data)
                for query_response in query_single_tag:
                    print(query_response.to_mongo())
            except:
                print('No COMMAND/SINGLE TAG !!!')
        case 'exit':
            exit()
        case other:
            print('No match found !!!')


if __name__ == "__main__":
    pass
