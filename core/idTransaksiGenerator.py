import random

def generate_id_transaksi():
    random_number = random.randint(100000, 999999)
    generate_id = f"TSJ{random_number}"
    return generate_id


