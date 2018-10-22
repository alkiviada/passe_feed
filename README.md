# Passe Feed

This a simple feed of letters and diaries written by excellent writers of such. The list of 'contributors' includes Carlyle and his wife, Byron, Dorothy Wordsworth, Swift, Asa Gray, Pepys, Cicero.
It can be enjoyed freely and publicly at: https://xl72sfeq0f.execute-api.us-east-1.amazonaws.com/passe_aws/

## Getting Started

This is a very small and simple Django app with data residing in PostgreSQL and served by the Django REST framework, and rendered by a React/Redux-based frontend
The epubs of the data were downloaded from the Project Gutenberg resource, parsed using Python's Beautiful Soup module, polulated thru a Django standalone script, and now this data is being served in a random fashion on a page with an infinite scroll capability  


