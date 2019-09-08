import datetime
import time


class CheckTime:
    def __init__(self, path):
        self.file = open(path)

    def __enter__(self):
        now = datetime.datetime.now()
        lines = self.file.readlines()
        counter = 0
        search = input('Введите букву поиска ')
        for line in lines:
            for i in line:
                if search == i:
                    counter += 1
        now2 = datetime.datetime.now()
        time_work = time.process_time()
        out = {'Время начала работы': now.time(), 'Время завершения работы': now2.time(),
            'Время затраченное на работу': time_work, 'Данная буква в тексте встречается ': counter}
        return out

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with CheckTime('war_and_peace.txt') as f:
    print(f)
