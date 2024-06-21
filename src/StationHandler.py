class StationHandler:

    def __init__(self):
        self.expected = []
        self.confirmed = []
        self.finished = []
    
    def addExpected(self, expected_item_id: int):
        print(f"Added expected Value: {expected_item_id}")
        self.expected.append(expected_item_id)
    
    def confirm(self, confirmed_item_item: int):
        self.expected.remove(confirmed_item_item)
        self.confirmed.append(confirmed_item_item)
    
    def finish(self, finished_item_id: int):
        self.confirmed.remove(finished_item_id)
        self.finished.append(finished_item_id)
    
    def send(self, send_item_id: int):
        self.finished.remove(left)
    
    def leftQueueLen(self) -> int:
        return self.expected.len() + self.confirmed.len()
    
    def rightQueueLen(self) -> int:
        return self.finished.len()

    def isIdle(self) -> bool:
        return (self.leftQueueLen() + self.rightQueueLen()) == 0