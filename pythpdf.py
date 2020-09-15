import camelot

def extract_information(pdf_path):
    tables = camelot.read_pdf(pdf_path)
    return tables

def create_file(information):
    totabledict={}
    for i in range(information.n):
        table1=information[i].df
        tabledict={}
        test_keys=[]
        test_values=[]
        for k in range(0,4):
            test_keys.append(table1[0][k])
            test_values.append(table1[1][k])                  
        tabledict= {test_keys[i]: test_values[i] for i in range(len(test_keys))}
        totabledict[i]=tabledict 
    return totabledict   

def write_content(infodict):
    with open('Servicename.c ', 'w') as fp:
        for i in range(0,len(infodict)):
            fp.write("/*"+infodict[i]['Description:']+"*/"+"\n")
            if infodict[i]['Retrun Value']=='None':
                fp.write("void "+infodict[i]['Service_Name']+"();"+"\n")
            else:
                fp.write(infodict[i]['Retrun Value']+" "+infodict[i]['Service_Name']+"();"+"\n")
    
    with open('Syntax.c', 'w') as fp1:
        for i in range(0,3):
            fp1.write("/*"+infodict[i]['Description:']+"*/"+"\n")
            fp1.write(infodict[i]['Syntax']+"\n")
                

if __name__ == '__main__':
    file="Service.pdf"
    inform=extract_information(file)
    filecontent=create_file(inform)
    write_content(filecontent)






