===========
userpass
===========


A small username (access_key) and password (secret_key) generator. It
is a wrapper for python secrets and uses examples from the docs to save
a few keystrokes for a common task.


Description
===========


A helper script useful when setting up services that need
a username and password or access_key and secret_key.

The command prints randomly generated keys.

.. code-block:: bash

    % userpass
    ACCESS_KEY=3MNJQ2ZezP531s6PEJlH0AP6mhoQjM3MRMDFY8K-BuI
    SECRET_KEY=l894Hssk4ltQKgkg8G8IWyyXZjO-JxBvieQClvtoJ7pgS6DX8g7IAmISlwvl-gSIsSr8tGUAVgDWYVsPl_robg


Module Usage
============

    >>> import userpass.generate
    >>> access_key = userpass.generate.alphanumeric(24)
    >>> secret_key = userpass.generate.alphanumeric(64)
    >>> security_token = userpass.generate.urlsafe()
    >>> passphrase = userpass.generate.passphrase(4)


Installation
============

.. code-block:: bash

    % python setup.py test
    % python setup.py install

