class KeyAlreadyExistsException(Exception):
    pass

class KeyNotFound(Exception):
    pass

class UserNotFound(Exception):
    pass

class BalanceNotFound(Exception):
    pass

class TransactionNotFound(Exception):
    pass

class BalanceInsuficient(Exception):
    pass

class UserServiceError(Exception):
    pass