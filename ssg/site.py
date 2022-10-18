from pathlib import Path

class Site:
    """docstring forSite
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def creat_dir(self, path):
        #directory contains full path to the destination folder
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.creat_dir(path)
