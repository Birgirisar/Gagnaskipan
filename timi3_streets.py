class Street:
    def __init__(self):
        self.new_street = ''


    def add_street(self, new_street, hood, hood_street):
        self.new_street = new_street
        if new_street not in hood_street.values():
            hood_street[hood].append(new_street)
        else:
            print("Alredy exists")

    def streets_in_hood(self, hood, hood_street):
        if hood in hood_street.keys():
            print("All streets in {}:".format(hood))
            num = 1
            for val in hood_street[hood]:
                print('{}. {}'.format(num, str(val)))
                num += 1
        print()


    def hood_of_street(self, street, hood_street):
        for key, val in hood_street.items():
            for i in val:
                if i == street:
                    print('The hood that contains {} is {}'.format(i, key))
                    return
        print('No hood')
        
                    

    def print(self, hood_street):
        for key, val in hood_street.items():
            print('{}: {}'.format(key,val))
        print()




def main():
    hood_street = {'Reykjavík': ['Langholtsvegur'], 'Garðabær': ['Garðbæsgata'], 'Hafnarfjörður': ['Hafngata'], 'Mosó': ['Mosgata'], 'Miðbær': ['Laugavegur']}
    test = Street()
    test.add_street('Efstasund', 'Reykjavík', hood_street)
    test.add_street('Skipasund', 'Reykjavík', hood_street)
    test.print(hood_street)
    test.streets_in_hood('Reykjavík', hood_street)
    test.hood_of_street('Skipasund', hood_street)
    

main()

