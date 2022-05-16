from typing import Dict, Tuple, List, Any, Set, Optional

a: int = 1
b: str = "2345t6"
c: float = 0.01
boolean: bool = False

d: Dict[Optional[str, int, None], Dict[bool, Dict[str, int]]] = {
    "3": {
        False: {
            "str": 123
        }
    },
    2134: {
        True: {
            "klcdmslk": 73473
        }
    },
}
dd = {"3": False}
t: Tuple[int, bool] = (1, False)
l: List[int] = ["lslks", False, 123]


class A:
    pass


a_obj: A = A()

print(a)