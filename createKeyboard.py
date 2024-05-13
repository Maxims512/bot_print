import json
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
def getBut(text, color):
    return {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"" + "1" + "\"}",
                    "label": f"{text}"
                },
                "color": f"{color}"
            }

def createKeyboard(line,column, titles):
    keyboard = VkKeyboard(one_time=True)

    if (column == 0 or line == 0):
        return json.dumps({ "one_time": True, "buttons": []}, ensure_ascii=False).encode('utf-8')

    k = 0
    for i in range(column):
        for j in range(0, line):
            if k < len(titles):
                keyboard.add_button(titles[k], color=VkKeyboardColor.PRIMARY)
                k+=1
        if (k < len(titles)):
            keyboard.add_line()
    return keyboard.get_keyboard()


