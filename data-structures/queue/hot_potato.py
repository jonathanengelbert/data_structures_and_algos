from queue import Queue


def hot_potato(namelist, num):
    # circle is formed
    circle = Queue()
    for name in namelist:
        circle.enqueue(name)


    while circle.size() > 1:
        for i in range(num):
            circle.enqueue(circle.dequeue())

        circle.dequeue()


    return circle.dequeue()



print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"], 7))
