(() => {
  const supported = new Set(["en", "fr", "ar", "es-419", "pt-br"]);
  const url = new URL(window.location.href);
  const requested = url.searchParams.get("lang")?.toLowerCase();

  if (!requested || !supported.has(requested)) return;

  const parts = url.pathname.split("/").filter(Boolean);
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
