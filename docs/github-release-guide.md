---
layout: page
title: GitHub Release Guide
---

This archive is prepared so the repository can be published publicly and the website can be deployed from `docs/`.

## Before First Release

1. Update `CITATION.cff` with the author name, repository URL, and release date.
2. Decide whether `LICENSE` should remain all-rights-reserved or be replaced with a reuse license.
3. Create a public GitHub repository, for example `ddf-public-archive`.
4. Push the contents of this folder to that repository.
5. In GitHub repository settings, enable Pages with GitHub Actions as the build and deployment source.
6. Create a versioned release once the first public archive is ready.
7. Connect the GitHub repository to Zenodo if a DOI is required.

## Notes

The website is intentionally a public front door. The full research record remains in the repository folders `notes/`, `papers/`, `raw/`, and `archive/`.
