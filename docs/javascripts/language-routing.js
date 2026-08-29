(() => {
  const supported = new Set(["en", "fr", "ar", "es-419", "pt-br"]);
  const url = new URL(window.location.href);
  const requested = url.searchParams.get("lang")?.toLowerCase();
  const parts = url.pathname.split("/").filter(Boolean);

  // GitHub Pages paths are case-sensitive. Older pages and Material's URL
  // filter emitted the valid BCP 47 tag as /pt-BR/, while the published docs
  // directory is intentionally /pt-br/. Preserve old bookmarks and deep links.
  if (!requested && parts[0]?.toLowerCase() === "pt-br" && parts[0] !== "pt-br") {
    parts[0] = "pt-br";
    window.location.replace(`/${parts.join("/")}/${url.search}${url.hash}`);
    return;
  }

  if (!requested || !supported.has(requested)) return;

  if (supported.has(parts[0])) parts.shift();

  const targetPath = requested === "en"
    ? `/${parts.join("/")}`
    : `/${requested}/${parts.join("/")}`;

  url.searchParams.delete("lang");
  const remainingQuery = url.searchParams.toString();
  const normalizedPath = targetPath.endsWith("/") ? targetPath : `${targetPath}/`;
  const target = `${normalizedPath}${remainingQuery ? `?${remainingQuery}` : ""}${url.hash}`;

  if (`${url.pathname}${url.search}${url.hash}` !== target) {
    window.location.replace(target);
  }
})();
