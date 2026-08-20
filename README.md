# Hannah Vogel personal site

This repository builds Hannah Vogel's academic homepage at <https://hvogel.org>.
It is a clean-history adaptation of the MIT-licensed
[Academic Jekyll](https://github.com/vsimkus/academic-jekyll) template.

The first content edition is independently worded from facts in Hannah's public
[Macquarie University researcher profile](https://researchers.mq.edu.au/en/persons/hannah-vogel/),
reviewed on 20 August 2026. See `CONTENT-LICENSE.md` and `NOTICE.md` for content
rights and template provenance.

## Work locally

The repository pins Ruby 4.0.6 in `.ruby-version`. With rbenv, install it once
with `rbenv install 4.0.6`; rbenv will select it automatically here. Then run:

```text
bundle install
bundle exec jekyll serve
```

Before pushing, run:

```text
bundle exec jekyll build
python3 -m unittest discover -s test -v
```

The separate `Lighthouse` workflow audits pull requests and pushes against the
100/100/100/100 baseline shipped for accessibility, best practices, performance,
and SEO. It can turn red without interrupting the independent Pages deployment,
and it preserves the HTML report as a workflow artifact.

## Add Hannah's photograph

Place the approved image in the repository, set `photo` and `photo_alt` in
`_config.yml`, and record its credit and rights in `CONTENT-LICENSE.md`. Until
then, the layout deliberately renders without a placeholder portrait.

GitHub Actions builds and deploys `main`; the custom domain is configured in the
repository's Pages settings rather than through a generated `CNAME` file.
