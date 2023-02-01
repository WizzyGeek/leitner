from quests import cards
from random import randint

def main():
    slots = (list(cards.items()), [], [], [], [])

    choices = []

    for idx, i in enumerate(slots):
        for j in range(len(slots) - idx):
            choices.append(i)

    while True:
        box = []
        while not box: # hehe, evil smirk
            f = randint(0, len(choices) - 1)
            box: list = choices[f]
        n = randint(0, len(box) - 1)
        box_idx = slots.index(box)
        q, a = box.pop(n)
        print(chr(27) + "[2J")
        print(q)
        print("-" * 4)
        input("Answer: ")
        o = input(f"The answer was: {a}\nWere you correct? (Y/n/exit): ")
        print("=" * 5)
        if not o or o[0].lower() == "y":
            box_idx = min(box_idx + 1, len(slots) - 1)
        elif o[0].lower() == "n":
            box_idx = max(box_idx - 1, 0)
        else:
            break
        slots[box_idx].append((q, a))
        if len(cards) == len(slots[-1]):
            print(f"You have memorised all {len(cards)} cards")
            k = input("Exit? (N/y): ")
            if o and o[0].lower() == "y":
                break

if __name__ == "__main__":
    main()