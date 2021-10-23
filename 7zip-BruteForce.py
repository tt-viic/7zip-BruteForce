
import os, zipfile, sys, subprocess
from threading import Thread

reset = '\033[0m'
red = '\033[31m'
green = '\033[32m'
blue = '\x1b[38;2;40;139;168m'

def clear():
    if os.name == "posix":
        return os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        return os.system ("cls")

def main():
    print('''
 {}
            ___________________    _____  _________  ____  __._____________________  
            \_   ___ \______   \  /  _  \ \_   ___ \|    |/ _|\_   _____/\______   \ 
            /    \  \/|       _/ /  /_\  \/    \  \/|      <   |    __)_  |       _/ 
            \     \___|    |   \/    |    \     \___|    |  \  |        \ |    |   \ 
             \______  /____|_  /\____|__  /\______  /____|__ \/_______  / |____|_  / 
                    \/       \/         \/        \/        \/        \/         \/  
 {}
                                    coded by viic w {}<3{}
    
    
    
                ┌──────────────────────────────────────────────────────────┐   
                │             ¿What do you want to Brute-Force?            │   
                ├──────────────────────────────────────────────────────────┤   
                │  [1]   .7z file                                          │   
                │  [2]   .zip file                                         │   
                │  [99]  {}EXIT{}, saldrás del programa                        │   
                └──────────────────────────────────────────────────────────┘   
    
    '''.format(blue, reset, red, reset, red, reset))

    choice = input('   Opción ❯  ')
    if choice == '1':
        clear()
        sevenzip()
    elif choice == '2':
        clear()
        zip()
    elif choice == '99':
        clear()
        print('  See you soon {}<3{} !'.format(red, reset))
        exit()
    else:
        clear()
        main()

def sevenzip():
    print('''
 {}   ___________
    \_____    /__________   _____________         ___________________    _____  _________  ____  __._____________________  
         /   / \____    /  |   \______   \        \_   ___ \______   \  /  _  \ \_   ___ \|    |/ _|\_   _____/\______   \ 
        /   /    __/___/__ |   ||     ___/        /    \  \/|       _/ /  /_\  \/    \  \/|      <   |    __)_  |       _/ 
       /   /      /   /___ |   ||    |      ---   \     \___|    |   \/    |    \     \___|    |  \  |        \ |    |   \ 
      /___/      /_______ \|___||____|             \______  /____|_  /\____|__  /\______  /____|__ \/_______  / |____|_  / 
                         \/                               \/       \/         \/        \/        \/        \/         \/  
 {}
    '''.format(blue, reset))

    sevenzip = input('   Enter the exact name of the .zip file ❯  ')
    print('   ')
    dictionary = input('   Enter the exact name of the dictionary file ❯  ')
    print('   ')
    with open(dictionary, "r") as dic:
        for line in dic:
            sevenzip_password = line.rstrip('\n')
            stdout = subprocess.call(
				"7z t -p'{0}' {1}".format(sevenzip_password, sevenzip), 
				stderr=subprocess.DEVNULL, 
				stdout=subprocess.DEVNULL, 
				shell=True
			)
            if stdout == 0:
                print('[{1}+{2}} Password Found!' + ': ' + sevenzip_password + '\n' .format(green, reset))
                return
    print('{}+{} Password not found.' .format(red, reset))

def zip():
    if os.getuid() != 0: 
      print('Execute the script as {}root{}'.format(red, reset))
      sys.exit(1) 
    print('''
 {}           __________   _____________         ___________________    _____  _________  ____  __._____________________  
            \____    /  |   \______   \        \_   ___ \______   \  /  _  \ \_   ___ \|    |/ _|\_   _____/\______   \ 
              __/___/__ |   ||     ___/        /    \  \/|       _/ /  /_\  \/    \  \/|      <   |    __)_  |       _/ 
               /   /___ |   ||    |      ---   \     \___|    |   \/    |    \     \___|    |  \  |        \ |    |   \ 
              /_______ \|___||____|             \______  /____|_  /\____|__  /\______  /____|__ \/_______  / |____|_  / 
                      \/                               \/       \/         \/        \/        \/        \/         \/  
 {}
            '''.format(blue, reset))
    def extract(zipFile, zippassword):
        try:
            zipFile.extractall(pwd=zippassword)
            print('{1}+{2} Password Found!' + ': ' + zippassword + '\n' .format(green, reset))
        except:
            pass

    def zipmain():

        zipname = input('   Enter the exact name of the .zip file ❯  ')
        print('   ')
        dicname = input('   Enter the exact name of the dictionary file ❯  ')
        print('   ')
        zipFile = zipfile.ZipFile(zipname)
        zippassFile = open(dicname)
        for line in zippassFile.readlines():
            zippassword = line.strip('\n')
            t = Thread(target=extract, args=(zipFile, zippassword))
            t.start()
    if __name__ == '__main__':
        zipmain()

clear()
main()
