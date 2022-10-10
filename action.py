

actions=["+","-","*","/","к","ст"]

string=input("пример: ")

def act_str(input_string):
    for item in actions:
        if item in input_string:
            print(item)
            main_act=item
            elems=input_string.split(main_act)
            if item == "+":
                result=int(elems[0])+int(elems[1])
            if item == "-":
                result=int(elems[0])-int(elems[1])
            if item == "*":
                result=int(elems[0])+int(elems[1])
            if item == "/":
                result=int(elems[0])+int(elems[1])
            if item == "к":
                result=pow(int(elems[0]),1/int(elems[1]))
            if item == "ст":
                result=(int(elems[0]) ** int(elems[1]))

    return result
            
print(act_str(string))