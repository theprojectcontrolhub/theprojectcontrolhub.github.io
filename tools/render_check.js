// Executes a page in a real DOM and reports JS errors and rendered row counts.
// check_site.py does not run JavaScript; this catches what it cannot.
//   npm install jsdom && node tools/render_check.js . learn.html
const { JSDOM } = require('jsdom');
const fs = require('fs'), path = require('path');
const dir = process.argv[2], page = process.argv[3];
let html = fs.readFileSync(path.join(dir, page), 'utf8');
const cur = fs.readFileSync(path.join(dir, 'curriculum.js'), 'utf8');
// inline curriculum.js where the real tag is; drop the auth ES module
html = html.replace(/<script src="curriculum\.js\?v=\d+"><\/script>/, '<script>\n' + cur + '\n</script>');
html = html.replace(/<script type="module">[\s\S]*?<\/script>/g, '');
html = html.replace(/<script src="auth\.js"[^>]*><\/script>/g, '');
const errors = [];
const dom = new JSDOM(html, {
  runScripts: 'dangerously',
  beforeParse(w) { w.addEventListener('error', e => errors.push(e.message)); }
});
const d = dom.window.document;
d.dispatchEvent(new dom.window.Event('DOMContentLoaded', { bubbles: true }));
console.log('--- ' + page + ' ---');
console.log('  js hatasi: ' + (errors.length ? errors.join(' | ') : 'yok'));
d.querySelectorAll('.module-weeks').forEach(el => {
  console.log('  ' + (el.id || '?').padEnd(16) + el.querySelectorAll('.week-item').length + ' satir');
});
d.querySelectorAll('.module-badge, .module-status, .track-badge').forEach(el => {
  const t = el.textContent.trim().replace(/\s+/g, ' ');
  if (el.id) console.log('  ' + el.id.padEnd(18) + t);
});
