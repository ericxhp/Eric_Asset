import xlrd

data = xlrd.open_workbook('Hercules.xlsx')
table = data.sheets()[0]
rwo_num = table.nrows
print rwo_num
for i in range[1,rwo_num]:
    data = table.row_values(i)
    cdata=[]
    for item in data:
        cdata.append(str(item))
    print cdata
