
class HuzaroWorksheet:

    def __init__(self, worksheet):
        self.worksheet = worksheet

    def initiate_worksheet(self):
        self.worksheet.write(0, 0, 'EAN')
        self.worksheet.write(0, 1, 'Cena')
        self.worksheet.write(0, 2, 'Stan')
        self.worksheet.write(0, 3, 'Nazwa')
        self.worksheet.write(0, 4, 'Uwagi')

        self.worksheet.set_panes_frozen(True)
        self.worksheet.set_horz_split_pos(1)

    def write(self, x, y, string):
        self.worksheet.write(x, y, string)
