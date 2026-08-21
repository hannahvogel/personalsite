# Working with AI in this repository

Last verified: 2026-08-21

Before asking an AI to change the site, write down:

1. the visitor and outcome the change is for;
2. the source material the change may rely on;
3. the smallest useful change; and
4. the check that would show whether it worked.

Read the relevant files before editing. The Macquarie University profile is a
factual source, not reusable copy: independently word prose and link to the
record. Ask Hannah when intent, attribution, preferred wording, or permission is
unclear. Do not invent claims, citations, honours, contributor identities,
image descriptions, permissions, or verification results.

Keep code, original prose, photographs, and third-party material within their
separate licences. A supplied photograph needs Hannah's approved alternative
text and a documented credit or rights statement before publication.

Preserve the site's low cognitive load and accessibility: semantic HTML,
descriptive links, logical headings, keyboard-visible focus, sufficient colour
contrast, and no information conveyed by colour alone.

After a change, run:

```text
bundle exec jekyll build
```

Report exactly what the build checked. Lighthouse is a separate,
non-blocking GitHub workflow; a red score still needs investigation.
