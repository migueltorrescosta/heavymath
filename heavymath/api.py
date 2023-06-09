from enum import Enum

from ninja import NinjaAPI, Schema

from .algorithms import simple_factorization, calculate_collatz_sequence

api = NinjaAPI()


class FactorizationMethods(str, Enum):
    SIMPLE = "simple"
    MIDDLE_OUT = "middle_out"


class FactorizationSchema(Schema):
    n: int
    factors: list[int]
    is_prime: bool
    method: FactorizationMethods


class CollatzSequenceSchema(Schema):
    n: int
    sequence: list[int]
    length: int
    terminated: bool


@api.get(
    path="/factorize",
    summary="Prime factorization",
    description="Returns the factors of a number n as a list",
    response=FactorizationSchema)
def factorize(request, n: int):
    # TODO: Add async support ( 1st algorithm to completion )
    # done, pending = await asyncio.wait(
    #     [something_to_wait(), something_else_to_wait()],
    #     return_when=asyncio.FIRST_COMPLETED)
    factors = sorted(simple_factorization(n))
    return FactorizationSchema(
        n=n,
        factors=factors,
        is_prime=(len(factors) == 1),
        method=FactorizationMethods.SIMPLE.value,
    )


@api.get(
    path="/collatz",
    summary="Collatz sequence",
    description="Returns the Collatz sequence starting at n",
    response=CollatzSequenceSchema)
def collatz(request, n: int, max_length: int = 1000):
    sequence = calculate_collatz_sequence(n, max_length)
    return CollatzSequenceSchema(
        n=n,
        length=len(sequence),
        sequence=sequence,
        terminated=sequence[-1] == 1,
    )
