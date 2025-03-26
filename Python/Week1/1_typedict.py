# StaticTypeChecking: by mypy or Pyright

# Not Validate Data, only for type hinting
# we trust developer/llm to provide in correct format

from typing import TypedDict

class Movie(TypedDict):
    name: str
    year: int
    casts: list[str]

m1: Movie = {'name':'Kick', 'year':'32'}
m1 = Movie({'name':'Kick', 'year':'32'})
m1 = Movie(name='hritik', year='234')

print(type(m1), m1)