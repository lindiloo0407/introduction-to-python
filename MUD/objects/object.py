class Object:
    def __init__(
        self,
        d={
            "name": None,
            "room_description": None,
            "key_words": (None),
            "description": None,
        },
    ):
        self.name = d["name"]
        self.room_description = d["room_description"]
        self.key_words = d["key_words"]
        self.description = d["description"]
        self.take = False


class Item(Object):
    def __init__(self, d):
        super(d)
        self.weight = d.get("weight", 0)
        self.mod = d.get("mod", [])
        self.take = True


class Weapon(Item):
    def __init__(self, d):
        self.dice = d.get("dice", "1d6")
        self.hitroll = d.get("hitroll", 0)
        self.damroll = d.get("damroll", 0)
