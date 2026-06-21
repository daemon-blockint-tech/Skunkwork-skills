#!/usr/bin/env python3
"""
ontology_to_prompt_text.py

Helper script for Ontology-Augmented Generation skill.
Converts a simple JSON-based ontology definition into the compact hierarchical
text format recommended for prompt injection.

Usage:
    python scripts/ontology_to_prompt_text.py path/to/ontology.json

Expected input JSON structure (example):
{
  "name": "E-Commerce",
  "classes": [
    {
      "name": "Product",
      "properties": ["sku (string, unique)", "name (string)", "price (decimal > 0)", "category (enum: electronics, clothing)", "inStock (boolean)"]
    },
    ...
  ],
  "relations": [
    {"name": "places", "domain": "Customer", "range": "Order", "cardinality": "1:*"}
  ],
  "constraints": [
    "Order.totalAmount must equal sum over items of (quantity * unitPrice)"
  ],
  "examples": [
    "Order ORD-987 placed by CUST-1001 contains Product SKU-42"
  ]
}

Output is printed to stdout — copy into your prompt.
"""

import json
import sys
from pathlib import Path

def format_ontology(onto: dict) -> str:
    lines = []
    name = onto.get("name", "Domain Ontology")
    lines.append(f"## {name} (task-relevant subset)\n")

    if classes := onto.get("classes"):
        lines.append("Classes:")
        for cls in classes:
            cname = cls.get("name", "Unnamed")
            props = cls.get("properties", [])
            lines.append(f"- {cname}")
            for p in props:
                lines.append(f"    - {p}")
        lines.append("")

    if relations := onto.get("relations"):
        lines.append("Relations:")
        for rel in relations:
            rname = rel.get("name", "rel")
            dom = rel.get("domain", "?")
            rng = rel.get("range", "?")
            card = rel.get("cardinality", "")
            card_str = f" ({card})" if card else ""
            lines.append(f"- {rname}: {dom} → {rng}{card_str}")
        lines.append("")

    if constraints := onto.get("constraints"):
        lines.append("Key Constraints / Axioms:")
        for c in constraints:
            lines.append(f"- {c}")
        lines.append("")

    if examples := onto.get("examples"):
        lines.append("Grounded Examples:")
        for ex in examples:
            lines.append(f"- {ex}")
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/ontology_to_prompt_text.py <ontology.json>")
        print("\nExample ontology.json structure is documented in the docstring.")
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"Error: File not found: {path}")
        sys.exit(1)

    try:
        with open(path, "r", encoding="utf-8") as f:
            onto = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {path}: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    formatted = format_ontology(onto)
    print(formatted)


if __name__ == "__main__":
    main()
