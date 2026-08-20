from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class SiteContractTest(unittest.TestCase):
    def test_config_names_the_canonical_personal_site(self) -> None:
        config = (ROOT / "_config.yml").read_text(encoding="utf-8")

        self.assertIn('name: "Hannah Vogel"', config)
        self.assertIn('url: "https://hvogel.org"', config)
        self.assertIn('baseurl: ""', config)
        self.assertIn("repository: hannahvogel/personalsite", config)
        self.assertIn("lang: en-AU", config)

    def test_homepage_has_named_sections_and_source_profiles(self) -> None:
        homepage = (ROOT / "index.html").read_text(encoding="utf-8")

        for section_id in (
            "about",
            "research",
            "teaching",
            "publications",
            "recognition",
            "contact",
        ):
            self.assertIn(f'id="{section_id}"', homepage)
        self.assertIn("https://orcid.org/0000-0001-6655-1604", homepage)
        self.assertIn("https://researchers.mq.edu.au/en/persons/hannah-vogel/", homepage)
        self.assertNotIn("John Doe", homepage)
        self.assertNotIn("Lorem ipsum", homepage)

    def test_licensing_and_ai_guidance_are_explicit(self) -> None:
        content_license = (ROOT / "CONTENT-LICENSE.md").read_text(encoding="utf-8")
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        claude = (ROOT / "CLAUDE.md").read_text(encoding="utf-8")

        self.assertIn("CC BY 4.0", content_license)
        self.assertIn("Macquarie University researcher profile", content_license)
        self.assertIn("Before asking an AI", agents)
        self.assertIn("Last verified: 2026-08-20", claude)


if __name__ == "__main__":
    unittest.main()
