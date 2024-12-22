class ObjList:

    def __init__(self, data: str):
        self.__data = data
        self.__next = None
        self.__prev = None

    def set_next(self, obj: object):
        self.__next = obj

    def set_prev(self, obj: object):
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

    def add_obj(self, obj):
        if not self.head:
            self.head = obj
            self.tail = obj
        else:
            obj.set_prev(self.tail)
            self.tail.set_next(obj)
            self.tail = obj

    def remove_obj(self):
        if not self.tail:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)

    def get_data(self):
        current_elem = self.head
        res = []
        while current_elem:
            res.append(current_elem.get_data())
            current_elem = current_elem.get_next()
        return res