def find_header_row(data):
    for i, row in enumerate(data):
        if "ID" in row and "Дата" in row:
            return i
    return None



def normalize_data(raw_data):
    print("NORMALIZE STARTED")
    header_index = None

    for i, row in enumerate(raw_data):
        joined = " ".join(row)
        if "ID" in joined and "Дата" in joined:
            header_index = i
            break

    if header_index is None:
        print("HEADER NOT FOUND")
        return []

    headers = raw_data[header_index]
    rows = raw_data[header_index + 1:]

    result = []

    for row in rows:
        if not any(row):
            continue

        item = dict(zip(headers, row))

        try:
            amount = float(item.get("Приход") or 0)
        except:
            amount = 0

        result.append({
            "order_id": (item.get("ID") or "").strip(),
            "date": (item.get("Дата") or "").strip(),
            "payment_type": (item.get("Способ оплаты") or "").strip(),
            "amount": amount
        })

    return result