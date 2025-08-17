from dataclasses import dataclass
from typing import List, Optional


@dataclass
class SourceDoc:
page_content: str
source: Optional[str] = None
metadata: Optional[dict] = None