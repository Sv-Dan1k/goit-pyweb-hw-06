import sqlite3


conn = sqlite3.connect('university.db')
cursor = conn.cursor()


def execute_query_from_file(filename, params=None):
    with open(filename, 'r') as file:
        query = file.read()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)


queries = [
    ('query_1.sql', None),
    ('query_2.sql', (1,)),  
    ('query_3.sql', (1,)),
    ('query_4.sql', None),
    ('query_5.sql', (1,)),
    ('query_6.sql', (1,)),
    ('query_7.sql', (1, 1)),
    ('query_8.sql', (1,)),
    ('query_9.sql', (1,)),
    ('query_10.sql', (1, 1))
]

for query_file, params in queries:
    print(f"Results for {query_file}:")
    execute_query_from_file(query_file, params)
    print("\n")


conn.close()