import xlrd


def readReceiversByExecl():
    data = xlrd.open_workbook('assets/receivers.xlsx')
    table = data.sheets()[0]
    # 收件人邮箱
    reveivers = table.col_values(0)[1:]
    # 发送邮件附件文件名
    attachmentNames = table.col_values(1)[1:]
    return [reveivers, attachmentNames]

def getMetaConfig():
    f = open('.meta.conf')
    lines = f.readlines()    
    dict = {}
    for line in lines:
        [k, val] = line.split(':')    
        dict[k] = val.replace('\n', '')
    
    return dict