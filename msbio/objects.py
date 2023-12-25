from typing import Union, List, final

# ! Integers
@final
class int32(int):
    pass

@final
class int64(int):
    pass

# ! Vars
SUPPORTED_TYPES: List[type] = [int32, int64, float, bytes, str, bool]

# ! Types
ValidatedType = Union[int32, int64, float, bytes, str, bool]