#Задание 2
import collections

#База данных питомцев
pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        },
    },
    2: {
        "Каа": {
            "Вид питомца": "Желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        },
    },
}

# Функция для получения правильного склонения слова 'год'
def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return "года"
    else:
        return "лет"
    
# Получение информации о питомце по ID
def get_pet(ID):
 
    return pets[ID] if ID in pets.keys() else False

# Отображение списка всех питомцев
def pets_list():
    if not pets:
        print("В базе данных нет питомцев.")
        return
    
    print("\n=== СПИСОК ВСЕХ ПИТОМЦЕВ ===")
    for pet_id, pet_info in pets.items():
        pet_name = list(pet_info.keys())[0]
        pet_data = pet_info[pet_name]
        age = pet_data["Возраст питомца"]
        suffix = get_suffix(age)
        print(f"ID {pet_id}: {pet_data['Вид питомца']} '{pet_name}', "
              f"{age} {suffix}, Владелец: {pet_data['Имя владельца']}")

# Создание новой записи о питомце
def create():
    if pets:
        last_id = collections.deque(pets, maxlen=1)[0]
        new_id = last_id + 1
    else:
        new_id = 1
    
    print(f"\nДобавление нового питомца (ID: {new_id})")
    
    name = input("Введите кличку питомца: ")
    species = input("Введите вид питомца: ")
    
    while True:
        try:
            age = int(input("Введите возраст питомца: "))
            if age < 0:
                print("Возраст не может быть отрицательным!")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите число!")
    
    owner = input("Введите имя владельца: ")
    
    pets[new_id] = {
        name: {
            "Вид питомца": species,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }
    
    print(f"Питомец '{name}' успешно добавлен с ID {new_id}!")

# Чтение информации о питомце
def read():
    pets_list()
    
    try:
        pet_id = int(input("\nВведите ID питомца для просмотра: "))
    except ValueError:
        print("Ошибка! Введите числовой ID.")
        return
    
    pet_info = get_pet(pet_id)
    
    if not pet_info:
        print(f"Питомец с ID {pet_id} не найден!")
        return
    
    pet_name = list(pet_info.keys())[0]
    pet_data = pet_info[pet_name]
    age = pet_data["Возраст питомца"]
    suffix = get_suffix(age)
    
    print(f"\nЭто {pet_data['Вид питомца']} по кличке '{pet_name}'. "
          f"Возраст питомца: {age} {suffix}. "
          f"Имя владельца: {pet_data['Имя владельца']}")

# Обновление информации о питомце
def update():
    pets_list()
    
    try:
        pet_id = int(input("\nВведите ID питомца для обновления: "))
    except ValueError:
        print("Ошибка! Введите числовой ID.")
        return
    
    pet_info = get_pet(pet_id)
    
    if not pet_info:
        print(f"Питомец с ID {pet_id} не найден!")
        return
    
    pet_name = list(pet_info.keys())[0]
    current_data = pet_info[pet_name]
    
    print(f"\nОбновление информации о питомце '{pet_name}':")
    print("(оставьте поле пустым, чтобы сохранить текущее значение)")
    
    new_name = input(f"Новая кличка [{pet_name}]: ") or pet_name
    new_species = input(f"Новый вид [{current_data['Вид питомца']}]: ") or current_data['Вид питомца']
    
    while True:
        new_age = input(f"Новый возраст [{current_data['Возраст питомца']}]: ")
        if not new_age:
            new_age = current_data['Возраст питомца']
            break
        try:
            new_age = int(new_age)
            if new_age < 0:
                print("Возраст не может быть отрицательным!")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите число!")
    
    new_owner = input(f"Новый владелец [{current_data['Имя владельца']}]: ") or current_data['Имя владельца']
    
    # Удаляем старую запись и создаем новую
    del pets[pet_id]
    
    # Если изменили кличку, создаем новую запись
    pets[pet_id] = {
        new_name: {
            "Вид питомца": new_species,
            "Возраст питомца": new_age,
            "Имя владельца": new_owner
        }
    }
    
    print(f"Информация о питомце обновлена!")

# Удаление записи о питомце
def delete():
    pets_list()
    
    try:
        pet_id = int(input("\nВведите ID питомца для удаления: "))
    except ValueError:
        print("Ошибка! Введите числовой ID.")
        return
    
    pet_info = get_pet(pet_id)
    
    if not pet_info:
        print(f"Питомец с ID {pet_id} не найден!")
        return
    
    pet_name = list(pet_info.keys())[0]
    
    confirm = input(f"Вы уверены, что хотите удалить питомца '{pet_name}'? (да/нет): ")
    if confirm.lower() == 'да':
        del pets[pet_id]
        print(f"Питомец '{pet_name}' удален из базы данных!")
    else:
        print("Удаление отменено.")

# Основная программа
def main():
    print("=== ВЕТЕРИНАРНАЯ КЛИНИКА - СИСТЕМА УПРАВЛЕНИЯ БАЗОЙ ДАННЫХ ===")
    print("Доступные команды: create, read, update, delete, list, stop")
    
    command = ""
    while command != 'stop':
        print("\n" + "="*50)
        command = input("Введите команду: ").lower()
        
        if command == 'create':
            create()
        elif command == 'read':
            read()
        elif command == 'update':
            update()
        elif command == 'delete':
            delete()
        elif command == 'list':
            pets_list()
        elif command == 'stop':
            print("Работа программы завершена.")
        else:
            print("Неизвестная команда! Доступные команды: create, read, update, delete, list, stop")

#Запуск программы
if __name__ == "__main__":
    main()
