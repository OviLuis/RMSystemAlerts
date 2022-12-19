
class MeasureValidator:
    """docstring for MeasureValidator."""

    def __init__(self, device_id, measure_value,  threshold=50.0):
        self.device_id = device_id
        self.measure_value = measure_value
        self.threshold = threshold

    def validate_threshold(self):
        """
        Valida si el valor de la medida sobrepasa el umbral
        :return: True --> valor valido ; False--> valor fuera del umbral
        """

        if self.measure_value > self.threshold:
            return False
        return True

    def validate(self):
        """
        realizar las validaciones sobre las medidas

        return: is_valid : True --> no hay validaciones fallidas; False --> hay validaciones fallidas
                message: mensaje con la validacion fallida
        """

        is_valid_threshold = self.validate_threshold()

        if not is_valid_threshold:
            msg = 'El medidor {} sobrepasa el umbral {} con una medida de {}'.format(
                self.device_id,
                self.threshold,
                self.measure_value
            )
            return False, msg

        return True, 'OK'
