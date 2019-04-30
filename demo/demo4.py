
import os

def main():
    filePath = '/home/ck/images/person_list.txt'
    personList = getPersonList(filePath)

    print(personList)

    for person in personList:
        print(person.strip('\n'))

    createFolder('/home/ck/images/caokai')

# 读取文件内容
def getPersonList(filePath):
    person_list = []

    with open(filePath,'r',encoding='utf-8') as f:
        for personName in f.readlines():
            person_list.append(personName)

    return person_list

def createFolder(folderPath):
    if not os.path.exists(folderPath):
        os.mkdir(folderPath)


if __name__ == '__main__':
    main()