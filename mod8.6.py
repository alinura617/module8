# Alinura Sultanova
# 08.18.2023

def check_tasks_and_debuffs(character):
    game_items = ['pan', 'paper', 'idea', 'rope', 'groceries']
    status_debuffs = ['slow']

    tasks = {
        'Climb a mountain': {'required_items': ['rope', 'coat', 'first aid kit'], 'forbidden_debuffs': ['slow']},
        'Cook a meal': {'required_items': ['pan', 'groceries'], 'forbidden_debuffs': ['small']},
        'Write a book': {'required_items': ['pen', 'paper', 'idea'], 'forbidden_debuffs': ['confusion']}
    }

    for task, details in tasks.items():
        missing_items = [item for item in details['required_items'] if item not in character.weapons]
        forbidden_debuffs = [debuff for debuff in details['forbidden_debuffs'] if debuff in character.weaknesses]

        if not missing_items and not forbidden_debuffs:
            print(f"Character can '{task}'.")
        else:
            print(f"Character cannot '{task}':")
            if missing_items:
                print(f"   Missing items: {', '.join(missing_items)}")
            if forbidden_debuffs:
                print(f"   Forbidden debuffs: {', '.join(forbidden_debuffs)}")

class Character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

player = Character('Dragon Slayer', ['pan', 'paper', 'idea', 'rope', 'groceries'], ['slow'])

check_tasks_and_debuffs(player)
