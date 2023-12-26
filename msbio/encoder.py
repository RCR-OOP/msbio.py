from struct import pack
from typing import IO, Dict, Any
from .objects import (
    SUPPORTED_TYPES,
    ValidatedType,
    int32,
    int64
)

# ! Main Class
class Encoder:
    def __init__(self, io: IO[bytes]) -> None:
        assert io.writable()
        self.io = io
    
    def encode(
        self,
        value: ValidatedType,
        encoding: str='utf-8',
        errors: str='strict'
    ) -> bytes:
        if isinstance(value, bool):
            return pack("!b", 0) + pack("!b", value)
        elif isinstance(value, int32):
            return pack("!b", 1) + pack("!i", value)
        elif isinstance(value, int64):
            return pack("!b", 2) + pack("!q", value)
        elif isinstance(value, float):
            return pack("!b", 3) + pack("!f", value)
        elif isinstance(value, str):
            return pack("!b", 4) + pack("!h", len(value)) + value.encode(encoding, errors)
        elif isinstance(value, bytes):
            return pack("!b", 5) + pack("!i", len(value)) + value
        raise TypeError(f"This type is not supported: {type(value)}.")
    
    def check(self, data: Dict[str, Any]) -> None:
        for key, value in data.items():
            if type(value) not in SUPPORTED_TYPES:
                raise TypeError(f"The value with the key '{key}' is an unsupported type: {data}.")
    
    def dump(
        self,
        data: Dict[str, ValidatedType],
        encoding: str='utf-8',
        errors: str='strict',
        type_checking: bool=True
    ) -> None:
        assert isinstance(data, dict)
        if type_checking:
            self.check(data)
        self.io.write(pack("!i", len(data)))
        for key, value in data.items():
            self.io.write(
                pack("!h", len(key)) + key.encode(encoding, errors) + self.encode(value, encoding, errors)
            )