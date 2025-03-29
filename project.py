from tabulate import tabulate

class TaskMaster:
    def __init__(self):
        print("\nTaskMaster | To-Do List")
        self.database = []
        self.count = 0

    def run(self):
        running = True
        while running:
            action = self.get_input()

            if action == "V":
                self.view()
            elif action == "C":
                self.create()
            elif action == "U":
                self.update()
            elif action == "D":
                self.delete()
            elif action == "M":
                self.mark_done()
            else:
                running = False

    def get_input(self):
        instructions = [
            {"Key": "V", "Action": "View Tasks"},
            {"Key": "M", "Action": "Mark Task as Done"},
            {"Key": "C", "Action": "Create a Task"},
            {"Key": "U", "Action": "Update a Task"},
            {"Key": "D", "Action": "Delete a Task"},
            {"Key": "E", "Action": "Exit"}
        ]

        while True:
            print(tabulate(instructions, headers="keys", tablefmt="rounded_outline"))
            action = input("What do you want to do?: ").upper()

            if action in ["V", "C", "U", "D", "M", "E"]:
                return action
            else:
                print("Invalid key, try again.")

    def view(self):
        print(tabulate(self.database, headers="keys", tablefmt="rounded_grid"))

    def create(self):
        task = input("Task: ")
        self.count += 1
        self.database.append({"ID": self.count, "Task": task, "Done": False})

    def update(self):
        numbers = [task["ID"] for task in self.database]

        while True:
            self.view()
            try:
                i = int(input("Which task would you like to update?: "))
                if i in numbers:
                    break
                else:
                    print("Invalid task ID, try again.")
            except ValueError:
                print("Invalid input, try again.")

        new_task = input("What do you want to update it to?: ")
        for task in self.database:
            if task["ID"] == i:
                task["Task"] = new_task

    def delete(self):
        numbers = [task["ID"] for task in self.database]

        while True:
            self.view()
            try:
                i = int(input("Which task would you like to delete?: "))
                if i in numbers:
                    break
                else:
                    print("Invalid task ID, try again.")
            except ValueError:
                print("Invalid input, try again.")

        self.database = [task for task in self.database if task["ID"] != i]

    def mark_done(self):
        numbers = [task["ID"] for task in self.database]

        while True:
            self.view()
            try:
                i = int(input("Which task would you like to mark as done?: "))
                if i in numbers:
                    break
                else:
                    print("Invalid task ID, try again.")
            except ValueError:
                print("Invalid input, try again.")

        for task in self.database:
            if task["ID"] == i:
                task["Done"] = True
                print(f'Task "{task["Task"]}" marked as done.')


def main():
    task_master = TaskMaster()
    task_master.run()


if __name__ == "__main__":
    main()
