# Exemple 2 : Sérialisation
# La sérialisation est le processus d’enregistrement de l’état d’un objet en une séquence
# d’octets.
# Propose un algorithme permettant de sérialiser des grappes d’objets.
#
# We assume that we have a method to serialise one object.
# Object.serialise()
# Then we assume we have an object tree: each object in the tree is a Node.
# Each Node can have children. Some Nodes do not have any children.

class Node:

    name: str
    children: list

    def __init__(self, name: str) -> None:
        self.name = name
        self.children = []
        print("Just created a Node called {}".format(self.name))

    def addChild(self, child: 'Node'):
        self.children.append(child)
        print("Just added a child Node {} to parent Node {}".format(child.name, self.name))

    def serialise(self) -> bytearray:
        ba = bytearray()
        ba.extend('['.encode())
        ba.extend(self.name.encode())
        ba.extend(']'.encode())
        for child in self.children:
            ba.extend(child.serialise())
        return ba

    def treeview(self, depth: int):
        print('+' + '--' * depth + self.name)
        for child in self.children:
            child.treeview(depth + 1)
        
    def __str__(self) -> str:
        return self.name

# Create a Node hierarchy
luca = Node('Luca')
luca.addChild(Node('Tun'))
luca.addChild(Node('Giulio'))
luca.addChild(Node('Vincenzo'))
diane = Node('Diane')
diane.addChild(Node('Elliott'))
kim = Node('Kim')
kim.addChild(Node('Matteo'))
kim.addChild(Node('Zoe'))
alberto = Node('Alberto')
alberto.addChild(luca)
alberto.addChild(diane)
alberto.addChild(kim)

alberto.treeview(1)
print(alberto.serialise())

