from anillo.http import NotFound, NoContent, Created, Ok


def test(request):
    return Ok({
        "one": 1,
        "two": 2,
    })

