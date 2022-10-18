import random

class Dobbelsteen:
    
    def __init__(self):
        self.values = set(range(1, 7))  
        self.roll()
        self.faces = {

            1: (

                "┌─────────┐\n"
                "│         │\n"
                "│    ●    │\n"
                "│         │\n"
                "└─────────┘\n"
            ),

            2: (

                "┌─────────┐\n"
                "│  ●      │\n"
                "│         │\n"
                "│      ●  │\n"
                "└─────────┘"
            ),

            3: (

                "┌─────────┐\n"
                "│  ●      │\n"
                "│    ●    │\n"
                "│      ●  │\n"
                "└─────────┘"
            ),

            4: (

                "┌─────────┐\n"
                "│  ●   ●  │\n"
                "│         │\n"
                "│  ●   ●  │\n"
                "└─────────┘"

            ),

            5: (

                "┌─────────┐\n"
                "│  ●   ●  │\n"
                "│    ●    │\n"
                "│  ●   ●  │\n"
                "└─────────┘"
            ),

            6: (

                "┌─────────┐\n"
                "│  ●   ●  │\n"
                "│  ●   ●  │\n"
                "│  ●   ●  │\n"
                "└─────────┘"

            )

        }

    def getList(self):
        return list(self.values)

    def roll(self):
        self.number = random.choice(self.getList())

    def getNumber(self):
        return self.number

    def show(self):        
        return str(self.faces.get(self.number))

def main():
    d = Dobbelsteen()
    d.roll()
    d.show()

if __name__ == main():
    main()                