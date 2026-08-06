"""
OGS Framework Exceptions
"""


class OGSException(Exception):
    """
    Base exception for OGS.
    """

    pass


class ValidationError(OGSException):
    """
    Raised when validation fails.
    """

    pass


class FactoryError(OGSException):
    """
    Raised when object creation fails.
    """

    pass


class AnalyzerError(OGSException):
    """
    Raised when analysis fails.
    """

    pass


class CollectionError(OGSException):
    """
    Raised for collection related errors.
    """

    pass