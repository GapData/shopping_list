def get_db_list(db):
    """Create a list from a comma-separated string. Empty string returns empty list."""
    if not db:
        return []
    else:
        return db.split(',')

def clean_db(item):
    """Return item as list, with whitespace stripped"""
    lyst = []
    items = item.split(',')
    for item in items:
        lyst.append(item.strip())

    return ','.join(map(str, lyst))

def create(item, db):
  """Add item to data holding string."""
  lyst = get_db_list(db)
  item = clean_db(item)
  lyst.append(item)
  return ','.join(map(str, lyst))


def get_items(db):
    """Get items. db is a string containing comma-separated values"""
    return get_db_list(db)

def remove_item(item, db):
    """Remove item from data string if it exists. Return new data string."""
    lyst = get_db_list(db)
    if item in lyst:
        lyst.remove(item)
    return ','.join(map(str, lyst))
