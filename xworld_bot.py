import random

BOT_VERSION = 7

def wrd_count(user_inpt):
    if len(user_inpt) > 0:
            if user_inpt[0] == ' ':
                        x = 0
            else:
                x = 1
            for i in range(len(user_inpt)):
                if (user_inpt[i] == ' ' and  user_inpt[i+1] != ' '):
                    x += 1
            return(x)  
    else:
            return(0)
 
def calc(s):
   
    tokens = []
    x = 0
    for c in s:
        if (c != '+' and c != '-' and c != '*' and c != '/'):
            x = x*10 + float(c)
        else:
            tokens.append(float(x))
            tokens.append(c)
            x = 0
    tokens.append(float(x))
 
    i = 0
    result = []
    while i < len(tokens):
        if tokens[i] == '*' or tokens[i] == '/':
            num1 = result.pop()
            num2 = tokens[i+1]
            result.append(num1 * num2 if tokens[i] == '*' else num1 / num2)
            i += 2
        else:
            result.append(tokens[i])
            i += 1
 
    tokens = result
    result = []
    i = 0
    while i < len(tokens):
        if tokens[i] == '+' or tokens[i] == '-':
            num1 = result.pop()
            num2 = tokens[i+1]
            result.append(num1 + num2 if tokens[i] == '+' else num1 - num2)
            i += 2
        else:
            result.append(tokens[i])
            i += 1
 
    return(result[0])
 
def num_sys(s, k):
 
    f = 0
    ind = int(k)
    res = 0
    dgr = len(s)-1
   
    for c in s:
        if (c.lower()) == 'a':
            x = 10
            if x >= ind:
                f += 1
                break
            else:
                res = res + x * (ind ** dgr)
                dgr -= 1
        elif (c.lower()) == 'b':
            x = 11
            if x >= ind:
                f += 1
                break
            else:
                res = res + x * (ind ** dgr)
                dgr -= 1
        elif (c.lower()) == 'c':
            x = 12
            if x >= ind:
                f += 1
                break
            else:
                res = res + x * (ind ** dgr)
                dgr -= 1
        elif (c.lower()) == 'd':
            x = 13
            if x >= ind:
                f += 1
                break
            else:
                res = res + x * (ind ** dgr)
                dgr -= 1
        elif (c.lower()) == 'e':
            x = 14
            if x >= ind:
                f += 1
                break
            else:
                res = res + x * (ind ** dgr)
                dgr -= 1
        elif (c.lower()) == 'f':
            x = 15
            if x >= ind:
                f += 1
                break
            else:
                res = res + x * (ind ** dgr)
                dgr -= 1
        else:
            x = int(c)
            if x >= ind:
                f += 1
                break
            else:
                res = res + x * (ind ** dgr)
                dgr -= 1
    if f == 0:
        return(res)
    else:
        return("Wrong entry")
 
 
 
def handle_request(request):
 
    results = None
 
    if (request.lower()) == "hello" or (request.lower()) == "hi":
        r = random.randint(1, 9)
        if r < 3:
            results = ["Hello!"]
        elif r > 6:
            results = ["Hi!"]
        else:
            results = ["Glade to see you!"]
   
    elif (request.lower()) == "bye" or (request.lower()) == "goodbye":
        r = random.randint(1, 8)
        if r < 4:
            results = ["Goodbye"]
        else:
            results = ["See you later"]
 
    elif (request.lower()) == "word counter":
        user_input = input("Write the text: ")
        results = [wrd_count(user_input)]
           
    elif (request.lower()) == "symbol counter":
        user_input = input("write the text: ")
        results = [len(user_input)]
 
    elif (request.lower()) == "weather":
        results = ["https://www.gismeteo.ru/weather-penza-4445/"]
 
    elif (request.lower()) == "twitch":
        results = ["https://www.twitch.tv/directory/game/Dota%202"]
 
    elif (request.lower()) == "calculator" or (request.lower()) == "calc":
        user_input = input("Write the math expression: ")
        results = [calc(user_input)]
 
    elif (request.lower()) == "translation nums":
        user_input1 = input("Index of the system: ")
        user_input2 = input("Number: ")
        results = [num_sys(user_input2, user_input1)]
 
    elif (request.lower()) == "version":
        results = [str(BOT_VERSION)]
 
    elif (request.lower()) == "options":
        results = []
        results.append("You can:")
        results.append("- Count the number of words (write 'word counter')")
        results.append("- Count the number of symbols (write 'symbol counter')")
        results.append("- Check the weather (write 'weather')")
        results.append("- Go to twitch (write 'twitch')")
        results.append("- Use the calculator (write 'calculator')")
        results.append("- Translate number from different number systems (write 'translation nums')")
        results.append("- Report bot version (write 'version')")
 
    else:
        results = []
        results.append("Unknown input")
        results.append("You can:")
        results.append("- Count the number of words (write 'word counter')")
        results.append("- Count the number of symbols (write 'symbol counter')")
        results.append("- Check the weather (write 'weather')")
        results.append("- Go to twitch (write 'twitch')")
        results.append("- Use the calculator (write 'calculator')")
        results.append("- Translate number from different number systems (write 'translation nums')")
        results.append("- Report bot version (write 'version')")
 
    return results
