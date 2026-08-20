from html.parser import HTMLParser
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class TemplateParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tags: list[tuple[str, dict[str, str | None]]] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        self.tags.append((tag, dict(attrs)))


def parse_template(path: Path) -> TemplateParser:
    parser = TemplateParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


class AccessibilityContractTest(unittest.TestCase):
    def test_layout_has_skip_link_and_named_main_landmark(self) -> None:
        parser = parse_template(ROOT / "_layouts" / "default.html")

        skip_links = [
            attrs
            for tag, attrs in parser.tags
            if tag == "a"
            and "skip-link" in (attrs.get("class") or "").split()
            and attrs.get("href") == "#content"
        ]
        main_landmarks = [
            attrs
            for tag, attrs in parser.tags
            if tag == "main"
            and attrs.get("id") == "content"
            and attrs.get("aria-label")
        ]

        self.assertEqual(len(skip_links), 1, "expected one skip link to #content")
        self.assertEqual(
            len(main_landmarks), 1, "expected one identified and named main landmark"
        )

    def test_navigation_is_named(self) -> None:
        parser = parse_template(ROOT / "_includes" / "navigation.html")
        named_navigation = [
            attrs
            for tag, attrs in parser.tags
            if tag == "nav" and attrs.get("aria-label") == "Primary"
        ]

        self.assertEqual(
            len(named_navigation), 1, "expected one Primary navigation landmark"
        )

    def test_styles_provide_skip_link_and_visible_keyboard_focus(self) -> None:
        stylesheet = (ROOT / "style.scss").read_text(encoding="utf-8")

        self.assertIn(".skip-link", stylesheet)
        self.assertIn(":focus-visible", stylesheet)


if __name__ == "__main__":
    unittest.main()
