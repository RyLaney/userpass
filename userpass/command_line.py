"""command line wrapper for module
"""

import userpass.generate


def main():
    """main function
    """
    print(f'ACESS_KEY={userpass.generate.token_urlsafe(32)}')
    print(f'SECRET_KEY={userpass.generate.token_urlsafe(64)}')
