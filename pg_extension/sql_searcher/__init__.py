import requests
from multicorn import ForeignDataWrapper
from multicorn.utils import log_to_postgres, ERROR, WARNING


class ConstantForeignDataWrapper(ForeignDataWrapper):

    def __init__(self, options, columns):
        super(ConstantForeignDataWrapper, self).__init__(options, columns)
        self.columns = columns
        self.options = options
        self.set_options()
    
    def set_options(self):
        self.backend_route = 'http://sql_searcher_backend:8080/search'
        if self.options['hostname']:
            self.backend_route = f"{self.options['hostname']}/search"
        

    def execute(self, quals, columns):
        if columns:
            selected_columns = columns
        else:
            selected_columns = self.columns
        print(columns)
        print(quals)

        payload = {}
        for qual in quals:
            if qual.field_name == 'q':
                payload['q'] = qual.value
        print(payload)

        r = requests.get(self.backend_route, params=payload)
        print(r.json())

        for rank, result in enumerate(r.json()):
            row = {}
            if 'rank' in selected_columns:
                row['rank'] = rank+1
            if 'q' in selected_columns:
                row['q'] = qual.value
            
            for column in selected_columns:
                if column in result:
                    row[column] = result[column]
            yield row