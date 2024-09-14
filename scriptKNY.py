# import os
# import img2pdf
#
# chapter = 1
# outputPath = f"KNY{chapter}.pdf"
# inputPath = f'C:/Users/HR/Downloads/kimetsu-no-yai/{chapter}'
#
# with open(outputPath, "wb") as file:
#     file.write(img2pdf.convert([i for i in os.listdir(inputPath) if i.endswith(".jpg")])) # Change the file directory accordingly

import os
import img2pdf
import re

chapter = 1

while chapter <= 11:

    input_path = f'C:/Users/HR/Downloads/kimetsu-no-yaiba_c011 _ c020/{chapter}'
    output_path = f'KNY{chapter}.pdf'

    jpg_files = [os.path.join(input_path, i) for i in os.listdir(input_path) if i.endswith(".jpg")]
    jpg_files.sort(key=lambda x: int(re.sub(r'\D', '', x.split('.')[0])))
    with open(output_path, 'wb') as file:
        file.write(img2pdf.convert(jpg_files))

    print(f"PDF {output_path} successfully created.")

    # try:
    #     jpg_files = [os.path.join(input_path, i) for i in os.listdir(input_path) if i.endswith(".jpg")]
    #
    #     with open(output_path, 'wb') as file:
    #         file.write(img2pdf.convert(jpg_files))
    #
    #     print(f"PDF {output_path} successfully created.")
    #
    # except FileNotFoundError as e:
    #     print(f"FileNotFoundError: {e}")
    #
    # except Exception as e:
    #     print(f"An error occurred: {e}")

    chapter += 1
