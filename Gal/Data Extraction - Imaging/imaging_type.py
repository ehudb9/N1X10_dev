from openpyxl import load_workbook

# path = 'pandas_to_excel.xlsx'


def write_to_xlsx(path, typ, row, column):
    # file = 'input.xlsx'
    # new_row = ['data1', 'data2', 'data3', 'data4']
    #
    # wb = openpyxl.load_workbook(filename=filename)
    # ws = wb['Sheet1']  # Older method was  .get_sheet_by_name('Sheet1')
    # row = ws.get_highest_row() + 1
    #
    # for col, entry in enumerate(new_row, start=1):
    #     ws.cell(row=row, column=col, value=entry)
    #
    # wb.save(file)

    # wb = load_workbook(filename=filename)
    # sheet_ranges = wb['range names']
    # print(sheet_ranges['D18'].value)

    # path = 'pandas_to_excel.xlsx'
    #
    # with pd.ExcelWriter(path) as writer:
    #     writer.book = openpyxl.load_workbook(path)
    #     df.to_excel(writer, sheet_name='new_sheet1')
    #     df2.to_excel(writer, sheet_name='new_sheet2')

    wb = load_workbook(path)
    sheets = wb.sheetnames
    dr_note = wb[sheets[4]]
    # Then update as you want it
    dr_note.cell(row=row, column=column).value = typ  # This will change the cell(2,4) to 4
    wb.save("NEW EXCEL SAMPLE.xlsx")


def imaging_type_line(filename, typ):
    # open the sample text representing the imaging doc
    doc = open(filename)

    # read the content of the file opened
    content = doc.readlines()

    # pre-proccesing, could be in another function
    fixed_content = [x.replace('\n', '') for x in content if x != '\n']

    start_of_content = fixed_content[0:15]
    index = 0
    for line in start_of_content:
        index += 1
        # makes sure it's not part of another word
        if typ+' ' in line or ' '+typ in line:
            return index
    return float('inf')


def imaging_type(filename, imaging_types):
    line_list = [float('inf')] * len(imaging_types);
    index = -1
    for typ in imaging_types:
        index += 1
        line_list[index] = imaging_type_line(filename, typ)
    return imaging_types[line_list.index(min(line_list))]



# could be improve using dictionary with values as other ways to write
imaging_types = ['XR', 'MRI', 'PET CT', 'CT', 'DOTATATE']
type1 = imaging_type('doc1.txt', imaging_types)
type2 = imaging_type('doc2.txt', imaging_types)
type3 = imaging_type('doc3.txt', imaging_types)
print(type1)
print(type2)
print(type3)

# write_to_xlsx('ac example.xlsx', type1, 19, 19)
# write_to_xlsx('ac example.xlsx', type2, 20, 19)
# write_to_xlsx('ac example.xlsx', type3, 21, 19)

