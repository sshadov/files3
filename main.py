
# with open("1.txt", "r+", encoding="utf8") as f1:
#     data = f1.read()
#     print(data)
#     number_of_rows1 = len(f.readlines())
#
# with open("2.txt", "r+", encoding="utf8") as f2:
#     number_of_rows2 = len(f2.readlines())
#
# def output_to_file3(files)
#
#     if number_of_rows2 > number_of_rows1:
#         print(f'{f1.name}\n {number_of_rows1}\n {f1.read})
#         print(f'{f2.name}\n {number_of_rows2}\n {f2.read})
#     else:
#         print(f'{f2.name}\n {number_of_rows2}\n {f2.read})
#         print(f'{f1.name}\n {number_of_rows1}\n {f1.read})

with open("1.txt", "r+", encoding="utf8") as f1:
    rows_f1 = 0
    text_f1 = str()
    for line in f1:
        text_f1 += line
        file_name = f1.name
        rows_f1 += 1
    out_f1 = (f'{f1.name}\n{rows_f1} \n{text_f1}')

with open("2.txt", "r+", encoding="utf8") as f2:
    rows_f2 = 0
    text_f2 = str()
    for line in f2:
        file_name = f2.name
        rows_f2 += 1
        text_f2 += line
    out_f2 = (f'{f2.name}\n{rows_f2} \n{text_f2}')

if rows_f2 < rows_f1:
    with open("3.txt", "w", encoding="utf8") as f3:
        f3.write((out_f2 + out_f1))
else:
    with open("3.txt", "w", encoding="utf8") as f3:
        f3.write((out_f1 + out_f2))

