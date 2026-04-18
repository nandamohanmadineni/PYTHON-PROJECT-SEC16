# utils/validators.py

class InvalidInputError(Exception):
    pass

class FileCorruptionError(Exception):
    pass

def validate_marks(marks):
    if not isinstance(marks, list):
        raise InvalidInputError("Marks must be a list")

    for m in marks:
        if not (0 <= m <= 100):
            raise InvalidInputError(f"Invalid mark: {m}")

    return True


def validate_attendance(att):
    if not (0 <= att <= 100):
        raise InvalidInputError("Attendance must be between 0 and 100")
    return True


def safe_file_read(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except:
        raise FileCorruptionError("File cannot be read or is corrupted")