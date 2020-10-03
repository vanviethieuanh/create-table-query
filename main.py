import re

path = input('path: ')
des = input('result file will save to: ')

file = open(path, 'r')
result = ''

first = True

for line in file.readlines():
    p = re.compile('^\S+$')
    if p.match(line) is not None:
        if first:
            first = False
        else:
            result += ');\n'
        result += "CREATE TABLE dbo.{table}(\n".format(table = p.match(line)[0])
    else:
        word = re.compile('\w.+?\s')
        m = word.findall(line)
        if 'chính) ' in m:
            result += ('\t' + m[0].replace(',','')+ m[-1][0:-1]+ ' NOT NULL PRIMARY KEY' +',\n')
        else:
            result += ('\t' + m[0].replace(',','') + m[-1][0:-1]+ ',\n')
    pass

result+= ');'
file.close()

write = open(des, 'w')
write.write(result)
write.close()

