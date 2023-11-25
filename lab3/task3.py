import os
import shutil
import csv
import random

random_numbers = random.sample(range(0, 10001), len(os.listdir(os.path.relpath('dataset2'))))
new_names = [f'{number}.jpg' for number in random_numbers]
    

def make_dataset3() -> None:

    if os.path.isdir('dataset3'):
        shutil.rmtree('dataset3')

    old_path = os.path.relpath('dataset2')
    new_path = os.path.relpath('dataset3')
    shutil.copytree(old_path, new_path)

    old_names = os.listdir(new_path)
    
    old_relative_paths = list(map(lambda name: os.path.join(new_path, name), old_names))
    
    new_relative_paths = list(map(lambda name: os.path.join(new_path, name), new_names))

    for old_name, new_name in zip(old_relative_paths, new_relative_paths):
        os.replace(old_name, new_name)



def make_annotation3() -> None:

    old_path = os.path.relpath('dataset2')
    old_names = os.listdir(old_path)
    old_relative_paths = list(map(lambda name: os.path.join(old_path, name), old_names))

    
    new_path = os.path.relpath('dataset3')
    new_relative_paths = list(map(lambda name: os.path.join(new_path, name), new_names))

    new_absolute_paths = list(map(lambda img: os.path.join(os.path.abspath('dataset3'), img), new_names))

    with open('annotation3.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\r')

        for  absolute_path, relative_path, old_relative_path in zip(new_absolute_paths, new_relative_paths, old_relative_paths):
            if 'cat' in old_relative_path:
                name = 'cat'
            else:
                name = 'dog'
            writer.writerow([absolute_path, relative_path, name])


if __name__ == "__main__":
    make_dataset3()
    make_annotation3()


