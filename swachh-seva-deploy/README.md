# Swachh Vatika (Swachh-Seva project folder)

Stack (locked by SRS): HTML5 + CSS3 + Vanilla JS -> Flask -> SQLite (sqlite3) + Groq API (server-side only).

**Status:** skeleton. `templates/index.html` is your original prototype, unchanged. Every `.py`, `.js` and `.sql` file is intentionally blank until coded.
The HTML pages under `templates/` extend `templates/base.html` and reuse the design system extracted from `index.html` into `static/css/`.

Note: `index.html` contains `{{ }}` / `{% %}` style text inside its JavaScript, so serve it with `send_from_directory`, not `render_template`.

Page naming: kebab-case (SRS Chunk 4). One JS file per page under `static/js/<role>/`, shared code in `static/js/core/`.

**Update:** `templates/index.html` (and `static-preview/index.html`) is now the new single-page prototype (index 2), linked to the full module pages via a "Full module pages" row at the bottom. Brand renamed to SWACHH VATIKA. A responsive layer for phones, tablets, laptops and large screens was added to `static/css/responsive.css` and the inline index styles.
