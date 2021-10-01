class Song:
    '''
    What a "Classy" Song
    '''
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def how_many(self, people):
        counter = 0

        for i in people:
            j = i.lower()
            if j in members:
                continue
            else:
                members.append(j)
                counter += 1
        return counter


mount_moose = Song('Mount Moose', 'The Snazzy Moose')

e = Song('ergre', 'tttttttt')
members = []




print(mount_moose.how_many(['John', 'Fred', 'Bob', 'Carl', 'RyAn']))
print(members)
print(mount_moose.how_many(['John', 'Fred', 'Bob', 'Carl', 'RyAn', 'ere','carl' ]))
print(members)
print(mount_moose.how_many(['John', 'Fred', 'Bob', 'Carl', 'RyAn', 'ere','KKKKKKKK' ]))
print(members)

print(mount_moose.how_many(['John', 'Fred', 'Bob', 'Carl', 'RyAn', 'ere','KKKKKKKK', 'BoB', 'freD']))
print(members)

print(e.how_many(['qwqeq2weq', 'John']))
print(members)
