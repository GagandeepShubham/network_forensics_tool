import sqlite3
import pdb
import os
def printProfile(skypeDB):
    #os.chdir("C:\Users\GOPI\Desktop")
    conn=sqlite3.connect(skypeDB)
    c = conn.cursor()
    os.chdir("C:\Users\HP 250 G5\Desktop")
    fname=raw_input("Enter the filename u want to save the Info. :")
    f=open(fname+".txt","w+")

    c.execute("SELECT fullname, skypename, city, country FROM Accounts;")
    for row in c:
        print '[*] -- Found Account --'
        print '[+] User: '+str(row[0])
        print '[+] Skype Username: '+str(row[1])
        print '[+] Location: '+str(row[2])+','+str(row[3])
        f.write('\n\n[*] -- Found Account --'+'\n[+] User: '+str(row[0])+'\n[+] Skype Username: '+str(row[1])+'\n[+] Location: '+str(row[2])+','+str(row[3]))
        

def main():
    skypeDB="C:\Users\HP 250 G5\Desktop\PRJT(FORENSICS_TOOL)\DATABASES\main.db"
    printProfile(skypeDB)
#if __name__ == "__main__":
 #   main()
