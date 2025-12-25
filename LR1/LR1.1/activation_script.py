import sys
import re
from urllib.request import urlopen
from importlib.abc import PathEntryFinder
from importlib.util import spec_from_loader


# URLLoader
class URLLoader:
    def create_module(self, spec):
        return None

    def exec_module(self, module):
        with urlopen(module.__spec__.origin) as page:
            source = page.read()
        code = compile(source, module.__spec__.origin, mode="exec")
        exec(code, module.__dict__)


# URLFinder
class URLFinder(PathEntryFinder):
    def __init__(self, url, available):
        self.url = url
        self.available = available

    def find_spec(self, name, target=None):
        if name in self.available:
            origin = f"{self.url}/{name}.py"
            loader = URLLoader()
            return spec_from_loader(name, loader, origin=origin)
        return None


# url_hook
def url_hook(path):
    if not path.startswith(("http://", "https://")):
        raise ImportError

    with urlopen(path) as page:
        data = page.read().decode("utf-8")

    filenames = re.findall(r"[a-zA-Z_][a-zA-Z0-9_]*\.py", data)
    modnames = {name[:-3] for name in filenames}

    return URLFinder(path, modnames)



sys.path_hooks.append(url_hook)

print("Custom url_hook added to sys.path_hooks")
print(sys.path_hooks)
