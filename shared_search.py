import requests

def find_domain(api_key, domain_name, login, password):
    api_url = "https://example.com/api/endpoint"  # Замените на реальный URL API
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Login": login,
        "Password": password
    }

    payload = {"domain": domain_name}

    try:
        response = requests.post(api_url, headers=headers, data=payload)
        response.raise_for_status()  # Проверка наличия ошибок в запросе

        # Обработка ответа API
        result = response.json()
        return result
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Пример использования с вводом от пользователя
api_key = "YOUR_API_KEY"  # Замените на реальный ключ API
login = input("Введите свой логин: ")
password = input("Введите свой пароль: ")
domain_name = input("Введите доменное имя: ")

result = find_domain(api_key, domain_name, login, password)

if result:
    print(f"Результат поиска для домена {domain_name}: {result}")
else:
    print("Что-то пошло не так.")
