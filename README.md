# Duidi Wu — academic homepage

Buildless static website for GitHub Pages. Open index.html to preview. No dependencies or tracking scripts.

## Publish

Create a GitHub repository named `Duidi-WU.github.io` under the matching GitHub account. Upload index.html, style.css, images, and .nojekyll to its root. In Settings → Pages choose Deploy from a branch → main → /(root). The URL depends on your actual GitHub username.

## Edit

Edit build.py for biography, news and publication records; run `python build.py` to regenerate index.html and publications.json. CSS is in style.css. Existing supplied images are preserved. Missing graphical abstracts are explicitly marked; replace them by adding an image and setting its filename prefix in build.py. Verified project links are included only when available. “Find paper” links are title searches, not verified publisher URLs.

## Content review

CV provides education dates but does not confirm degree conferral or a current appointment; neither is claimed. Confirm current title and affiliation before publishing. Authors abbreviated in the CV remain abbreviated. The supplied Google Scholar text attachment was empty at time of reading; complete Scholar reconciliation is pending. News dates follow the CV, including the December 2025 Shanghai Outstanding Graduate entry; confirm that date. Original CV is not publicly bundled because it contains personal details.

References for layout: https://alvinwen428.github.io/ , https://www.polyu.edu.hk/me/david/ , https://tairanhe.com/ , https://dongjaelee95.github.io/ , https://xiaofeng-guo.github.io/ . Reimplemented with original HTML/CSS; no third-party tracking IDs copied.

Update: The complete user-supplied Google Scholar list is now included (27 entries), including a separately labelled SSRN preprint without an invented year. Source records are in scholar-publications.json. Publication years follow the supplied Scholar list. Citation counts are omitted because they change over time. The website now uses a monochrome palette and a compact image/text grid at desktop and mobile sizes. Missing abstracts are labelled. Current title, degree conferral and award dates still need owner review before publication.
