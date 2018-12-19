class string_converter:

    def convert_to_int(self, number):
        self.mandays_validation(number)
        return float(number)


    def mandays_validation(self,number):
        mandays=float(number)
        mod = mandays % 0.5
        if mod != 0:
            raise TypeError('Use only full and halves!!')
