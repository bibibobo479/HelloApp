import random

def generate_random_list(n):
    journal_number = 24
    max_val = journal_number * 100
    return [random.randint(5, max_val) for _ in range(n)]

if __name__ == "__main__":
    journal_number = 24
    n = journal_number + 10
    random_list = generate_random_list(n)
    print(f"Сгенерировано {n} чисел в диапазоне 5..{journal_number*100}:")
    print(random_list)
