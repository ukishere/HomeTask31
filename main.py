class Contact:

    def __init__(self, name, sirname, number, tag=False, **optional_data):
        self.name = name
        self.sirname = sirname
        self.number = number
        self.tag = tag
        self.optional_data = optional_data

    def __str__(self):
        optional_data = str()
        if len(self.optional_data) != 0:
            for item in self.optional_data.items():
                optional_data = optional_data + f'\t{item[0]} : {item[1]}\n'
            optional_data = optional_data.rstrip('\n')
        else:
            optional_data = 'Нет'

        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.sirname}\n' \
               f'Телефон: {self.number}\n' \
               f'В избранных: {(lambda tag: "Да" if tag else "Нет")(self.tag)}\n' \
               f'Дополнительная информация:\n {optional_data}'

class Phonebook:

    def __init__(self, name, contacts):
        self.name = name
        self.contacts = contacts

    def print_all(self):
        for contact in self.contacts:
            print(contact)

    def print_all_tagged(self):
        for contact in self.contacts:
            if contact.tag:
                print(contact)

    def add_new_contact(self, name, sirname, number, tag=False, **optional_data):
        contact = Contact(name, sirname, number, tag, **optional_data)
        self.contacts.append(contact)

    def delete_contact(self, number):
        for contact in self.contacts:
            if contact.number == number:
                self.contacts.remove(contact)

    def search_by_name_and_sirname(self, name, sirname):
        found = False
        for contact in self.contacts:
            if contact.name == name and contact.sirname == sirname:
                found = True
                print(contact)
                break
        if found == False:
            print('Контакт не найден')

if __name__ == '__main__':

    my_phonebook = Phonebook('My Phonebook', [])
    my_phonebook.add_new_contact('John', 'Bell', '+1 111 11 11', email='johnbell@gmail.com', telegram='@johnbell')
    my_phonebook.add_new_contact('James', 'Well', '+2 222 22 22', tag=True)
    my_phonebook.add_new_contact('Judy', 'Dell', '+3 333 33 33')

    print('Полный список контактов')
    my_phonebook.print_all()

    print('Список контактов в избранном')
    my_phonebook.print_all_tagged()

    print('Поиск контакта John Bell')
    my_phonebook.search_by_name_and_sirname('John', 'Bell')

    print('Удаление контакта John Bell')
    my_phonebook.delete_contact('+1 111 11 11')
    my_phonebook.search_by_name_and_sirname('John', 'Bell')

