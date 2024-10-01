from typing import Optional, Sequence, Union

class MemcmpEncoding:
    Binary: "MemcmpEncoding"
    def __int__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...

class Memcmp:
    def __init__(
        self,
        offset: int,
        bytes_: Union[str, Sequence[int], bytes],
        encoding: Optional[MemcmpEncoding] = None,
    ): ...
    @property
    def offset(self) -> int: ...
    @property
    def bytes_(self) -> Union[str, Sequence[int]]: ...
    @property
    def encoding(self) -> Optional[MemcmpEncoding]: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __richcmp__(self, other: "Memcmp", op: int) -> bool: ...
    def __bytes__(self) -> bytes: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "Memcmp": ...

class RpcFilterTypeFieldless:
    TokenAccountState: "RpcFilterTypeFieldless"
    def __int__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    @staticmethod
    def from_string(s: str) -> "RpcFilterTypeFieldless": ...
    @staticmethod
    def default() -> "RpcFilterTypeFieldless": ...

RpcFilterType = Union[int, Memcmp, RpcFilterTypeFieldless]
