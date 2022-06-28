from infra.adapter.UserAdapter import UserAdapter

class DateCompare:

    def compare(a, b):
        if not isinstance(a, UserAdapter) or not isinstance(b, UserAdapter):
            return NotImplemented

        if a.birth.year > b.birth.year:
            return -1
        if a.birth.year < b.birth.year:
            return 1
        if a.birth.month > b.birth.month:
            return -1
        if a.birth.month < b.birth.month:
            return 1
        if a.birth.day > b.birth.day:
            return -1
        if a.birth.day < b.birth.day:
            return 1
        return 0