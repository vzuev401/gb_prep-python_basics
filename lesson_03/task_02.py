from typing import Optional, Union


def my_func(
    *,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    year_of_birth: Optional[Union[str, int]] = None,
    city: Optional[str] = None,
    email: Optional[str] = None,
    phone: Optional[str] = None
) -> None:
    """Prints info about a person.

    Takes only keyword-arguments.

    Parameters
    ----------
    first_name: str, optional
    last_name: str, optional
    year_of_birth: {str, int}, optional
    city: str, optional
    email: str, optional
    phone: str, optional

    Returns
    -------
    None
    """
    print(
        'person: '
        f'{first_name if first_name is not None else "_"} '
        f'{last_name if last_name is not None else "_"}, '
        f'born at {year_of_birth if year_of_birth is not None else "_"}, '
        f'live in {city if city is not None else "_"}, '
        f'email: {email if email is not None else "_"}, '
        f'phone: {phone if phone is not None else "_"}'
    )

