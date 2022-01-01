class Character:

    def __init__(
        self,
        life,
        attack,
        defence,
        speed,
        effects,
        level=1,
    ):
        self._life = life
        self._attack = attack
        self._defence = defence
        self._speed = speed
        self._effects = effects
        self._level = level

    @property
    def life(self) -> int:
        return self._life

    @property
    def attack(self) -> int:
        return self._attack

    @property
    def defence(self) -> int:
        return self._defence

    @property
    def speed(self) -> int:
        return self._speed

    @property
    def effects(self) -> int:
        return self._effects

    @property
    def level(self) -> int:
        return self._level
