from struct import pack
from typing import IO, Literal, Union, Dict, Any
from .objects import SUPPORTED_TYPES, int32, int64

# ! Main Class
class Encoder:
    def __init__(self, io: IO[bytes]) -> None:
        assert io.writable()
        self.io = io
    
    def encode(self, key: str, value: ...) -> ...:
        # TODO: Needed to write the encoding code.
        ...
    
    def check(self, data: Dict[str, Any]) -> None:
        for key, value in data.items():
            if type(value) not in SUPPORTED_TYPES:
                raise TypeError(f"The value with the key '{key}' is an unsupported type: {data}.")
    
    def dump(
        self,
        data: Dict[str, Any],
        errors: str='ignore',
        encoding: str='utf-8',
        type_checking: bool=True
    ) -> None:
        assert isinstance(data, dict)
        if type_checking:
            self.check(data)
        # TODO: Needed to write the encoding code.