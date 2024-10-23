class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, new_obj):
        if self.head is None:
            self.head = new_obj
            self.tail = new_obj
            return
        new_obj.set_prev(self.tail)
        self.tail.set_next(new_obj)
        self.tail = new_obj

    def remove_obj(self):
        for_delete = self.tail
        if self.head != for_delete:
            prev_obj = self.tail.get_prev()
            prev_obj.set_next(None)
            self.tail = prev_obj
        else:
            self.head = None
        del for_delete

    def get_data(self):
        current = self.head
        res = []
        while current:
            res.append(current.get_data())
            current = current.get_next()
        return res
