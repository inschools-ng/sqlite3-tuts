@staticmethod
    def _current_time():
        return pytz.utc.localize(datetime.datetime.utcnow())
        # return 1