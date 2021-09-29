class World:
    """
    :data Dictionary from the World List Parser
    Used to hold world data
    """

    def __init__(self, data):
        assert dict, type(data)
        self.pvp: bool = None
        self.number: int = None
        self.player_count: int = None
        self.country: str = None
        self.type: str = None
        self.activity: str = None

        self._parse_data(data)

    def _parse_data(self, data) -> None:
        if 'pvp' in data:
            self.pvp = data['pvp']

        if 'number' in data:
            self.number = data['number']

        if 'player_count' in data:
            self.player_count = data['player_count']

        if 'country' in data:
            self.country = data['country']

        if 'type' in data:
            self.type = data['type']

        if 'activity' in data:
            self.activity = data['activity']

    def to_dict(self) -> dict:
        return {
            'pvp': self.pvp,
            'number': self.number,
            'player_count': self.player_count,
            'country': self.country,
            'type': self.type,
            'activity': self.activity,
        }
