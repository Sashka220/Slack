import random
import string

def generate_russian_fake_addresses(num_addresses):
    street_names = ['ул.', 'пр.', 'пл.', 'пер.', 'бульвар', 'набережная']
    street_types = ['Ленина', 'Гоголя', 'Мира', 'Кирова', 'Октября', 'Садовая']
    cities = ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Нижний Новгород', 'Казань']
    address_list = []

    for _ in range(num_addresses):
        street_name = random.choice(street_names)
        street_type = random.choice(street_types)
        house_number = str(random.randint(1, 100))
        city = random.choice(cities)
        address = f"{street_name} {street_type}, {house_number}, {city}"
        address_list.append(address)

    return address_list

# Example usage:
num_addresses = 5
fake_addresses = generate_russian_fake_addresses(num_addresses)
print(fake_addresses)