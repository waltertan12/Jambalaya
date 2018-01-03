
def all_params_are_of_type(params: list, paramsType: type) -> None:
    """
    Check that the list of parameters are all of the same type 
    :param params: list<str>
    :param paramsType: type
    :return: 
    :raises:
        - TypeError if params or paramsType are not of type list and type respectively
        - TypeError if any of the objects passed in params are not of type paramsType
    """
    if not isinstance(params, list) or not isinstance(paramsType, type):
        raise TypeError("expected parameters to be of list, and type respectively")
    for param in params:
        if not isinstance(param, type):
            raise TypeError("Expected type", type, "but received", type(param))