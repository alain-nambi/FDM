import logging

class ClientInfoFilter(logging.Filter):
    def filter(self, record):
        if not hasattr(record, 'client_ip'):
            record.client_ip = '-'
        if not hasattr(record, 'user'):
            record.user = '-'
        return True