import os

def getfromfile(filename):
    result = []
    with open(os.path.join('init_files',filename), "r") as fp:
        for i in fp.read().splitlines():

            tmp = i.split("\t")
            try:
                result.append(tmp)
                # result.append((eval(tmp[0]), eval(tmp[1])))
            except:
                pass


    return result

def getscript(filename):
    sql_path = "sql//"+filename +".sql"
    fd = open(sql_path, 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')
    return  sqlCommands
