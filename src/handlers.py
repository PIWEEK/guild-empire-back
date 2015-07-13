# coding: utf-8

# third party
from anillo.http import Ok, NotImplemented

# guild empire back
from dummy import DUMMY_GET


def get_turn(request):
    return Ok(DUMMY_GET)


def post_turn(request):
    return NotImplemented()
