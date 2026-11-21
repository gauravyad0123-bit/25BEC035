class FavoritesList:
    def __init__(self):
        self.entries = []  # each entry is [element, access_count]

    def access(self, e):
        for entry in self.entries:
            if entry[0] == e:
                entry[1] += 1
                return
        self.entries.append([e, 1])

    def remove(self, e):
        for i, entry in enumerate(self.entries):
            if entry[0] == e:
                self.entries.pop(i)
                return

    def top(self, k):
        if k < 0:
            raise ValueError('k must be non-negative')
        ordered = sorted(self.entries, key=lambda entry: entry[1], reverse=True)
        return [entry[0] for entry in ordered[:k]]

f = FavoritesList()
f.access('Python'); f.access('DSA'); f.access('Python')
print(f.top(2))  # ['Python', 'DSA']