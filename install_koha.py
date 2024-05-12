import subprocess as sp
import sys
import socket


COLOR_PASSED = '\033[92m'
COLOR_END = '\033[0m'


def edit(filename, actual_txt, replace_txt):
    with open(filename, "r") as file:
        filedata = file.read()

    filedata = filedata.replace(actual_txt, replace_txt)

    with open(filename, "w") as file:
        file.write(filedata)


def append_text(filename, text):
    with open(filename, "a") as file:
        file.write(text)


def local_ip():
    return socket.gethostbyname(socket.gethostname())


def ip():
    return (([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0]


def comands():
    cmd_list = [
        "wget -q -O- https://debian.koha-community.org/koha/gpg.asc | sudo apt-key add -",
        "sudo apt-get update",
        "echo 'deb http://debian.koha-community.org/koha stable main' | sudo tee /etc/apt/sources.list.d/koha.list",
        "sudo apt-get update",
        "echo 'deb http://debian.koha-community.org/koha 19.05 main' | sudo tee /etc/apt/sources.list.d/koha.list",
        "sudo apt-get update",
        "yes | sudo apt-get install apache2",
        "yes | sudo apt-get install mariadb-server mariadb-client",
        "yes | sudo apt-get install koha-common",
        "sudo a2dismod mpm_event",
        "yes | sudo apt-get install -f",
        "edit",
        "sudo a2enmod cgi",
        "sudo a2enmod rewrite",
        "sudo service apache2 restart",
        "sudo koha-create --create-db meukoha",
        "sudo koha-translate --install pt-BR",
        "append",
        "sudo service apache2 restart",
        "yes | sudo apt install net-tools",
    ]

    total_commands = len(cmd_list)
    progress_width = 25

    for i, cmd in enumerate(cmd_list):
        if cmd == "edit":
            edit("/etc/koha/koha-sites.conf", 'INTRAPORT="80"', 'INTRAPORT="8080"')
            edit("/etc/koha/koha-sites.conf", 'OPACPORT="80"', 'OPACPORT="8888"')
        elif cmd == "append":
            append_text("/etc/apache2/ports.conf", "Listen 8080\n")
            append_text("/etc/apache2/ports.conf", "Listen 8888\n")
        else:
            sp.check_output(cmd, stderr=sp.STDOUT, shell=True)

        progress = int((i + 1) / total_commands * progress_width)
        bar = "[" + "#" * progress + "." * (progress_width - progress) + "]"
        sys.stdout.write(f"\rProgresso: {bar} [{((i + 1) / total_commands * 100):.2f}%]")
        sys.stdout.flush()

    print(f"\n{COLOR_PASSED}Instalação bem sucedida\n{COLOR_END}")
    
    
def main():   
    comands()
        
    print(f"Continue a configuração localmente em: {local_ip()}:8080")
    print(f"Ou remotamente em: {ip()}:8080\n")

    user = (sp.check_output("sudo xmlstarlet sel -t -v 'yazgfs/config/user' /etc/koha/sites/meukoha/koha-conf.xml", stderr=sp.STDOUT, shell=True)).decode('utf-8').strip("'")
    print(f"Usuario: {user}")

    password = (sp.check_output("sudo xmlstarlet sel -t -v 'yazgfs/config/pass' /etc/koha/sites/meukoha/koha-conf.xml", stderr=sp.STDOUT, shell=True)).decode('utf-8').strip("'")
    print(f"Senha: {password}")

    print()


if __name__ == "__main__":
    main()
