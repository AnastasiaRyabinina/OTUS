import json
from csv import DictReader

# 1. Открываем файл .csv с помощью контекстного менеджера
with open('../Homework_1_part_2/data/books.csv', 'r', encoding='utf-8', newline='') as f:
    books = DictReader(f)

    # Итерируемся по данным и создаем список книг с нужными нам атрибутами
    list_of_books = []
    for row in books:
        book = {'title':row['Title'],'author':row['Author'],'height':row['Height']}
        list_of_books.append(book)


# 2. Открываем файл .json и грузим все данные о пользователях в список users
with open('../Homework_1_part_2/data/users.json', 'r', encoding='utf-8', newline='') as file:
    users = json.load(file)  # здесь должен быть словарь, но получется список, не поняла почему..
    # print('-----Type of users: ',type(users))


# 3. Открываем новый файл на запись, собираем в словарь нужные данные о пользователе и добавяем книгу
with open('../Homework_1_part_2/data/result.json', "w+") as ff:
    ibooks = 0
    ff.write('[\n')
    for i in users:
        if ibooks < len(list_of_books):
            my_dict = {'name':i['name'], 'gender':i['gender'], 'address':i['address'], 'books':[list_of_books[ibooks]]}
        else:
            my_dict = {'name': i['name'], 'gender': i['gender'], 'address': i['address'], 'books': []}
        json.dump(my_dict, ff, indent=4)
        ff.write(',\n')
        ibooks += 1
    ff.seek(ff.tell()-3, 0)
    ff.write('\n]')
