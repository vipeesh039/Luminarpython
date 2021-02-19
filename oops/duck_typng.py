
class Pycharm:
    def start(self):
        print("start with pycharm ide")
class Vscode:
    def start(self):
        print("start wth vscode ide")

class Django:
    def execute(self,ide):
        ide.start()

py=Vscode()
dj=Django()
dj.execute(py)
#the operation is same