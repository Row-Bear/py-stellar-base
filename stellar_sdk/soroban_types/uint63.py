from .base import BaseScValAlias
from ..xdr import SCVal, SCValType, Int64 as Int64

__all__ = ["Uint63"]


class Uint63(BaseScValAlias):
    def __init__(self, value: int):
        self.value: int = value

    def _to_xdr_sc_val(self) -> SCVal:
        return SCVal(SCValType.SCV_U63, u63=Int64(self.value))
