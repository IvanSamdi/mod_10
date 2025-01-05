from datetime import datetime
import multiprocessing


def read_info(name):
    all_date = []
    with open(name, 'r', encoding="utf-8") as file:
        while True:
            string = file.readline()
            if string == '': break
            all_date.append(int(string))


filenames = [f'./file {number}.txt' for number in range(1, 5)]
"""
# Линейный
start = datetime.now()
for file in filenames:
    read_info(file)
end = datetime.now()
print(f'{end - start} (линейный)')

"""

# Многопроцессорный
if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.now()
        pool.map(read_info, filenames)
        end = datetime.now()
        print(f'{end - start} (многопроцессорный)')
