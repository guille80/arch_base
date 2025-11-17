class EcoPlugin:
    def __init__(self, message: str):
        self.message = message

    def echo(self) -> str:
        """Devuelve el mensaje original."""
        return self.message

    def shout(self) -> str:
        """Devuelve el mensaje en mayúsculas."""
        return self.message.upper()