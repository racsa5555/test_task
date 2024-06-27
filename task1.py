import re

def verify_user_input(test_text, list_keys):
    pattern = re.compile(r'{(.*?)}')
    matches = pattern.findall(test_text)
    res = ''
    for match in matches:
        if match not in list_keys:
            res+= f"Некорректный ключ {match}\n"
    
    lines = test_text.splitlines()
    for _, line in enumerate(lines, start=1):
        if line.count('{') != line.count('}'):
            words = line.split()
            for word in words:
                if word.count('{') != word.count('}'):
                    res+= f'Неверный формат: {word}'
    if not res:
        return 'Все тесты пройдены'

test_text = '''{name}, ваша запись изменена:
{day_month} в {start_time}
{master}
Услуги:
{services}
управление записью '''
list_keys = ['name', 'day_month', 'day_of_week', 'start_time', 'end_time', 'master', 'services']

result = verify_user_input(test_text, list_keys)
print(result)
