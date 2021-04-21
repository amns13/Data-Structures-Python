from random import randrange
from BST import BST

def main():
    bst = BST()

    for i in range(20):
        val = randrange(40)
        print(f"{i}. Inserting {val} into the BST.")
        try:
            bst.insert(val)
        except ValueError as err:
            print(err)

    print("Inorder Traversal:")
    bst.inorder()
    print("Levelorder Traversal:")
    bst.levelorder()

    print('=======================================')

    for i in range(20):
        val = randrange(40)
        print(f"Searching key {val} in the BST.")
        print("Found" if bst.search(val) else "Not found")

    print('=======================================')

    for i in range(20):
        val = randrange(40)
        print(f"Removing key {val} from the BST.")
        try:
            bst.remove(val)
        except ValueError as err:
            print(err)

    print("Inorder Traversal:")
    bst.inorder()
    print("Levelorder Traversal:")
    bst.levelorder()


if __name__ == '__main__':
    main()
