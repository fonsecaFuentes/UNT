import re


class FieldValidation():
    def validate_fields(self, titulo, estilo, desarrollador, precio):
        nulo = r"^(?!\s*$).+"

        if (
            re.match(nulo, titulo)
            and re.match(nulo, estilo)
            and re.match(nulo, desarrollador)
            and re.match(nulo, precio)
        ):
            return True
        else:
            return False

    def validate_price(self, precio):
        numero = r"^\d+(\.\d{1,2})?$"
        if re.match(numero, precio):
            return True
        else:
            return False
