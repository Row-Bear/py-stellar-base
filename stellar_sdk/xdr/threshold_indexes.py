# This is an automatically generated file.
# DO NOT EDIT or your changes may be overwritten
import base64
from enum import IntEnum
from xdrlib import Packer, Unpacker

from ..__version__ import __issues__
from ..exceptions import ValueError
from ..type_checked import type_checked

__all__ = ["ThresholdIndexes"]


@type_checked
class ThresholdIndexes(IntEnum):
    """
    XDR Source Code
    ----------------------------------------------------------------
    enum ThresholdIndexes
    {
        THRESHOLD_MASTER_WEIGHT = 0,
        THRESHOLD_LOW = 1,
        THRESHOLD_MED = 2,
        THRESHOLD_HIGH = 3
    };
    ----------------------------------------------------------------
    """

    THRESHOLD_MASTER_WEIGHT = 0
    THRESHOLD_LOW = 1
    THRESHOLD_MED = 2
    THRESHOLD_HIGH = 3

    def pack(self, packer: Packer) -> None:
        packer.pack_int(self.value)

    @classmethod
    def unpack(cls, unpacker: Unpacker) -> "ThresholdIndexes":
        value = unpacker.unpack_int()
        return cls(value)

    def to_xdr_bytes(self) -> bytes:
        packer = Packer()
        self.pack(packer)
        return packer.get_buffer()

    @classmethod
    def from_xdr_bytes(cls, xdr: bytes) -> "ThresholdIndexes":
        unpacker = Unpacker(xdr)
        return cls.unpack(unpacker)

    def to_xdr(self) -> str:
        xdr_bytes = self.to_xdr_bytes()
        return base64.b64encode(xdr_bytes).decode()

    @classmethod
    def from_xdr(cls, xdr: str) -> "ThresholdIndexes":
        xdr_bytes = base64.b64decode(xdr.encode())
        return cls.from_xdr_bytes(xdr_bytes)

    @classmethod
    def _missing_(cls, value):
        raise ValueError(
            f"{value} is not a valid {cls.__name__}, please upgrade the SDK or submit an issue here: {__issues__}."
        )
