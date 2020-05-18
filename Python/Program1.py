b1 = {"grass", "goat", "tiger"}
b2 = set()
case1 = {"grass", "goat"}
case2 = {"tiger", "goat"}
b = 1
while len(b1) != 0:
    if b == 1:
        if len(b1) == 3:
            obj = b1.pop()
            
            if b1 != case1 and b1 != case2:
                print(f"Farmer takes {obj} from bank1 to bank2")
                b2.add(obj)
                b = 2
            else:
                b1.add(obj)
        else:
            obj = b1.pop()
            print(f"Farmer takes {obj} from bank1 to bank2")
            b2.add(obj)
            b = 2
    else:
        if b2 == case1 or b2 == case2:
            obj = b2.pop()
            print(f"Farmer takes {obj} from bank2 to bank1")
            b1.add(obj)
        else:
            print("Farmer comes from bank2 to bank1")

        b = 1