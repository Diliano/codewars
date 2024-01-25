def number(lines):
    formatted_lines = []

    # use enumerate to access the index and value of each iteration
    for index, value in enumerate(lines):
        # as zero-indexed, format lines using index + 1 to meet expected numbering
        formatted_lines.append(f"{index + 1}: {value}")

    return formatted_lines