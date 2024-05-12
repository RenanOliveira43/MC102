from os import system


def edit(filename, actual_txt, replace_txt):
    with open(filename, 'r') as file:
        filedata = file.read()

    filedata = filedata.replace(actual_txt, replace_txt)

    with open(filename, 'w') as file:
        file.write(filedata)


def append_text(filename, text):
    with open(filename, 'a') as file:
        file.write(text)


def pacotes_koha():
    system('wget -q -O- https://debian.koha-community.org/koha/gpg.asc | sudo apt-key add -')

    system('sudo apt-get update')

    system("echo 'deb http://debian.koha-community.org/koha stable main' | sudo tee /etc/apt/sources.list.d/koha.list")

    system('sudo apt-get update')

    system("echo 'deb http://debian.koha-community.org/koha 19.05 main' | sudo tee /etc/apt/sources.list.d/koha.list")

    system('sudo apt-get update')


def main():
    pacotes_koha()
    
    system('yes | sudo apt-get install apache2')

    system('yes | sudo apt-get install mariadb-server mariadb-client')

    system('yes | sudo apt-get install koha-common')

    system('sudo a2dismod mpm_event')

    system('yes | sudo apt-get install -f')

    edit('/etc/koha/koha-sites.conf', 'INTRAPORT="80"', 'INTRAPORT="8080"')
    
    edit('/etc/koha/koha-sites.conf', 'OPACPORT="80"', 'OPACPORT="8888"')

    # system('sudo nano /etc/koha/koha-sites.conf')
    
    system('sudo a2enmod cgi')

    system('sudo a2enmod rewrite')

    system('sudo service apache2 restart')

    system('sudo koha-create --create-db meukoha')

    system('sudo koha-translate --install pt-BR')

    append_text('/etc/apache2/ports.conf', 'Listen 8080\n')

    append_text('/etc/apache2/ports.conf', 'Listen 8888\n')

    # system('sudo nano /etc/apache2/ports.conf')

    system('sudo service apache2 restart')

    system('yes | sudo apt install net-tools') # instala 'ifconfig' se linux for novo

    print('\nUser: ')
    system("sudo xmlstarlet sel -t -v 'yazgfs/config/user' /etc/koha/sites/meukoha/koha-conf.xml")

    print('\nPassword: ')
    system("sudo xmlstarlet sel -t -v 'yazgfs/config/pass' /etc/koha/sites/meukoha/koha-conf.xml")


if __name__ == '__main__':
    main()
