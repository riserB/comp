
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        print(self.data)
        # print("")
        for child in self.children:
            child.print_tree()
        

def build_book_tree():
    root = Node("-----     DSA Book     -----")

    # For Chapter 1
    chapter1 = Node("1. Chapter-1 ")
    Topic1= Node("Hashing")

    Subtopic= Node("\t1.1 Topics 1")
    Subtopic.add_child(Node("\t\t1.1.1 Subtopic-1"))
    Subtopic.add_child(Node("\t\t1.1.2 Subtopic-2"))
    Subtopic.add_child(Node("\t\t1.1.3 Subtopic-3"))
    Topic1.add_child(Subtopic)

    Subtopic2= Node("\t1.2 Topics 2")
    Subtopic2.add_child(Node("\t\t1.2.1 Subtopic-1"))
    Subtopic2.add_child(Node("\t\t1.2.2 Subtopic-2"))
    Subtopic2.add_child(Node("\t\t1.2.3 Subtopic-3"))
    Topic1.add_child(Subtopic2)

    Topic1.add_child(Node("\t1.3 Topics 3"))
    Subtopic3= Node("\t1.4 Topics 4")
    Subtopic3.add_child(Node("\t\t1.4.1 Subtopic-1"))
    Subtopic3.add_child(Node("\t\t1.4.2 Subtopic-2"))
    Subtopic3.add_child(Node("\t\t1.4.3 Subtopic-3"))
    Topic1.add_child(Subtopic3)

    # For Chapter 2
    chapter2 = Node("2. chapter-2")
    Topic2= Node("Graph")
    Topic2.add_child(Node("\t2.1 Topic 1"))
    Topic2.add_child(Node("\t2.2 Topic 2"))
    Topic2.add_child(Node("\t2.3 Topic 3"))
    Topic2.add_child(Node("\t2.4 Topic 4"))
    Topic2.add_child(Node("\t2.5 Topic 5"))

    # For Chapter 3
    chapter3 = Node("3. chapter-3")
    Topic3= Node("Tree")
    Topic3.add_child(Node("\t3.1 Topic 1"))
    Topic3.add_child(Node("\t3.2 Topic 2"))
    Topic3.add_child(Node("\t3.3 Topic 3"))
    Topic3.add_child(Node("\t3.4 Topic 4"))
    Topic3.add_child(Node("\t3.5 Topic 5"))


    root.add_child(chapter1)
    chapter1.add_child(Topic1)
    root.add_child(chapter2)
    chapter2.add_child(Topic2)
    root.add_child(chapter3)
    chapter3.add_child(Topic3)

    return root


if __name__ == '__main__':
    root = build_book_tree()
    root.print_tree()

