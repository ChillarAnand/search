from haystack.inputs import Clean


class Words(Clean):
    input_type_name = 'words'
    post_process = False

    def __init__(self, query_string, **kwargs):
        self.original = query_string
        super().__init__(query_string, **kwargs)

    def prepare(self, query_obj):
        query_string = super().prepare(query_obj)
        qs = ' OR '.join(query_string.split(' '))
        return qs
