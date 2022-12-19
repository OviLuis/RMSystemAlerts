import sys

from validator import MeasureValidator
from notifier import Notifier


class MeasureConsumer:

    def __init__(self, connection):
        self.connection = connection

    def get_data(self):
        last_id = 0
        sleep_ms = 5000
        while True:
            try:
                resp = self.connection.xread(
                    {'RMSystem': last_id}, count=1, block=sleep_ms
                )
                if resp:
                    key, messages = resp[0]
                    last_id, data = messages[0]
                    print("REDIS ID: ", last_id)
                    print("      --> ", data)

                    parsed_data = {key.decode(): val.decode() for key, val in data.items()}

                    validator = MeasureValidator(int(parsed_data.get('device_id')), float(parsed_data.get('measure_value')))
                    is_valid, message = validator.validate()

                    if not is_valid:
                        self.log(message)

            except ConnectionError as e:
                print("ERROR REDIS CONNECTION: {}".format(e))
            except Exception as e:
                print('ERROR NO CONTROLADO: {}'.format(str(e)))
                sys.exit()

    def log(self, message):
        """
        registrar alerta por validacion fallida
        """

        notifier = Notifier(message)
        notifier.record_in_plain_text()
        notifier.print_warning_log()
