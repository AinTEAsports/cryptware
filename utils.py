import os
from dataclasses import dataclass
from cryptography.fernet import Fernet


def get_all_files(path : str) -> iter :
    for root, _, files in os.walk(path):
        for file in files:
            yield os.path.join(root, file)


@dataclass(frozen=True)
class File:
    filename: str
    
    def __post__init__(self) -> None :
        if not os.path.exists(self.filename) and not os.path.isfile(self.filename):
            raise FileNotFoundError(f"File {self.filename} not found")


    @property
    def absolute_path(self) -> str :
        return os.path.abspath(self.filename)
    
    
    @property
    def content(self) -> bytes :
        with open(self.filename, "rb") as f:
            file_content = f.read()

        return file_content
    
    
    def encrypt(self, key : str = "") -> None :
        if not key:
            key = Fernet.generate_key()
            
        encrypted_content = Fernet(key).encrypt(self.content)
        
        with open(self.filename, "wb") as f:
            f.write(encrypted_content)
    
    
    def decrypt(self, key : str) -> None :
        decrypted_content = Fernet(key).decrypt(self.content)
        
        with open(self.filename, "wb") as f:
            f.write(decrypted_content)

