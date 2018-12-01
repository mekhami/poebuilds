import attr

@attr.s
class BaseItem(object):
    id = attr.ib(type=int)
    frame = attr.ib(type=int)
    name = attr.ib(type=str)
    type = attr.ib(type=str)
    icon = attr.ib(type=str)
    tier = attr.ib()
    lvl = attr.ib()
    quality = attr.ib()
    corrupted = attr.ib()
    links = attr.ib()
    ilvl = attr.ib()
    variation = attr.ib()
    category = attr.ib()
    group = attr.ib()


@attr.s
class ItemMod(object):
    name_orig = attr.ib(type=str)
    name = attr.ib(type=str)
    ranges = attr.ib(kw_only=True, default=None)
    values = attr.ib(kw_only=True, default=None)
    isVariable = attr.ib(type=bool, kw_only=True)
