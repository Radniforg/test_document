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


def document_owner(user_input = None):
    if user_input is None:
        document_number = input('Пожалуйста, введите номер документа\n')
    else:
        document_number = user_input
    for docs in documents:
        if docs["number"] == document_number:
          return docs['name']
    return "Ошибка: документ с заданным номером не найден"


def list_command():
    line = ''
    for docs in documents:
        line = line + f'{docs["type"]} "{docs["number"]}" "{docs["name"]}"\n'
    if line != '':
      return line
    else:
      return 'Ошибка: документы не обнаружены'


def shelf_list():
    second_line = ''
    for keys, values in directories.items():
        second_line = second_line + f'Полка №{keys} - {values}\n'
    if second_line != '':
      return second_line
    else:
      return 'Ошибка: полки не заданы'


def what_shelf(user_input = None):
    if user_input is None:
        document_number = input('Пожалуйста, введите номер документа\n')
    else:
        document_number = user_input
    for keys, values in directories.items():
      for doc_number in values:
        if doc_number == document_number:
          return f'Номер полки - {keys}'
    return 'Ошибка: документ с заданным номером не найден'


def add_document(type = None, number = None, owner = None, appointed_shelf = None):
    if type is None:
        doc_type = input('Пожалуйста, введите тип нового документа\n')
    else:
        doc_type = type
    if number is None:
        document_number = input('Пожалуйста, введите номер нового документа\n')
    else:
        document_number = number
    if owner is None:
        owner_name = input('Пожалуйста, введите имя владельца нового документа\n')
    else:
        owner_name = owner
    for docs in documents:
        if  docs['type'] == doc_type and docs["number"] == document_number and docs["name"] == owner_name:
            return 'Ошибка: данный документ уже существует'
    new_document = {}
    new_document['type'] = doc_type
    new_document['number'] = document_number
    new_document['name'] = owner_name
    if appointed_shelf is None:
        shelf_number = input('Пожалуйста, введите полки с новым документом\n')
    else:
        shelf_number = appointed_shelf
    if directories.get(shelf_number, 'Error') != 'Error':
        documents.append(new_document)
        directories[shelf_number].append(document_number)
        list_command()
        shelf_list()
        return f'{list_command()}\n{shelf_list()}'
    return 'Ошибка: заданная полка не существует'


def add_shelf(shelf_number = None):
    if shelf_number is None:
        shelf = input('Пожалуйста, введите номер новой полки\n')
    else:
        shelf = shelf_number
    if directories.get(shelf, 'Clear') != 'Clear':
      return 'Ошибка: заданная полка уже существует'
    directories[shelf] = []
    return shelf_list()


def doc_delete(doc_number = None):
    variable_check=0
    if doc_number is None:
        document_number = input('Пожалуйста, введите номер документа\n')
    else:
        document_number = doc_number
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
      return 'Ошибка: документ на удаление не найден'
    return f'{list_command()}\n{shelf_list()}'


def doc_move(doc_number = None, shelf_number = None):
    variable_check=0
    if doc_number is None:
        document_number = input('Пожалуйста, введите номер документа\n')
    else:
        document_number = doc_number
    if shelf_number is None:
        final_shelf = input('Пожалуйста, введите номер новой полки\n')
    else:
        final_shelf = shelf_number
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
      return 'Ошибка: документ на перемещение не найден'
    elif variable_check == 2:
      return 'Ошибка: нельзя переместить на ту же самую полку'
    elif variable_check == 3:
      return 'Ошибка: заданная полка не существует'
    return shelf_list()


def owners():
  document_list = []
  for document in directories.values():
    for document_numbers in document:
      document_list.append(document_numbers)
  for document_number in document_list:
    for docs in documents:
      if docs["number"] == document_number:
        try:
          return f'Владелец документа номер {docs["number"]} - {docs["name"]}'
        except KeyError:
          return 'Ошибка: у документа отсутствует владелец'

if __name__ == '__main__':
    user_command = input('Пожалуйста, введите пользовательскую команду\n')

    if user_command.lower() == 'p':
        print(document_owner())
    elif user_command.lower() == 'l':
        print(list_command())
    elif user_command.lower() == 's':
        print(what_shelf())
    elif user_command.lower() == 'a':
        print(add_document())
    elif user_command.lower() == 'd':
        print(doc_delete())
    elif user_command.lower() == 'm':
        print(doc_move())
    elif user_command.lower() == 'as':
        print(add_shelf())
    elif user_command.lower() == 'n':
        print(owners())
    else:
        print('Ошибка: Пользовательская команда не найдена')