import pandas as pd
import openpyxl
#把网页的表格写入Excel

def append_excel(data, excelname, sheetname, insert_type):
    original_file = pd.DataFrame(pd.read_excel(excelname, sheet_name=sheetname))  # 读取原数据文件和表
    original_row = original_file.shape[0]
    if insert_type == 'w':
        startrow = 1
    elif insert_type == 'a+':
        startrow = original_row + 1
    book = openpyxl.load_workbook(excelname)
    writer = pd.ExcelWriter(excelname, engine='openpyxl')
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

    # 将data数据写入Excel中
    data.to_excel(writer, sheet_name=sheetname, startrow=startrow, index=False, header=False)
    writer.save()


if __name__ == '__main__':
    df = pd.read_html("./wiki.html", encoding='utf-8', header=0)
    num = len(df)
    for i in range(num - 4):
        append_excel(df[i], './wiki_data.xlsx', 'Sheet1', 'a+')
