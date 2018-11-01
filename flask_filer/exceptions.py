
class InvalidPathError(ValueError):
    """
    Exception raised when a path is not valid.
    """
    code = 'invalid-path'
    template = 'Path {0.path!r} is not valid.'

    def __init__(self, message=None, path=None):
        self.path = path
        message = self.template.format(self) if message is None else message
        super(InvalidPathError, self).__init__(message)
