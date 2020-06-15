from doc.logger_script import logger

documents = [{
    "type": "passport",
    "number": "2207 876234",
    "name": "Василий Гупкин"
}, {
    "type": "invoice",
    "number": "11-2",
    "name": "Геннадий Покемонов"
}, {
    "type": "insurance",
    "number": "10006",
    "name": "Аристарх Павлов"
}]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}

@logger('log/')
def document_owner():
    document_number = input('Пожалуйста, введите номер документа\n')
    for docs in documents:
        if docs["number"] == document_number:
          print(docs["name"])
          return None
    print("Ошибка: документ с заданным номером не найден")

@logger('log/')
def list_command():
    line = ''
    for docs in documents:
        line = line + f'{docs["type"]} "{docs["number"]}" "{docs["name"]}"\n'
    if line != '':
      print(line)
      return None
    else:
      print('Ошибка: документы не обнаружены')


@logger('log/')
def shelf_list():
    second_line = ''
    for keys, values in directories.items():
        second_line = second_line + f'Полка №{keys} - {values}\n'
    if second_line != '':
      print(second_line)
      return None
    else:
      print('Ошибка: полки не заданы')


@logger('log/')
def what_shelf():
    document_number = input('Пожалуйста, введите номер документа\n')
    for keys, values in directories.items():
      for doc_number in values:
        if doc_number == document_number:
          print(f'Номер полки - {keys}')
          return None
    print('Ошибка: документ с заданным номером не найден')


@logger('log/')
def add_document():
  doc_type = input('Пожалуйста, введите тип нового документа\n')
  document_number = input('Пожалуйста, введите номер нового документа\n')
  owner_name = input('Пожалуйста, введите имя владельца нового документа\n')
  for docs in documents:
      if  docs['type'] == doc_type and docs["number"] == document_number and docs["name"] == owner_name:
        print('Ошибка: данный документ уже существует')
        return None
  new_document = {}
  new_document['type'] = doc_type
  new_document['number'] = document_number
  new_document['name'] = owner_name
  shelf_number = input('Пожалуйста, введите полки с новым документом\n')
  if directories.get(shelf_number, 'Error') != 'Error':
    documents.append(new_document)
    directories[shelf_number].append(document_number)
    list_command()
    shelf_list()
    return None
  print('Ошибка: заданная полка не существует')


@logger('log/')
def add_shelf():
    shelf = input('Пожалуйста, введите номер новой полки\n')
    if directories.get(shelf, 'Clear') != 'Clear':
      print('Ошибка: заданная полка уже существует')
      return None
    directories[shelf] = []
    shelf_list()


@logger('log/')
def doc_delete():
    variable_check=0
    document_number = input('Пожалуйста, введите номер документа\n')
    for docs in documents:
        if docs["number"] == document_number:
            del (documents[documents.index(docs)])
            variable_check = 1
    for shelf_content in directories.values():
        for doc_on_shelf in shelf_content:
            if doc_on_shelf == document_number:
              del (shelf_content[shelf_content.index(document_number)])
              variable_check = 1
    if variable_check == 0:
      print('Ошибка: документ на удаление не найден')
      return None
    list_command()
    shelf_list()



@logger('log/')
def doc_move():
    variable_check=0
    document_number = input('Пожалуйста, введите номер документа\n')
    final_shelf = input('Пожалуйста, введите номер новой полки\n')
    if directories.get(final_shelf, 'Clear') != 'Clear':
      for shelf_number, shelf_content in directories.items():
        if variable_check == 2:
          break
        else:
          for doc_on_shelf in shelf_content:
           if doc_on_shelf == document_number:
              if shelf_number == final_shelf:
                variable_check = 2
                break 
              else:
                del(shelf_content[shelf_content.index(document_number)])
                variable_check = 1
      directories[final_shelf].append(document_number)
    else:
      variable_check = 3
    if variable_check == 0:
      print('Ошибка: документ на перемещение не найден')
      return None
    elif variable_check == 2:
      print('Ошибка: нельзя переместить на ту же самую полку')
      return None
    elif variable_check == 3:
      print('Ошибка: заданная полка не существует')
      return None
    shelf_list()


@logger('log/')
def owners():
  document_list = []
  for document in directories.values():
    for document_numbers in document:
      document_list.append(document_numbers)
  for document_number in document_list:
    for docs in documents:
      if docs["number"] == document_number:
        try:
          print(f'Владелец документа номер {docs["number"]} - {docs["name"]}')
        except KeyError:
          print('Ошибка: у документа отсутствует владелец')


user_command = input('Пожалуйста, введите пользовательскую команду\n')

if user_command.lower() == 'p':
  document_owner()
elif user_command.lower() == 'l':
  list_command()
elif user_command.lower() == 's':
  what_shelf()
elif user_command.lower() == 'a':
  add_document()
elif user_command.lower() == 'd':
  doc_delete()
elif user_command.lower() == 'm':
  doc_move()
elif user_command.lower() == 'as':
  add_shelf()
elif user_command.lower() == 'n':
  owners()
else:
  print('Ошибка: Пользовательская команда не найдена')