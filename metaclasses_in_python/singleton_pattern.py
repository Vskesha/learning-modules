from dataclasses import dataclass


class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


@dataclass
class Settings(metaclass=Singleton):
    db: str = "MySQL"
    port: int = 3306


class NewSettings(Settings):
    pass


if __name__ == '__main__':
    connect = Settings()
    connect2 = Settings()
    new_connect = NewSettings()
    print(connect2.port)
    connect.port = 5432
    print(connect2.port)
    print(new_connect.port)
