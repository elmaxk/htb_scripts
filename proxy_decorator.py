#!/usr/bin/env python


class User(object):
    def __init__(self, roles):
        self.roles = roles


class Unauthorized(Exception):
    print('Unauthorized')


def protect(role):
    def _protect(function):
        def __protect(*args, **kw):
            user = globals().get('user')
            if user is None or role not in user.roles:
                raise Unauthorized("I won't tell you")
            return function(*args, **kw)
        return __protect
    return _protect


# Example repl code

Max = User(('admin', 'user'))
bill = User(('user'))


class RecipeVault(object):
    @protect('admin')
    def get_waffle_recipe(self):
        print('Use tons of butter.')