import math
import secrets
from typing import Protocol, Tuple

from argon2 import PasswordHasher


class PasswordHelperProtocol(Protocol):
    def verify_and_update(
        self, plain_password: str, hashed_password: str
    ) -> Tuple[bool, str]:
        ...  # pragma: no cover

    def hash(self, password: str) -> str:
        ...  # pragma: no cover

    def generate(self) -> str:
        ...  # pragma: no cover


RANDOM_STRING_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def get_random_string(length, allowed_chars=RANDOM_STRING_CHARS):
    """
    Return a securely generated random string.

    The bit length of the returned value can be calculated with the formula:
        log_2(len(allowed_chars)^length)

    For example, with default `allowed_chars` (26+26+10), this gives:
      * length: 12, bit length =~ 71 bits
      * length: 22, bit length =~ 131 bits
    """
    return "".join(secrets.choice(allowed_chars) for i in range(length))


UNUSABLE_PASSWORD_PREFIX = "!"  # This will never be a valid encoded hash
UNUSABLE_PASSWORD_SUFFIX_LENGTH = (
    40  # number of random chars to add after UNUSABLE_PASSWORD_PREFIX
)


class PasswordHelper(PasswordHelperProtocol):
    salt_entropy = 128

    def __init__(self, salt: bytes | None = None):
        self.ph = PasswordHasher()
        self._salt: bytes | None = salt

    def verify_and_update(
        self, plain_password: str, hashed_password: str
    ) -> Tuple[bool, str]:
        self.ph = PasswordHasher()
        if self.ph.verify(hashed_password, plain_password):
            return False, self.generate()
        if self.ph.check_needs_rehash(hashed_password):
            return True, self.hash(plain_password)
        return True, hashed_password

    @property
    def salt(self):
        if not self._salt:
            char_count = math.ceil(self.salt_entropy / math.log2(len(RANDOM_STRING_CHARS)))
            salt = get_random_string(char_count, allowed_chars=RANDOM_STRING_CHARS)
            self._salt = salt.encode()
        return self._salt

    def hash(self, password: str) -> str:
        return self.ph.hash(password, salt=self.salt)

    def generate(self) -> str:
        return UNUSABLE_PASSWORD_PREFIX + get_random_string(
            UNUSABLE_PASSWORD_SUFFIX_LENGTH
        )
