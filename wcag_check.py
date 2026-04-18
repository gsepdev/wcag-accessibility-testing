import json

WCAG_MAPPING = {
    "image-alt": ("1.1.1 Non-text Content", "A"),
    "label": ("3.3.2 Labels or Instructions", "A"),
    "button-name": ("4.1.2 Name, Role, Value", "A"),
    "color-contrast": ("1.4.3 Contrast (Minimum)", "AA"),
    "link-name": ("2.4.4 Link Purpose", "A"),
}

with open("report.json", "r", encoding="utf-8") as f:
    data = json.load(f)

audits = data["audits"]

print("\nWCAG Compliance Report\n")

for key, value in audits.items():
    if key in WCAG_MAPPING and value["score"] == 0:
        wcag, level = WCAG_MAPPING[key]
        print(f"\n❌ {key} -> {wcag} -> Level {level}")

        details = value.get("details", {})
        items = details.get("items", [])

        for item in items:
            node = item.get("node", {})
            snippet = node.get("snippet", "No snippet")
            selector = node.get("selector", "No selector")
            text = node.get("nodeLabel", "No text")

            print(f"   🔎 Element: {snippet}")
            print(f"      Selector: {selector}")
            print(f"      Text: {text}")