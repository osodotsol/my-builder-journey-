class Agent:
    def __init__(self, name, personality):
        self.name = name
        self.personality = personality
        self.memory = []

    def speak(self, message):
        print(f"{self.name} says: {message}")
    def remember(self, fact):
        self.memory.append(fact)

    def recall(self):
            print(f"{self.name}'s memory: {self.memory}")


oso = Agent("Oso", "direct and analytical")
forge = Agent("Forge", "strategic and precise")

oso.speak("I build in public every day.")
forge.speak("Strategy before action. Always.")
oso.remember("Github pushed today")
oso.remember("OOP makes sense now")
oso.recall()
forge.recall()