class EngineRegistry:

    def __init__(self):

        self._engines = {}

    # ---------------------------------------------

    def register(
        self,
        engine
    ):

        self._engines[
            engine.name
        ] = engine

    # ---------------------------------------------

    def get(
        self,
        name
    ):

        return self._engines[name]

    # ---------------------------------------------

    def list(self):

        return list(
            self._engines.keys()
        )