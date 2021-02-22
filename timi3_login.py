from datetime import datetime
class LogEntries:

    def __init__(self):
        self.now = datetime.now()
        self.curr_time = self.now.strftime('%H:%M:%S')
        self.user = ''
        self.passw = ''

    def Add(self, entries):
        print("You are now adding a log entry..")
        self.user = input('Enter username: ')
        self.passw = input("Enter password: ")

        entries[self.curr_time] = [self.user, self.passw]
        

    def AllItems(self, start, end, entries):
        for key, val in entries.items():
            if key >= start or key <= end:
                print(val)

    def DeleteEntry(self):
        pass

    def NewestEntry(self):
        pass


def main():
    
    Entries = {}
    test = LogEntries()
    test.Add(Entries)
    print(Entries)

    test.AllItems(15:32:10, 15:40:10, Entries)
    

main()