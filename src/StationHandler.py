class StationHandler:

    def __init__(self):
        self.expected = []
        self.confirmed = []
        self.finished = []
    
    def addExpected(self, expected: int):
        print(f"Added expected Value: {expected}")
        self.expected.append(expected)
    
    def confirm(self, confirmed: int):
        self.expected.remove(confirmed)
        self.confirmed.append(confirmed)
    
    def finish(self, finished: int):
        self.confirmed.remove(finished)
        self.finish.append(finished)
    
    def leftQueueLen() -> int:
        return self.expected.len() + self.confirm.len()
    
    def rightQueueLen() -> int:
        return self.finish.len()