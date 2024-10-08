// Работа с API
// https://api.openweathermap.org/data/2.5/weather?q=Москва&appid=23496c2a58b99648af590ee8a29c5348&units=metric&lang=ru

// У нас есть 3 варианта получения данных:
// 1. HMLHTTPRequest - старый метод (рассматривать не будем)
// 2. Fetch API - ES6 - 2015 Год
// 3. Async/Await - ES8 - 2017 год. Является расширением для Fetch API (Синтаксический сахар)
// fetch - это объект запроса
// promise - это обещание. Это то что мы получаем после выполнения fetch
// .then - который возвращает promis (обещание) - что мы будем делать дальше, когда данные придут
// .catch - если что-то пойдет не так

// Вставьте ваш API ключ в переменную apiKey
const apiKey = "23496c2a58b99648af590ee8a29c5348";

const units = "metric";
const lang = "ru";
const input = document.getElementById('input');
const formButton = document.getElementById('formButton');
const pResult= document.getElementById('result');



// Хорошо, давайте разберем весь процесс шаг за шагом простым языком:

// У нас есть функция getWeather(url), которая делает запрос к API погоды.

// Внутри этой функции мы используем fetch(url), который начинает асинхронный запрос к серверу.

// fetch(url) возвращает промис. Промис - это объект, который представляет будущий результат асинхронной операции.

// К этому промису мы добавляем .then(), где обрабатываем ответ от сервера. Здесь мы проверяем, успешен ли запрос, и преобразуем ответ в JSON.

// Вся эта цепочка (fetch и then) возвращается из функции getWeather(url).

// В обработчике клика на кнопку мы вызываем getWeather(url).

// Затем мы добавляем еще один .then() к результату getWeather(url). Этот .then() выполнится после всех предыдущих операций в цепочке.

// Когда мы вызываем этот последний .then(), JavaScript автоматически выполняет всю цепочку промисов: сначала делает запрос через fetch, затем обрабатывает ответ в первом .then() внутри getWeather, и только потом выполняет наш последний .then(), где мы обновляем текст на странице.

// Весь этот процесс происходит асинхронно. Это значит, что основной код продолжает выполняться, не ожидая завершения запроса к API.

// Если бы функция возвращала готовый объект вместо промиса, она стала бы синхронной и блокировала бы выполнение кода до получения данных.

// Такой подход позволяет эффективно работать с асинхронными операциями, сохраняя код чистым и понятным.

function getUrlByInput() {
    const cityName = input.value;
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${cityName}&appid=${apiKey}&units=${units}&lang=${lang}`;

    return url;
}

function getWeather(url) {
    // Выполняем асинхронный запрос на URL
    return fetch(url)
      // Тут могут выполняться параллельно другой JS
      .then((response) => {
        // response - объект ответа
        if (response.ok) {
          console.log("Получен успешный ответ");
          return response.json();
        } else {
          console.error("Ошибка при получении данных");
          throw new Error(`HTTP-код ошибки: ${response.status}`);
        }
      });
  }

formButton.addEventListener('click', (event) => {
    // Блокируем отправку формы
    event.preventDefault();
    
    const url = getUrlByInput();

    // Получаем ответ
    getWeather(url).then(data => {
        pResult.textContent = `Город: ${data.name}. Температура: ${data.main.temp}, ощущается как ${data.main.feels_like}`;
    })
});