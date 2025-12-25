import sys
import re
import requests
from importlib.abc import PathEntryFinder
from importlib.util import spec_from_loader


# URLLoader
class URLLoader:
    def create_module(self, spec):
        return None

    def exec_module(self, module):
        response = requests.get(module.__spec__.origin)
        response.raise_for_status()  # если ошибка HTTP — исключение

        source = response.text
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

    response = requests.get(path)
    response.raise_for_status()

    filenames = re.findall(r"[a-zA-Z_][a-zA-Z0-9_]*\.py", response.text)
    modnames = {name[:-3] for name in filenames}

    return URLFinder(path, modnames)



sys.path_hooks.append(url_hook)

print("Custom url_hook (requests-based) added to sys.path_hooks")
print(sys.path_hooks)
