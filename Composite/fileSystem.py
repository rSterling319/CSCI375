import os
import copy

cp = {}

class Component:
    def __init__(self, name):
        self.name = name

    def Rename(self, name, newName):
        if name in self.children.keys():
            self.children[name].name = newName
        else:
            for f in self.children.values():
                if type(f) == Folder:
                    f.Rename(name, newName)

    def Copy(self, name):
        if name in self.children.keys():
            if name in cp.keys():
                cp[name] += 1
            else:
                cp[name] = 1
            self.children[name+'('+ str(cp[name])+')']= copy.deepcopy(self.children[name])
            self.Rename(name+'('+ str(cp[name])+')', name+'('+ str(cp[name])+')')
        else:
            for f in self.children.values():
                if type(f) == Folder:
                    f.Copy(name)


    def Add(self, item, destination):
        try:
            item = eval(item)
            if type(item) == Folder:
                item.name = item.name.upper()
            try:
                if destination == self.name:
                    self.children[item.name]=item
                elif destination in self.children.keys():
                    self.children[destination].children[item.name]=item
                else:
                    for f in self.children.values():
                        if type(f) == Folder:
                            f.Add(item, destination)
            except AttributeError:
                print("Files can't inherit other Files/Folders")
                input("Press enter to continue...")
        except:
            print("Could not add %s" %item)
            input("Press enter to continue...")

    def Delete(self, name):
        if name in self.children.keys():
            del self.children[name]
        else:
            for f in self.children.values():
                if type(f) == Folder:
                    f.Delete(name)

    def __str__(self):
        return self.name


class Folder(Component):
    def __init__(self, name):
        Component.__init__(self, name)
        self.children = {}

    def __str__(self):
        return self.name

class File(Component):
    def __init__(self,name):
        Component.__init__(self, name)

    def __str__(self):
        return self.name

def printFileSystem(item, lev=0, all=True):
    level = lev
    if all:
        if type(item)==Folder:
            print(level * '|  ' + item.name.upper() + ' --> ' + str(type(item).__name__))
            #print(item.children)
            for f in item.children.values():
                printFileSystem(f,level+1)
                #print(f, str(type(f)))
        else:
            print(level * '|  ' + item.name + ' --> ' + str(type(item).__name__))
    else:
        print(item.name.upper() + '--> ' + str(type(item).__name__))
        for f in item.children.values():
            if type(f)==Folder:
                print('-' + f.name.upper() + ' --> ' + str(type(f).__name__))
            else:
                print('-' + f.name + ' --> ' + str(type(f).__name__))

def printMenu():
    print(' '*25 + 'Mock File Tree')
    print('*'*64)
    print(' '*26 + '* Commands *')
    print('   Add: Add Type("Name") Destination    |    Copy: Copy Name')
    print('   Delete: Delete Name               |    Rename: Rename Name New_Name')
    print('*'*64)


quit = False

def Quit():
    global quit
    quit = True

os.system('clear')
printMenu()
folder = Folder(input('Input name of starting Folder: ').upper())
commands = {'Copy': folder.Copy, 'Delete': folder.Delete, 'Add': folder.Add, 'Rename': folder.Rename, 'Quit': Quit }
#FIXME rename not working!
while not quit:
    os.system('clear')
    printMenu()
    printFileSystem(folder)
    command = input('\nEnter command: ')
    command = command.split()
    if len(command) == 2:
        commands[command[0]](command[1])
    elif len(command) == 3:
        commands[command[0]](command[1], command[2])
    else:
        commands[command[0]]()

os.system('clear')
