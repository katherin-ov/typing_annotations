# ==============================================
#  УРОВЕНЬ: BASIC
# ==============================================

# === Задача 1: any ===
from typing import Any


def foo(x: Any):
    """⬆️ Change me. No need to implement the function."""


# === Задача 2: dict ===
def foo(x: dict[str, str]):
    pass


# === Задача 3: final ===
from typing import Final, List, Any


my_list: Final[List[Any]] = []


# === Задача 4: kwargs ===
def foo(**kwargs: int | str):
    ...


# === Задача 5: list ===
def foo(x: list[str]):
    pass

# === Задача 6: optional ===
from typing import Optional

def foo(x: Optional[int | None] = None):
    pass


# === Задача 7: parameter ===
def foo(x: int):
    pass


# === Задача 8: return ===
def foo() -> int:
    return 1


# === Задача 9: tuple ===
def foo(x: tuple[str, int]):
    pass


# === Задача 10: typealias ===
from typing import List

Vector = List[float]


# === Задача 11: union ===
from typing import Union


def foo(x: Union[str, int]):
    pass


# === Задача 12: variable ===
a: int


# ==============================================
#    УРОВЕНЬ: INTERMEDIATE
# ==============================================

# === Задача 1: await ===
from typing import Awaitable


def run_async(x: Awaitable[int]):
    ...


# === Задача 2: callable ===
from typing import Callable

SingleStringInput = Callable[[str], None]


# === Задача 3: class-var ===
from typing import ClassVar

class Foo:
    """Hint: No need to write __init__"""
    bar: ClassVar[int]


# === Задача 4: decorator ===
from typing import Callable, TypeVar

T = TypeVar("T", bound=Callable)

def decorator(func: T) -> T:
    return func


# === Задача 5: empty-tuple ===
def foo(x: tuple[()]):
    pass


# === Задача 6: generic ===
from typing import TypeVar

T = TypeVar("T")


def add(a: T, b: T) -> T:
    ...


# === Задача 7: generic2 ===
from typing import TypeVar

T = TypeVar("T", int, str)

def add(a: T, b: T) -> T:
    ...


# === Задача 8: generic3 ===
from typing import TypeVar

T = TypeVar("T", bound=int)

def add(a: T) -> T:
    ...


# === Задача 9: instance-var ===
class Foo:
    """Hint: you don't need to write __init__"""
    bar: int


# === Задача 10: literal ===
from typing import Literal

def foo(direction: Literal['left', 'right']):
    ...


# === Задача 11: literalstring ===
from typing import Iterable, LiteralString


def execute_query(sql: LiteralString, parameters: Iterable[str] = ...):
    ...


# === Задача 12: self ===
import typing


class Foo:
    def return_self(self) -> typing.Self:
        ...


# === Задача 13: typed-dict ===
from typing import TypedDict

class Student(TypedDict):
    name: str
    age: int
    school: str


# === Задача 14: typed-dict2 ===
from typing import TypedDict, NotRequired

class Student(TypedDict):
    name: str
    age: int
    school: NotRequired[str]


# === Задача 15: typed-dict3 ===
from typing import TypedDict, NotRequired

class Person(TypedDict):
    name: str
    age: NotRequired[int]
    gender: NotRequired[str]
    address: NotRequired[str]
    email: NotRequired[str]


# === Задача 16: unpack ===
from typing import TypedDict


class Person(TypedDict):
    name: str
    age: int


def foo(name: str, age: int, **kwargs):
    ...


# ==============================================
#    УРОВЕНЬ: ADVANCE
# ==============================================

# === Задача 1: buffer ===
from collections.abc import Buffer

def read_buffer(b: Buffer):
    ...


# === Задача 2: callable-protocol ===
from typing import Protocol


class SingleStringInput(Protocol):
    def __call__(self, name: str) -> None: ...


# === Задача 3: decorator ===
from typing import Callable, TypeVar, ParamSpec

P = ParamSpec('P')
R = TypeVar('R')


def decorator(message: str) ->Callable[[Callable[P, R]], Callable[P, R]]:
    ...


# === Задача 4: Descriptor ===
from typing import TypeVar, Generic, Self, overload

T = TypeVar('T')


class Descriptor(Generic[T]):
    @overload
    def __get__(self, instance: None, owner: type) -> Self:
        ...

    @overload
    def __get__(self, instance: T, owner: type[T]) -> str:
        ...

    def __get__(self, instance, owner) -> Self | str:
        ...


# === Задача 5: forward ===
class MyClass:
    def __init__(self, x: int) -> None:
        self.x = x

    def copy(self) -> 'MyClass':
        copied_object = MyClass(x=self.x)
        return copied_object
