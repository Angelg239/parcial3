class Validar:
    def _init_(self):
        self.con = 0

    def validarNumeros(self, num):
        """Verifica que la cadena contenga solo números."""
        if num == "":
            return False

        if self.con >= len(num):
            self.con = 0
            return True

        if 48 <= ord(num[self.con]) <= 57:  # '0' a '9'
            self.con += 1
            return self.validarNumeros(num)
        else:
            self.con = 0
            return False

    def validarLetra(self, dato):
        """Verifica que el primer carácter sea una letra mayúscula."""
        if dato == "":
            return False

        if 65 <= ord(dato[0]) <= 90:  # 'A' a 'Z'
            return True
        else:
            return False

    def validarEntrada(self, dato):
        """Verifica que la cadena tenga máximo 2 dígitos."""
        if dato == "":
            return False
        return len(dato) <= 2