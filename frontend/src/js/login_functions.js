import autosize from "autosize";

export const no_resizable_textarea = () => {
  const MAX_WORDS = 50; // Define el número máximo de palabras permitido
  const textarea = document.querySelector("textarea");

  let autosizeScript = document.createElement("script");
  autosizeScript.src =
    "https://cdnjs.cloudflare.com/ajax/libs/autosize.js/4.0.2/autosize.min.js";
  document.head.appendChild(autosizeScript);

  autosizeScript.onload = function () {
    autosize(document.querySelector("textarea"));
  };

  textarea.addEventListener("input", () => {
    const words = textarea.value.trim().split(/\s+/); // Divide el contenido del textarea en palabras
    if (words.length > MAX_WORDS) {
      textarea.value = words.slice(0, MAX_WORDS).join(" "); // Si se supera el límite de palabras, se borra lo que se escriba extra
      textarea.blur(); // Desactiva la edición del textarea
    }
  });
};
