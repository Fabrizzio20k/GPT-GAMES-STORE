export const changeSearchParams = (categoria, elemento) => {
  let url = new URL(window.location);
  url.searchParams.set(categoria, elemento);

  url.search = url.searchParams;
  url = url.toString();

  history.pushState({}, null, url);
};
