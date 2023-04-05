from abc import ABC, abstractmethod


class Importer(ABC):
    @classmethod
    def ext_validation(cls, path: str, file_ext: str):
        ext = path.split(".")[-1]

        if ext == file_ext:
            return True

        raise ValueError('Arquivo inválido')

    @abstractmethod
    def import_data(path: str):
        raise NotImplementedError
