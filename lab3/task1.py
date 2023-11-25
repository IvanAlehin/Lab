import os
import csv
from typing import List

def get_absolute_path(name: str) -> List[str]:
    """
    Данная функция возвращает список абсолютных путей для всех изображений 
    определенного имени животного, переданного в функцию
    """
    name_absolute_path=os.path.abspath(f"dataset/{name}")
    image_names = os.listdir(name_absolute_path)

    image_absolute_paths = list(map(lambda img: os.path.join(name_absolute_path, img), image_names))
    
    return image_absolute_paths

def get_relative_path(name: str) -> List[str]:
    """
    Данная функция возвращает список относительных путей для всех изображений 
    определенного имени животного, переданного в функцию
    """
    name_relative_path=os.path.relpath(f"dataset/{name}")
    image_names = os.listdir(name_relative_path)

    image_relative_paths = list(map(lambda img: os.path.join(name_relative_path, img), image_names))

    return image_relative_paths
    
def make_annotation() -> None:
    cat='cat'
    dog='dog'
    
    cat_absolute_paths = get_absolute_path(cat)
    cat_relative_paths = get_relative_path(cat)
    dog_absolute_paths = get_absolute_path(dog)
    dog_relative_paths = get_relative_path(dog)

    with open('annotation.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\r')

        for absolute_path, relative_path in zip(cat_absolute_paths, cat_relative_paths):
            writer.writerow([absolute_path, relative_path, cat])

        for absolute_path, relative_path in zip(dog_absolute_paths, dog_relative_paths):
            writer.writerow([absolute_path, relative_path, dog])



