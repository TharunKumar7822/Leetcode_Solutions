class BrowserHistory:

    def __init__(self, homepage):
        self.history = [homepage]
        self.current = 0

    def visit(self, url):
        # Remove all forward history
        self.history = self.history[:self.current + 1]

        # Add new page
        self.history.append(url)

        # Move to the new page
        self.current += 1

    def back(self, steps):
        # Move back, but not before the first page
        self.current = max(0, self.current - steps)

        return self.history[self.current]

    def forward(self, steps):
        # Move forward, but not beyond the last page
        self.current = min(len(self.history) - 1,
                           self.current + steps)

        return self.history[self.current]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)