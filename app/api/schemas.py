from pydantic import BaseModel, UUID4


class BaseItemIn(BaseModel):
    id: UUID4 | str | None = None
    title: str
    description: str


class BaseItemOut(BaseModel):
    id: UUID4 | str
    title: str
    description: str

    class Config:
        orm_mode = True


class MenuIn(BaseItemIn):
    pass


class SubmenuIn(BaseItemIn):
    pass


class DishIn(BaseItemIn):
    price: str | float


class MenuOut(BaseItemOut):
    submenus_count: int
    dishes_count: int


class SubmenuOut(BaseItemOut):
    dishes_count: int


class DishOut(BaseItemOut):
    price: str | float