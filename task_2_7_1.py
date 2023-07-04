class Notebook:

    def __init__(self, note):
        self._notes = note

    @property
    def notes_list(self):
        for x in range(len(self._notes)):
            print(f'{x + 1}.{self._notes[x]}')
        return self._notes



note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
note.notes_list

