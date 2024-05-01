import random


class VacuumAgent:
    def _init_(self):
        self.location = random.choice(['A', 'B'])

    def perceive(self, location_status):
        if location_status[self.location] == 'Dirty':
            return 'Clean'
        else:
            return 'Move'

    def act(self, action):
        if action == 'Move':
            self.location = 'A' if self.location == 'B' else 'B'
            print(f"Moving to {self.location}")
        elif action == 'Clean':
            print(f"Cleaning {self.location}")
            return 'Cleaned'


def main():
    location_status = {'A': random.choice(['Clean', 'Dirty']),
                       'B': random.choice(['Clean', 'Dirty'])}

    agent = VacuumAgent()

    while True:
        print(f"Current Location: {agent.location}, Status: {location_status[agent.location]}")

        action = agent.perceive(location_status)
        result = agent.act(action)

        if result == 'Cleaned':
            location_status[agent.location] = 'Clean'

        print("Location Status:", location_status)
        print("----------")

        if all(status == 'Clean' for status in location_status.values()):
            print("All locations are clean.")
            break


if __name__ == "__main__":
    main()