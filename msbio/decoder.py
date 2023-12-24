from struct import unpack
from typing import IO, Literal, Dict, Any
from .objects import int32, int64

# ! Main Class
class Decoder:
    def __init__(self, io: IO[bytes]) -> None:
        assert io.readable()
        self.io = io
    
    def decode(
        self,
        type_id: Literal[0, 1, 2, 3, 4, 5],
        errors: str='ignore',
        encoding: str='utf-8'
    ) -> Any:
        if type_id == 0:    #? bool
            return bool(unpack("!b", self.io.read(1))[0])
        elif type_id == 1:  #? int32
            return int32(unpack("!i", self.io.read(4))[0])
        elif type_id == 2:  #? int64
            return int64(unpack("!q", self.io.read(8))[0])
        elif type_id == 3:  #? float32
            return float(unpack("!f", self.io.read(4))[0])
        elif type_id == 4:  #? str
            length = unpack("!h", self.io.read(2))[0]
            return self.io.read(length).decode(encoding, errors)
        elif type_id == 5:  #? bytes
            length = unpack("!i", self.io.read(4))[0]
            return self.io.read(length)
        raise TypeError(f"There is no type under this ID: {type_id}.")
    
    def load(
        self,
        errors: str='ignore',
        encoding: str='utf-8'
    ) -> Dict[str, Any]:
        data = {}
        count = unpack("!i", self.io.read(4))[0]
        for _ in range(count):
            length = unpack("!h", self.io.read(2))[0]
            key = self.io.read(length).decode(encoding, errors)
            type_id = unpack("!b", self.io.read(1))[0]
            data[key] = self.decode(type_id)
        return data