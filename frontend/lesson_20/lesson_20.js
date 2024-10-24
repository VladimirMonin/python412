const input = document.querySelector("#input");
const formButton = document.querySelector("#formButton");
const localP = document.querySelector("#localP");

// Листнер по клику на кнопку формы, записывает данные в хранилище браузера
formButton.addEventListener("click", function (event) {
  // Препятствуем отправке формы
  event.preventDefault();
  const inputValue = input.value;
  localP.textContent = inputValue;
  sessionStorage.setItem("inputValue", inputValue);
});

// Листнер по загрузке документа, проверяет есть ли в хранилище данные inputValue
// если есть, поместит в параграф localP

document.addEventListener("DOMContentLoaded", function () {
  const inputValue = sessionStorage.getItem("inputValue");
  if (inputValue) {
    localP.textContent = inputValue;
  }
});
