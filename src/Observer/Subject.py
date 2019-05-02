from Observer.Observer import Observer


class Subject:

    _observers = set()
    _subject_state = None

    def attach(self, observer):
        self._observers.add(observer)

    def detach(self, observer):
        self._observers.discard(observer)

    def _notify(self):
        for observer in self._observers:
            observer.update(self._subject_state)
