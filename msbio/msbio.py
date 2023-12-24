from io import BytesIO
from typing import IO, Dict, Any
from _typeshed import ReadableBuffer
from .decoder import Decoder

# ! Load Methods
def load(
    io: IO[bytes],
    errors: str='ignore',
    encoding: str='utf-8'
) -> Dict[str, Any]:
    return Decoder(io).load(errors, encoding)

def loads(
    data: ReadableBuffer,
    errors: str='ignore',
    encoding: str='utf-8'
) -> Dict[str, Any]:
    return Decoder(BytesIO(data)).load(errors, encoding)