from db_models import Authors, Quotes
from db_connection import db
from bson import ObjectId


#input_data = input("Please, insert your query::: ")

#def find_it(command, data):
#    match command:
#        case 'name':
#            query_name = Quotes.objects(name='Albert Einstein')
#            for i in query_name:
#                print(i.to_mongo())

#try:
#    work_data = input_data.split(':')
#    print(work_data[0])
#
#    find_it(work_data[0], work_data[1])
#except:
#    print('Try again...')
#

#find_it('name', 'Albert Einstein')

query_name = Quotes.objects(tags='world')
print(query_name)
print('-----------------------------')
for i in query_name:
    print(i.to_mongo())

print('---------------------------------------------------------')

query_name = Quotes.objects(author='Albert Einstein')
print(query_name)
print('-----------------------------')
for i in query_name:
    print(i.to_mongo())