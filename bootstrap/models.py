# -*- coding: utf-8 -*-
"""
bootstrap.models
~~~~~~~~

This module contains the primary objects that power Bootstrap.

:copyright: (c) 2012 by Firstname Lastname.
:license: ISC, see LICENSE for more details.

"""

from .exceptions import BoostrapException


class World(object):
    """The :class:`World <World>` object. It carries out all functionality
    of World."""

    def __init__(self, state=None):

        if state:
            self.state = state

    def get_state():
        """Get the state of the world"""
        return state

    def set_state(state=None):
        """Set the state of the world"""
        if state:
            self.state = state
        else:
            raise BootstrapException()
