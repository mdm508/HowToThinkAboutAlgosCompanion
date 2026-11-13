"""Check the Python actually embedded in the student lesson, without duplication."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import xml.etree.ElementTree as ET

root = ET.parse(Path(__file__).resolve().parents[1] / "source/lesson-01-maximum.ptx")
code = root.find(".//program/code").text
namespace = {}
output = StringIO()
with redirect_stdout(output):
    exec(compile(code, "lesson-01-maximum.ptx", "exec"), namespace)
assert output.getvalue().splitlines() == [
    "checkpoint: 1 6", "checkpoint: 2 6", "checkpoint: 3 9",
    "checkpoint: 4 9", "maximum: 9",
]
maximum = namespace["maximum"]
for values in ([7], [-8, -3, -5], [9, 9, 2], [1, 2, 3], [3, 2, 1]):
    original = values.copy()
    with redirect_stdout(StringIO()):
        result = maximum(values)
    assert result == max(values), values
    assert values == original, "The input must remain unchanged"
try:
    maximum([])
except ValueError:
    pass
else:
    raise AssertionError("Empty input must be rejected")
print("Lesson code: checkpoint trace, edge cases, input preservation and empty-input contract passed.")
