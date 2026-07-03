/* Injects the shared nav and footer into every page.
   Each page includes <div id="nav-include"></div> and
   <div id="footer-include"></div>, plus this script. */
(function () {
  function inject(id, url) {
    var el = document.getElementById(id);
    if (!el) return;
    fetch(url)
      .then(function (r) { return r.text(); })
      .then(function (html) {
        el.outerHTML = html;
      })
      .catch(function (e) {
        console.error("Failed to load " + url, e);
      });
  }

  function run() {
    inject("nav-include", "/nav.html");
    inject("footer-include", "/footer.html");
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", run);
  } else {
    run();
  }
})();
