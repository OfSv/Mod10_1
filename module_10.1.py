# "Создание потоков"
# Задача "Потоковая запись в файлы"

# Импорты необходимых модулей и функций
import time, threading

# Объявление функции write_words,
# где word_count - количество записываемых слов,
# а file_name - название файла, куда будут записываться слова
def wite_words(word_count, file_name):
    word_num = 0
    with open(file_name, 'a', encoding='utf-8') as file:
        for word_num in range(word_count):
            word_num += 1
            file.write(f'Какое-то слово № {word_num}\n')
            time.sleep(0.1)
    return print(f'Завершилась запись в файл {file_name}')

# Взятие текущего времени
t0 = time.time()

# Запуск функций с аргументами из задачи
wite_words(10,'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

# Взятие текущего времени
t1 = time.time()

# Вывод разницы начала и конца работы функций
print(t1-t0)

# Взятие текущего времени
t0 = time.time()

# Создание и запуск потоков с аргументами из задачи

thread1 = threading.Thread(target=wite_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=wite_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=wite_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=wite_words, args=(100, 'example8.txt'))

thread1.start() 
thread2.start() 
thread3.start() 
thread4.start() 

thread1.join()
thread2.join()
thread3.join()
thread4.join() 

# Взятие текущего времени
t1 = time.time()
# Вывод разницы начала и конца работы потоков
print(t1-t0)
