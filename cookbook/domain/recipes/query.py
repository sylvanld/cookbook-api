from fastapi import Query


class RecipeQuery:
    name: str

    @classmethod
    def from_request(cls, name: str = Query(None, description="Name or part of the name of the searched recipe(s)")):
        query = cls()
        query.name = name
        return query
