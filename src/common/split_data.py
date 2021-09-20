def split_data(data, file):
    data = data.split('\n')

    for i, d in enumerate(data):
        data[i] = data[i].split(',')

        if data[i] == ['']:
            continue

        if len(data[i]) != 2:
            file.append_error(f'Wystąpił błąd w linijce {i}\n', close=True)

    data = list(filter(lambda x: x != [''], data))  # remove empty elements

    return data
