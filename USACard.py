import random

def generate_fake_card():
    # Generate a random card number
    card_number = ''.join(str(random.randint(0, 9)) for _ in range(16))
    
    # Generate a random owner name
    owner_name = ' '.join(random.choice(['John', 'Jane', 'David', 'Sarah', 'Michael', 'Emily']) for _ in range(2))
    
    # Generate a random expiration date
    expiration_date = f"{random.randint(1, 12):02}/{random.randint(2023, 2030):02}"
    
    # Generate a random CVC (Card Verification Code)
    cvc = ''.join(str(random.randint(0, 9)) for _ in range(3))
    
    return card_number, owner_name, expiration_date, cvc

# Generate and print 10 fake bank cards
for _ in range(10):
    card_number, owner_name, expiration_date, cvc = generate_fake_card()
    print(f"Card Number: {card_number}, Owner: {owner_name}, Expiration: {expiration_date}, CVC: {cvc}")