# as a list ...
ll = [3, 4]
ll += [5, 6]  # ll = [3, 4, 5, 6]
# ... as a stack ...
ll.append(10)  # ll = [4, 5, 6, 10]
ll.pop()  # ll = [4, 5, 6]
# ... and as a queue
ll.insert(0, 5)  # ll = [5, 4, 5, 6]
ll.pop()  # ll = [5, 4, 5]
