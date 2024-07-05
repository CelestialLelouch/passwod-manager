from random import randrange;


def _shifter(cypher:int, string: str):
    if len(string) == 0 :
        print('INVALID STRING INPUT')
    else:
        output = ''
        for a in string:
            output +=chr(ord(a) + cypher)
        return output;


def _shifter(cypher:int, string: str):
    if len(string) == 0 :
        print('INVALID STRING INPUT')
    else:
        output = ''
        for a in string:
            output +=chr(ord(a) - cypher)
        return output;  

def generate_password(max: int)-> str:
    values = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    password = ''
    for i in range(max):
        index = randrange(0, 88)
        password += values[index]
    return password;
    


def _getcypher():
    try:
        with open('safe_code.txt', 'r') as file:
            shifter = list(file.read());
            sum = 0;
            for i in range(len(shifter)):
                sum += int(shifter[i]);
        return sum;
     
    except:
        print("Failed to generate password")
        return 0


def check_code(code: str):
    with open('safe_code.txt', 'r') as file:
        sf_code = file.read()
        if code == sf_code:
            return True
        else:
            return False

def save_password(file_path: str ,platform: str, username:str, password: str):
    with open(file_path, 'a') as file :
        data = '\n \n MY ACCOUNT FOR: '+platform + '\n username: '+username +'\n encry-password: '+ password
        file.write('\n'+data);

def read_passwords():
    with open('passwords.txt', 'r') as file:
        content = file.read()
    return content;
