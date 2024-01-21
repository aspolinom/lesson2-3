import requests

nameUrl = "https://playground.learnqa.ru/ajax/api/compare_query_type"
method_get = {"method":"GET"}
method_post = {"method":"POST"}
method_delete = {"method":"DELETE"}
method_put = {"method":"PUT"}
method_patch = {"method":"PATCH"}

method_massiv = [method_get,method_post,method_delete,method_put,method_patch]

print('Работа через метод GET:')
for met in method_massiv:
    reasponce = requests.get(nameUrl,params = met)
    print(met["method"],' ответ: ',reasponce.text)
print()

print('Работа через метод POST:')
for met in method_massiv:
    reasponce = requests.post(nameUrl,data = met)
    print(met["method"],' ответ: ',reasponce.text)
print()

print('Работа через метод DELETE:')
for met in method_massiv:
    reasponce = requests.delete(nameUrl,data = met)
    print(met["method"],' ответ: ',reasponce.text)
print()

print('Работа через метод PUT:')
for met in method_massiv:
    reasponce = requests.put(nameUrl,data = met)
    print(met["method"],' ответ: ',reasponce.text)
print()

print('Работа через метод PATH:')
for met in method_massiv:
    reasponce = requests.patch(nameUrl,data = met)
    print(met["method"],' ответ: ',reasponce.text)
