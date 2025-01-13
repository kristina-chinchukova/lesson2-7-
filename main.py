def  custom_write(file_name, strings):
    file_name=f'{file_name}.txt'
    file=open(file_name, 'a',encoding='utf-8')
    a=0
    strings_positions={}
    for i in strings:
        strings[a]=strings[a]+'\n'
        b=file.tell()
        file.write(strings[a])
        a=a+1
        p=(a,b)
        strings_positions[p]=strings[a-1]
    return strings_positions



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)



