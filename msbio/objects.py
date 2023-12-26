from typing import Union, List, final

# ! Integers
@final
class int32(int):
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"

@final
class int64(int):
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"

# ! Vars
SUPPORTED_TYPES: List[type] = [int32, int64, float, bytes, str, bool]

# ! Types
ValidatedType = Union[int32, int64, float, bytes, str, bool]