#!/usr/bin/env python3

import os
import time
import random
import sys

colors = ["R", "B", "Y", "G"]

simon_said = []

def clear(): os.system('clear')
i = 1
j = 0
while True:
    random_color = random.choice(colors)
    simon_said.append(random_color)

    clear()
    did_simon_say = random.choice(['Yes', 'Yes', 'Yes', 'No'])
    if did_simon_say == 'Yes':
        print("Simon says: {0}".format(simon_said))
    else: print("{0}".format(simon_said))

    time.sleep(i)

    clear()

    if did_simon_say == 'Yes':
        for color in simon_said:
            response = input("Press enter after each letter: ").strip().upper()

            if response == color:
                continue
            else:
                print("INCORRECT")
                print(f"Score: {j}")
                sys.exit()

        i += 0.1
        j += 1
    else:
        response = input("Press enter after each letter: ").strip().upper()

        if response:
            print("Tsk tsk tsk, I didn't say, 'Simon says'")
            print(f"Score: {j}")
            sys.exit()
        else:
            simon_said.pop()
            continue
