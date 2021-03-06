"""
# Drawings From Quick, Draw!
It is a python file that uses quickdraw API for finding random drawings.
## Output:
An ndjson file which includes 20(number_of_drawings) simplified drawing data with random 60 categories.
"""

from quickdraw import QuickDrawData
import ndjson
import random


file_path = "./googleqd_categories"


def open_and_read(file_path):
    # file path is the path of the file as a string.
    object_list = []
    with open(file_path) as f:
        for line in f:
            if line != "\n":
                new_line = line.rstrip("\n")
                object_list.append(new_line)

    return object_list


qd_categories = open_and_read(file_path)
number_of_categories_to_subsample = 10

#qd_categories_subsample = random.sample(qd_categories, number_of_categories_to_subsample)
qd_categories_subsample =  random.sample(qd_categories, number_of_categories_to_subsample)
print(qd_categories_subsample)

for category in qd_categories_subsample:
    sketch_name = category
    number_of_drawings = 1
    qd = QuickDrawData()
    doodle = qd.get_drawing(sketch_name)
    drawing_list = []
    all_keys = []
    with open("./ndjson_files/10_test/" + sketch_name + "_simplified_qd.ndjson", 'w') as f:
        writer = ndjson.writer(f, ensure_ascii=False)
        for i in range(number_of_drawings):
            while doodle.recognized is False or doodle.key_id in all_keys:
                doodle = qd.get_drawing(sketch_name)
            drawing_list.append(doodle)
            drawing_map = {"word": sketch_name, "key_id": doodle.key_id, "drawing": doodle.image_data}
            if len(all_keys) > 0:
                all_keys.append(doodle.key_id)
            else:
                all_keys = [doodle.key_id]
            writer.writerow(drawing_map)