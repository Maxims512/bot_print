import json

def getBut(text, color):
    return {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"" + "1" + "\"}",
                    "label": f"{text}"
                },
                "color": f"{color}"
            }

def createKeyboard(line, column, titles):
    str = [[]]
    str2 = []
    for i in range(column-1):
        str.append(str2)

    k = 0
    for i in range(0, column):
        str2 = []
        for j in range(line):
            if k < len(titles):
                print(k)
                str2.append(getBut(titles[k], "positive"))
                k+=1
        str[i]=str2

    keyboard = {
        "one_time": False,
        "buttons": str
    }

    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    return keyboard


