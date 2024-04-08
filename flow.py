class Flow:
    def __init__(self, deadline, period, traveltime):
        self._deadline = deadline
        self._period = period
        self._traveltime = traveltime

    @property
    def deadline(self):
        return self._deadline

    @property
    def period(self):
        return self._period

    @property
    def traveltime(self):
        return self._traveltime
    