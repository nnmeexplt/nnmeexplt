import base64
from pathlib import Path

template = Path("profile_template.svg").read_text(encoding="utf-8")
gif_b64 = base64.b64encode(Path("skull.gif").read_bytes()).decode("ascii")
output = template.replace("SKULL_DATA_URI", f"data:image/gif;base64,{gif_b64}")
Path("profile.svg").write_text(output, encoding="utf-8")
print(f"Wrote profile.svg ({len(output) / 1024:.0f} KB)")
