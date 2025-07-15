import random
from datetime import datetime, timedelta

def generate_russian_fake_person():
    first_names_male = ["Александр", "Дмитрий", "Максим", "Сергей", "Андрей", "Алексей", "Иван", "Николай", "Евгений", "Петр"]
    first_names_female = ["Анастасия", "Елена", "Мария", "Анна", "Алина", "Виктория", "Екатерина", "Ольга", "Юлия", "Людмила"]
    last_names = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Попов", "Васильев", "Соколов", "Лебедев", "Козлов", "Новиков"]
    patronymics = ["Иванович", "Петрович", "Сидорович", "Кузнечиков", "Попович", "Васильевич", "Соколович", "Лебедевич", "Козлов", "Новиков"]

    gender = random.choice(["male", "female"])
    if gender == "male":
        first_name = random.choice(first_names_male)
    else:
        first_name = random.choice(first_names_female)
    last_name = random.choice(last_names)
    patronymic = random.choice(patronymics)

    start_date = datetime(1945, 1, 1)
    end_date = datetime(2003, 12, 31)
    birth_date = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))

    age = (datetime.now() - birth_date).days // 365

    return {
        "first_name": first_name,
        "last_name": last_name,
        "patronymic": patronymic,
        "birth_date": birth_date.strftime("%d.%m.%Y"),
        "age": age,
        "gender": gender
    }

# Example usage
fake_person = generate_russian_fake_person()
print("First Name:", fake_person["first_name"])
print("Last Name:", fake_person["last_name"])
print("Patronymic:", fake_person["patronymic"])
print("Birth Date:", fake_person["birth_date"])
print("Age:", fake_person["age"])
print("Gender:", fake_person["gender"])