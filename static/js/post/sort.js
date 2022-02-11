const params = new URL(location.href).searchParams;
const value = params.get("sort")
const element = document.querySelector(`option[value=${value}`);
element.selected = true;
