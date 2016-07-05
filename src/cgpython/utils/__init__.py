from ._path import Path as NativePath


class Path(NativePath):

    def __init__(self, *args, **kwargs):
        super(Path, self).__init__(*args, **kwargs)
