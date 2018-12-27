class string_converter:

    def convert_to_int(self,number):
        new_number=self.comma_replace(number)
        try:
            self.mandays_validation(new_number)
            return float(new_number)
        except ValueError:
            return "This is not a correct entry"



    def mandays_validation(self,number):
        mandays=float(number)
        mod = mandays % 0.5
        if mod != 0:
            raise TypeError('Use only full and halves!!')

    def comma_replace(self,number):
        new_mandays = ""
        for letter in number:
            if letter == ",":
                letter = "."
                new_mandays += letter
            else:
                new_mandays += letter
        return new_mandays
