class Notifier:
    def __init__(self, message):
        self.message = message

    def record_in_plain_text(self):
        """
        registra el log de notificaciones
        """
        try:
            f = open("log.txt", "a")
            f.write('[WARNING] {} \n'.format(self.message))
            f.close()
        except Exception as e:
            print('ERROR AL ESCRIBIR ARCHIVO DE LOGS: {}'.format(str(e)))

    def print_warning_log(self):
        """
        Imprime log por partalla
        """
        print('[WARNING] {}'.format(self.message))