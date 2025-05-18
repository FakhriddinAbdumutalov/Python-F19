def write_file(file_path, content):
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    except IOError as e:
        raise IOError(f"Unable to write to {file_path}: {e}")
