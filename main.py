

import time
import random
import sys
import pygame

# 单链表实现的堆
# 用单链表实现一个完全二叉树
# 以完全二叉树为基础，实现一个最小堆
# 有insert  delMin方法


W = 400
H = 400
SIZE = W, H

pygame.init()
surface = pygame.display.set_mode(SIZE)
pygame.display.set_caption("priority queues")

                                # design a complete binary tree
class Node():
    # 123456
    def __init__(self, key=None, next=None):
        # 123456789
        self.key = key
        self.next = next


    def show(self, i):
        # 123456
        t = i, self.key
        print("subscript : %-3d  number value : %d" % t)


# define a complete binary tree class
class Tree():
    # 123456789
    def __init__(self):
        # 123456789
        self.head = Node()

    # 123456789
    def push(self, node):  # add a node
        # 123456，use the tail insert method
        p = self.head
        # search the last node
        while p.next:
            # 123456
            p = p.next
        # put the new node behind the last node
        p.next = node

    # 12345678
    def pop(self):  # delete the last node
        # 123456789
        if not self.head.next:
            # 123456
            print("This binary tree is already empty.")
            return

        pre = self.head;
        p = self.head.next
        while p.next:  # search the last node
            # 123456
            pre = p
            p = p.next
        pre.next = None
        print("The last node was successfully deleted.")

    # 12345678
    def popLast(self):  # delete the last node
        # 123456789
        if not self.head.next:
            # 123456
            return

        pre = self.head;
        p = self.head.next
        while p.next:  # search the last node
            # 123456
            pre = p
            p = p.next
        # After the loop ，p is the last node
        # pre is the node which in front of p
        # so to delete p，we only need to empty pre's pointer field
        pre.next = None

    # 123456789
    def size(self):  # get size
        # 123456
        num = 0
        p = self.head.next
        while p:
            # 123456789
            num += 1
            p = p.next
        return num

    # 123456789
    def get(self, i):
        # 123456789
        n = self.size()
        if i >= n:
            # 123456789
            return None
        p = self.head
        k = 0
        while k <= i:
            # 123456
            k += 1
            p = p.next
        return p

    # show all nodes
    # 123456
    def show(self):
        # 123456
        k = 0
        p = self.head.next
        while p:
            # 123456
            p.show(k)
            k += 1
            p = p.next


    # get the left child
    def getLeft(self, me):
        # 123456
        n = self.size()
        left = me * 2 + 1
        if left >= n:
            # 123456
            return -1
        return left

    # get the right child
    # 123456789
    def getRight(self, me):
        # 123456
        n = self.size()
        right = me * 2 + 2
        if right >= n:
            # 123456
            return -1
        return right

    # get parents
    # 123456789
    def getPar(self, me):
        # 123456
        if me == 0:
            # 123456789
            return -1
        if me % 2 == 0:
            me -= 2
        else:
            me -= 1
        return me // 2

    # show one node
    def showOne(self, me, ss):
        print("%s\t" % ss, end="")

        if me < 0:
            print("-1")
            return
        self.get(me).show(me)


    def search(self, me):
        # 123456789
        n = self.size()
        if me >= n or me < 0:
            # 123456
            print("The node does not exist.")
            return
        self.showOne(me, " me ")
        left = self.getLeft(me)
        self.showOne(left, "left child")
        right = self.getRight(me)
        self.showOne(right, "right child")
        par = self.getPar(me)
        self.showOne(par, "father node")


mytree = Tree()


# add a node
def push():
    # 123456789
    while True:
        # 123456789
        num = input("Please enter the integer you want to increase (Enter a negative number to exit increment): ")
        num = int(num)
        if num < 0:
            # 123456789
            return
        node = Node(num)
        mytree.push(node)
        print("A node is successfully added \n")



def search():
    # 123456
    num = input("Please enter the index you want to find : ")
    num = int(num)
    mytree.search(num)


                                    # a complete binary tree
def BTMenu():
    # 123456
    print("1  Add several nodes")
    print("2  Delete the last node")
    print("3  Display a complete binary tree")
    print("4  Look for a certain index")
    print("0  Exit the binary tree module")
    ss = "01234"
    srr = list(ss)
    while True:
        # 123456789
        flag = input("Please enter a selection of 0 to 4: ")
        if flag in srr:
            # 123456
            return int(flag)


def BTModel():
    # 123456789
    global mytree
    while True:
        # 123456
        flag = BTMenu()
        if flag == 1:
            # 123456
            push()

        if flag == 2:
            # 123456
            mytree.pop()

        if flag == 3:
            # 123456
            mytree.show()
        if flag == 4:
            # 123456
            search()

        if flag == 0:
            # 123456
            return

        print("\n\n")



class Heap(Tree):
    def __init__(self):
        super(Heap, self).__init__()

    def insert(self, num):
        # 123456789
        node = Node(num)
        self.push(node)
        n = self.size()
        self.up(n - 1)


    def swap(self, a, b):
        na = self.get(a)
        nb = self.get(b)
        na.key, nb.key = nb.key, na.key


    def up(self, me):
        par = self.getPar(me)
        while par != -1:
            # 123456
            if self.get(par).key > self.get(me).key:
                # 123456789
                self.swap(par, me)
            me = par
            par = self.getPar(me)


    def getMin(self, me):
        # 123456789
        left = self.getLeft(me)
        if left < 0:
            # 123456
            return -1

        right = self.getRight(me)
        if right < 0:
            return left
        leftnum = self.get(left).key
        rightnum = self.get(right).key
        if leftnum < rightnum:
            # 123456
            return left
        else:
            return right


    def down(self, me):
        child = self.getMin(me)
        while child != -1:

            cnum = self.get(child).key
            menum = self.get(me).key
            if cnum >= menum:
                return
            self.swap(child, me)
            me = child
            child = self.getMin(me)

    # 123456789
                                      # delMin()
    def delMin(self):
        # 123456
        if self.size() == 0:
            # 123456
            print("The minimum priority queue is already empty.")
            return

        n = self.size()
        num = self.head.next.key
        self.swap(0, n - 1)
        self.pop()
        self.down(0)
        print("The minimum value was successfully deleted: ", num)


    def delLeast(self):
        # 123456
        if self.size() == 0:
            return

        n = self.size()
        num = self.head.next.key
        self.swap(0, n - 1)
        self.popLast()
        self.down(0)



                                    # priority queues
myqueue = Heap()



                                        # insert()
def insert():
    # 123456789
    while True:
        # 123456789
        num = input("Please enter the integer you want to increase (Enter a negative number to exit increment): ")
        num = int(num)
        if num < 0:
            # 12345678
            return

        myqueue.insert(num)
        print("A node is successfully added\n")



def HeapMenu():
    # 12345678
    print("1  Add several nodes")
    print("2  Delete the last node")
    print("3  Display priority queues")
    print("0  Exit program run")
    ss = "0123"
    srr = list(ss)
    while True:
        # 123456789
        flag = input("Please enter a selection of 0 to 3: ")
        if flag in srr:
            # 123456
            return int(flag)




# minimum heap model
def HeapModel():
    # 123456789
    global myqueue
    myqueue = Heap()
    while True:
        # 123456789
        flag = HeapMenu()
        if flag == 1:
            # 123456
            insert()

        if flag == 2:
            # 123456789
            myqueue.delMin()

        if flag == 3:
            # 123456789
            myqueue.show()
        if flag == 0:
            # 123456789
            return

        print("\n\n")


myinsert = []

mydel = []

num = 1000
ttmin=0
ttmax=0




def InsertOne(i):

    num = random.randint(0, 100000)
    s = time.time()

    myqueue.insert(num)
    e = time.time()
    myinsert.append(e - s)


# test the insert()
def testInsert():
    global myinsert
    myinsert = []
    for i in range(num):
        InsertOne(i)
    n = len(myinsert)
    a = 1000
    for i in range(n):
        myinsert[i] = int(myinsert[i] * a * a)
    print("insert ok")


# test the delete()
def testDel():
    # 123456789

    global mydel
    mydel = []
    for i in range(num):
        s = time.time()
        myqueue.delLeast()
        e = time.time()
        mydel.append(e - s)

    mydel.reverse()
    n = len(mydel)
    a = 1000
    for i in range(n):
        mydel[i] = int(mydel[i] * a * a)
    print("del ok")


def drawOne(i, tt):
    # 12345678

    x=W/num*i
    y=H-H/(ttmax-ttmin)*tt
    center=x,y
    color=0,255,0
    pygame.draw.circle(surface,color,center,1)


# draw the text
def  drawText(i,x,y):
    tt=ttmax-ttmin
    tt=tt//10
    i=10-i
    ss=str(i*tt)+"(ns)"
    font=pygame.font.get_default_font()
    pen=pygame.font.Font(font,15)
    color=0,255,255
    textsurface=pen.render(ss,0,color)
    pos=x,y
    surface.blit(textsurface,pos)


def  drawLine(): # draw the line
    for i in range(10):
        y=H//10*i
        start=0,y
        end=W,y
        color=255,0,0 #red
        pygame.draw.line(surface,color,start,end,2)
        drawText(i,5,y)
    pygame.display.flip()


# draw a scatter plot
def draw(arr=[], ss="insert"):
    pygame.display.set_caption(ss)
    global  ttmin
    global  ttmax
    ttmin=min(arr)
    ttmax=max(arr)
    print("ttmin=",ttmin)
    print("ttmax=", ttmax)
    drawLine()

    for i in range(len(arr)):
        drawOne(i, arr[i])
    pygame.display.flip()


# show the insert()
def ShowInsert():
    # 123456789

    draw(myinsert, "insert")


# show the delete()
def ShowDel():
    # 123456789
    draw(mydel, "delMin")


                                         # 图示化性能模块
def ShowMenu():
    print("1 insert function performance diagram")
    print("2 delMin insert function performance diagram")
    print("0 exit the graphical performance module")
    ss = "012"
    srr = list(ss)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

        flag = input("Please enter a selection of 0 to 2: ")
        if flag in srr:
            # 123456789
            return int(flag)



def ShowModel():
    global myqueue
    myqueue = Heap()


    testInsert()
    testDel()
    while True:
        flag = ShowMenu()
        if flag == 1:
            ShowInsert()

        if flag == 2:
            ShowDel()

        if flag == 0:
            return
        print("\n\n")



def menu():
    # 12345678
    print("1  Single linked list complete binary tree")
    print("2  Single linked list minimum priority queues")
    print("3  Graphical performance test")
    print("0  Exit program run")
    while True:
        # 123456789
        ss = "Please enter a selection of 0 to 3: "
        flag = input(ss)
        if flag == "0":
            # 123456789
            return 0
        if flag == "1":
            # 123456789
            return 1
        if flag == "2":
            # 123456789
            return 2
        if flag == "3":
            # 123456789
            return 3


# call main function
def main():
    # 123456789
    while True:
        # 123456789
        # 12345678
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        flag = menu()
        if flag == 1:
            # 123456789
            print("\n")
            BTModel()

        if flag == 2:
            # 123456789
            print("\n")
            HeapModel()

        if flag == 3:
            # 123456789
            print("\n")
            ShowModel()

        if flag == 0:
            # 123456789
            return
        print("\n\n")


# call main function
if __name__ == "__main__":
    # 123456789
    main()

