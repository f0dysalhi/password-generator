#by sami

import itertools



ban = '''
                                                    '''

print('''
                    ██╗    ██╗ ██████╗ ██████╗ ██████╗ ██╗     ██╗███████╗████████╗
                    ██║    ██║██╔═══██╗██╔══██╗██╔══██╗██║     ██║██╔════╝╚══██╔══╝
                    ██║ █╗ ██║██║   ██║██████╔╝██║  ██║██║     ██║███████╗   ██║   
                    ██║███╗██║██║   ██║██╔══██╗██║  ██║██║     ██║╚════██║   ██║   
                    ╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗██║███████║   ██║   
                     ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝╚══════╝   ╚═╝   
                                                               		 
                     
''')
print('''

         SSSSSSSSSSSSSSS                                                              iiii  
      SS:::::::::::::::S                                                            i::::i 
     S:::::SSSSSS::::::S                                                             iiii
      S:::::S     SSSSSSS
      S:::::S              aaaaaaaaaaaaa    aaaaaaaaaaaaa      mmmmmmm    mmmmmmm   iiiiiii 
      S:::::S              a::::::::::::a   a::::::::::::a   mm:::::::m  m:::::::mm i:::::i 
      S::::SSSS           aaaaaaaaa:::::a  aaaaaaaaa:::::a m::::::::::mm::::::::::m i::::i 
       SS::::::SSSSS               a::::a           a::::a m::::::::::::::::::::::m i::::i 
         SSS::::::::SS      aaaaaaa:::::a    aaaaaaa:::::a m:::::mmm::::::mmm:::::m i::::i 
            SSSSSS::::S   aa::::::::::::a  aa::::::::::::a m::::m   m::::m   m::::m i::::i 
                 S:::::S a::::aaaa::::::a a::::aaaa::::::a m::::m   m::::m   m::::m i::::i 
                 S:::::Sa::::a    a:::::aa::::a    a:::::a m::::m   m::::m   m::::m i::::i 
     SSSSSSS     S:::::Sa::::a    a:::::aa::::a    a:::::a m::::m   m::::m   m::::mi::::::i
     S::::::SSSSSS:::::Sa:::::aaaa::::::aa:::::aaaa::::::a m::::m   m::::m   m::::mi::::::i
     S:::::::::::::::SS  a::::::::::aa:::aa::::::::::aa:::am::::m   m::::m   m::::mi::::::i
      SSSSSSSSSSSSSSS     aaaaaaaaaa  aaaa aaaaaaaaaa  aaaammmmmm   mmmmmm   mmmmmmiiiiiiii  

                    project :     > https://github.com/saaaami/password-generator/
''')


scale = input('>>  provide a size scale [eg: "4 to 8" = 4:8] : ')
start = int(scale.split(':')[0])
final = int(scale.split(':')[1])

use_nouse = str(input("[?] Do you want to enter personal data ? [y/N]: "))
if use_nouse == 'y':
	first_name = str(input("] Fist Name: "))
	last_name = str(input(" Last Name: "))
	birthday = str(input(" Birthday: "))
	month = str(input(" Month: "))
	year = str(input(" Year: "))
	chrs = first_name + last_name + birthday + month + year
else:
	chrs = 'abcdefghijklmnopqrstuvwxyz'
	pass

chrs_up = chrs.upper()
chrs_specials = '!\][/?.,~-=";:><@#$%&*()_+\' '
chrs_numerics = '1234567890'

file_name = input('\n\033[36m[!] Insert a name for your wordlist file: ')
arq = open(file_name, 'w')
if input('\n\033[36m[?] Do you want to use uppercase characters? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_up])
if input('\n\033[36m[?] Do you want to use special characters? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_specials])
if input('\n\033[36m[?] Do you want to use numeric characters? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_numerics])

for i in range(start, final+1):
	for j in itertools.product(chrs, repeat=i):
		temp = ''.join(j)
		print(temp)
		arq.write(temp + '\n')
arq.close()