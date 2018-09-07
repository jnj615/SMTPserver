  

#This program takes in a message from a user through keyboard
#input and then forwards the file to a  mail server
#if the user inputs incorrect information the program informs
#the user and reprompts them

import sys
from socket import*

def loop(content, clientSocket):

    i=0
    while(i<len(content)):

        mailFrom = content[i]
        mailFrom = "MAIL FROM:" + mailFrom[5:]
        clientSocket.send(mailFrom.encode())

        reply = clientSocket.recv(1024).decode()
        if(reply[:3]!="250"):
            break
        i=i+1
        if(i>=len(content)):
            break


        rcptTo = content[i]
        while(rcptTo[:3]=="To:"):
            rcptTo = "RCPT TO:"+rcptTo[3:]
            clientSocket.send(rcptTo.encode())
            reply = clientSocket.recv(1024).decode()
            if(reply[:3]!="250"):
                break
            i=i+1
            if(i>=len(content)):
                break
            rcptTo = content[i]


        if(reply[:3]!="250"):
            break
        data = "DATA"
"Client.py" 265L, 6610C                                                1,0-1         Top
    return (ord(char)>64 and ord(char)<91) or (ord(char)>96 and ord(char)<123)

def c(char):
    return (ord(char)<128 and special(char) == False and SP(char)==False)

def d(char):
    return (char=='0' or char=='1' or char=='2' or char=='3' or char=='4' or
            char=='5' or char=='6' or char=='7' or char=='8' or char=='9')

def special(char):
    return (char=='<' or char=='>' or char=='(' or char==')' or char=='[' or
            char==']' or char=='\\' or char=='.' or char==',' or char==';' or
            char==':' or char=='@' or char=='"')







#-----------------------------------------------------------------------

#creates socket and sends the message to the server
def makeSocket(content):

    serverName = sys.argv[1]
    serverPort = int(sys.argv[2])
    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))

    greeting = clientSocket.recv(1024)
    helo = 'HELO ' + gethostname()
    clientSocket.send(helo.encode())
    serSentence = clientSocket.recv(1024)

    loop(content, clientSocket)

    clientSocket.close()


content = userInput()
makeSocket(content)

  

import sys
from socket import*

#Server takes in  an email from a client, processes it
#and then sends it to a forward file with its domain

#Functions for checking grammar:rcpt, checkRCPT, checkTo, mail_from_cmd, 
#checkforMAIL,checkforFROM, path, mailbox,domain, local_part, name,
#let_dig_string, let_dig, string,SP, a, c, d, special, CRFL

#Functions for checking 500 error command not recognized:
#dataCommand, rcptCommand,mailCommand, isCommand

#Function processFile: used for taking message and putting it as
#a file within the forward directory

#Function stateMachine: runs while lines are being entered. expects 
#MAIL FROM, RCPT TO(where there can be multiple RCPT COMMANDS, then
#DATA.



def rcpt(word):
    word = rcptCommand(word)
    if word == "null":
        return "null"

    word = path(word)
    if word == "null":
        return "null"

    return word


def dataCommand(word):
    if word[:4] != "DATA":
        return "null"
    else:
        word = word[4:]                 #remove "DATA" and extra space before returning word
        word = removeSpace(word)
"Server.py" 396L, 10425C                                               1,0-1         Top
            messageFile.append(message[i])
            i = i + 1

        processFile(rcptList, messageFile)
#-------------------------------------------------------------
        break


#sets up socket for accepting emails for processing,
#runs constantly. If an error occurs the server restarts 
#itself
def socketSetUp():
    try:
        serverPort = int(sys.argv[1])
        serverSocket = socket(AF_INET,SOCK_STREAM)
        serverSocket.bind(('',serverPort))
        while True:
            while True:
                serverSocket.listen(1)
                connectionSocket, addr = serverSocket.accept()
                sentence = '220 Greetings, this is ' + gethostname()
                connectionSocket.send(sentence.encode())

                hello = connectionSocket.recv(1024).decode()
                if len(hello) < 6:
                    connectionSocket.close()
                    break
                if hello[:5] != "HELO ":
                    connectionSocket.close()
                    break

                sentence = '250 ' + hello + ', pleased to meet you'

                connectionSocket.send(sentence.encode())
                stateMachine(connectionSocket)
                connectionSocket.close()
    except socket.error, e:
        print "A socket error occured and the server was restarted"
        socketSetUp()


socketSetUp()