"""
        An example for creating custom containers similar to list or dictionary
    """


class TagGames:
    """
        An example for creating custom containers similar to list or dictionary
    """

    def __init__(self):
        # use __ before the attribute or property name to make it as a private member
        # ex: __<Attribute_NAME> self.__tag
        self.__tag = {}

    def add(self, tag):
        """
            convert the given tag to lower and increment to count by 1
        """
        self.__tag[tag.lower()] = self.__tag.get(tag.lower(), 0) + 1

    def __len__(self):
        return len(self.__tag)

    def __iter__(self):
        return iter(self.__tag)


tag_games = TagGames()
tag_games.add("CSGO")
tag_games.add("CSGO")
tag_games.add("EuroTruck")
tag_games.add("eurotruck")

print(tag_games.__tag)
