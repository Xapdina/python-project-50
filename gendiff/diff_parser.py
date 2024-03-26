def diff_parser(data1, data2):
    diff = {}

    keys1 = set(data1)
    keys2 = set(data2)

    all_keys = keys1 | keys2
    added = keys2 - keys1
    deleted = keys1 - keys2

    for key in sorted(all_keys):
        if key in added:
            diff[key] = {'status': 'added', 'value': data2.get(key)}
        elif key in deleted:
            diff[key] = {'status': 'deleted', 'value': data1.get(key)}
        elif data1.get(key) == data2.get(key):
            diff[key] = {'status': 'unchanged', 'value': data1.get(key)}
        elif isinstance(data1.get(key), dict) and isinstance(data2.get(key), dict):
            diff[key] = {'status': 'nested', 'value': diff_parser(data1.get(key), data2.get(key))}
        else:
            diff[key] = {'status': 'updated', 'value': [data1.get(key), data2.get(key)]}
    return diff
