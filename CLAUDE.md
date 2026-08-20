# Hannah Vogel personal site

Last verified: 2026-08-20

## Stack

Jekyll 4.4.1 on Ruby 4.0.6, with local SCSS and no client-side JavaScript.

## Commands

- `bundle exec jekyll serve` — local site at `http://127.0.0.1:4000/`
- `bundle exec jekyll build` — production-style static build
- `python3 -m unittest discover -s test -v` — repository contracts

## Structure

- `index.html` — the single-page academic profile
- `_config.yml` — canonical URL, identity, optional photo and plugins
- `_data/navigation.yml` — section navigation
- `_layouts/` and `_includes/` — shared semantic page structure
- `style.scss` — complete visual system and responsive behaviour
- `CONTENT-LICENSE.md` and `NOTICE.md` — content rights and provenance

## Conventions and boundaries

Read `AGENTS.md` before editing content. Keep profile claims tied to a named
source and review date. Keep `baseurl` empty because this site owns
`https://hvogel.org`. Treat `Gemfile.lock`, workflow action pins, licensing, and
the custom-domain setting as deliberate reproducibility boundaries.
