from io import BytesIO
from typing import IO, Dict, Any
from _typeshed import ReadableBuffer
from .decoder import Decoder
from .encoder import Encoder
from .objects import ValidatedType

# ! Load Methods
def load(
    io: IO[bytes],
    encoding: str='utf-8',
    errors: str='ignore'
) -> Dict[str, ValidatedType]:
    return Decoder(io).load(errors, encoding)

def loads(
    data: ReadableBuffer,
    encoding: str='utf-8',
    errors: str='ignore'
) -> Dict[str, ValidatedType]:
    return Decoder(BytesIO(data)).load(errors, encoding)

# ! Dump Methods
def dump(
    data: Dict[str, Any],
    io: IO[bytes],
    encoding: str='utf-8',
    errors: str='ignore',
    type_checking: bool=True
) -> None:
    return Encoder(io).dump(data, encoding, errors, type_checking)

def dumps(
    data: Dict[str, Any],
    encoding: str='utf-8',
    errors: str='ignore',
    type_checking: bool=True
) -> bytes:
    encoder = Encoder(BytesIO())
    encoder.dump(data, encoding, errors, type_checking)
    encoder.io.seek(0)
    return encoder.io.read()