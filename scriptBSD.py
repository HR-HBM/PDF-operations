import os
import img2pdf
import re

chapter = 1

while chapter <= 10:

    input_path = f'C:/Users/HR/Downloads/bungou-stray-dogs_c001 _ c010/{chapter}'
    output_path = f'BSD{chapter}.pdf'

    jpg_files = [os.path.join(input_path, i) for i in os.listdir(input_path) if i.endswith(".jpg")]
    jpg_files.sort(key=lambda x: int(re.sub(r'\D', '', x.split('.')[0])))
    with open(output_path, 'wb') as file:
        file.write(img2pdf.convert(jpg_files))

    print(f"PDF {output_path} successfully created.")

    chapter += 1
