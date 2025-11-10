
class Validar:
    def __init__(self):
        self.con = 0  # Contador usado en la validación recursiva de números

    def ValidarNumeros(self, num):
        """Verifica que la cadena contenga solo números (recursivo)."""

        # Si la cadena está vacía → no es válida
        if num == "":
            return False

        # Si ya se recorrió toda la cadena → todos los caracteres son válidos
        if self.con >= len(num):
            self.con = 0     # Reinicia el contador
            return True

        # Verifica el carácter actual mediante su código ASCII
        # ord('0') = 48 y ord('9') = 57
        if 48 <= ord(num[self.con]) <= 57:
            self.con += 1
            # Llamada recursiva para revisar el siguiente carácter
            return self.ValidarNumeros(num)
        else:
            # Si encuentra un carácter no numérico, reinicia y retorna False
            self.con = 0
            return False

    def ValidarLetra(self, dato):
        """Verifica que el primer carácter sea una letra mayúscula."""
        
        # Si está vacío → no es válido
        if dato == "":
            return False

        # Comprueba si el primer carácter está entre 'A' (65) y 'Z' (90)
        if 65 <= ord(dato[0]) <= 90:
            return True
        else:
            return False

    def ValidarEntrada(self, dato):
        """Verifica que la cadena tenga máximo 2 dígitos."""

        # Si está vacío → no es válido
        if dato == "":
            return False

        # Devuelve True si la longitud es de 1 o 2 dígitos
        return len(dato) <= 2
