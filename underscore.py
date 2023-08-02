class Underscore(object):
    def map(self, lister, functioner):
        return [functioner(x) for x in lister]
    def reduce(self, lister, functioner):
        result = lister[0]
        for x in range(1, len(lister)):
            result = functioner(result, lister[x])
            print(result)
        return result
    # def find(self):

    def filter(self, lister, condition):
        return [x for x in lister if condition(x)]
    # def reject(self):


