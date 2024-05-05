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
    if (column == 0 or line == 0):
        return json.dumps({ "one_time": True, "buttons": []}, ensure_ascii=False).encode('utf-8')

    str = [[]]
    str2 = []
    for i in range(line-1):
        str.append(str2)

    k = 0
    for i in range(0, line):
        str2 = []
        for j in range(column):
            if k < len(titles):
                str2.append(getBut(titles[k], "positive"))
                k+=1
        str[i]=str2
    keyboard = {
        "one_time": True,
        "buttons": str
    }


    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    return keyboard


