oidAsString = "10"
all_rows = [
    ("first row 1", "first row 2", "first row 3", "first row 4", ),
    ("second row 1", "second row 2", "second row 3", "second row 4", ),
    ("third row 1", "third row 2", "third row 3", "third row 4", )
    ]
fetched_row = all_rows[1]
choice = ("foo", "bar", "baz")
formattedUpdateQuery = "update transactions set category1='bar', category2='baz' where oid=10"


