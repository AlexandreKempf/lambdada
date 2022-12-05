class Sequence:
    def __init__(self, iterable):
        self._sequence = iterable

    def __str__(self):
        return self.to_list()._sequence.__str__()

    def map(self, fun, index=False, array=False):
        if index and array:
            array = self.to_list()._sequence
            self._sequence = (
                fun(array, idx, element) for idx, element in enumerate(self._sequence)
            )
        elif index:
            self._sequence = (
                fun(idx, element) for idx, element in enumerate(self._sequence)
            )
        elif array:
            array = self.to_list()._sequence
            self._sequence = (fun(array, element) for element in self._sequence)
        else:
            self._sequence = (fun(element) for element in self._sequence)
        return self

    def star_map(self, fun, index=False, array=False):
        if index and array:
            array = self.to_list()._sequence
            self._sequence = (
                fun(array, idx, *element) for idx, element in enumerate(self._sequence)
            )
        elif index:
            self._sequence = (
                fun(idx, *element) for idx, element in enumerate(self._sequence)
            )
        elif array:
            array = self.to_list()._sequence
            self._sequence = (fun(array, *element) for element in self._sequence)
        else:
            self._sequence = (fun(*element) for element in self._sequence)
        return self

    def filter(self, fun, index=False, array=False):
        if index and array:
            array = self.to_list()._sequence
            self._sequence = (
                element
                for idx, element in enumerate(self._sequence)
                if fun(array, idx, element)
            )
        elif index:
            self._sequence = (
                element
                for idx, element in enumerate(self._sequence)
                if fun(idx, element)
            )
        elif array:
            array = self.to_list()._sequence
            self._sequence = (
                element for element in self._sequence if fun(array, element)
            )
        else:
            self._sequence = (element for element in self._sequence if fun(element))
        return self

    def star_filter(self, fun, index=False, array=False):
        if index and array:
            array = self.to_list()._sequence
            self._sequence = (
                element
                for idx, element in enumerate(self._sequence)
                if fun(array, idx, *element)
            )
        elif index:
            self._sequence = (
                element
                for idx, element in enumerate(self._sequence)
                if fun(idx, *element)
            )
        elif array:
            array = self.to_list()._sequence
            self._sequence = (
                element for element in self._sequence if fun(array, *element)
            )
        else:
            self._sequence = (element for element in self._sequence if fun(*element))
        return self

    def show(self, n=10):
        array = self.to_list()._sequence
        min_n = min(n, len(array))
        print("[")
        [print(" ", array[idx]) for idx in range(min_n)]
        if min_n < len(array):
            print("  ...")
        print("]")

    def to_list(self):
        self._sequence = list(self._sequence)
        return self


a = (
    Sequence({"a": 3, "f": 4})
    .map(lambda i, x: (i, x), index=True)
    .star_map(lambda arr, i, *args: args, index=True, array=True)
    .show()
)
