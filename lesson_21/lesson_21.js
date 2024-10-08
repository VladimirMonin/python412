// Вставьте ваш API ключ в переменную apiKey
const apiKey = "23496c2a58b99648af590ee8a29c5348";

const units = "metric";
const lang = "ru";
const input = document.getElementById("input");
const formButton = document.getElementById("formButton");
const pResult = document.getElementById("result");
const airPollutionDiv = document.getElementById("airPollution");
const forecastDiv = document.getElementById("forecastDiv");
const airPollutionDescriptionObj = {
    1: {
      description: "Отличное",
      bsClass: "alert-success",
    },
    2: {
      description: "Хорошее",
      bsClass: "alert-success",
    },
    3: {
      description: "Удовлетворительное",
      bsClass: "alert-warning",
    },
    4: {
      description: "Плохое",
      bsClass: "alert-danger",
    },
    5: {
      description: "Ужасное",
      bsClass: "alert-danger",
    },
  };
  

// http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
// Функция получает город из формы, формирует URL для запроса к GEOAPI, выполняет запрос, получает ответ, возвращает объект с данными о городе. lat lon ключи (создадим новый компактный объект)

async function getGeoByCityName() {
  const cityName = input.value;
  const url = `http://api.openweathermap.org/geo/1.0/direct?q=${cityName}&limit=1&appid=${apiKey}`;
  const response = await fetch(url);
  if (response.ok) {
    const data = await response.json();

    clearDana = {
      lat: data[0].lat,
      lon: data[0].lon,
    };

    return clearDana;
  } else {
    console.error("Ошибка при получении данных");
    throw new Error(`HTTP-код ошибки: ${response.status}`);
  }
}

// Функция будет формировать объект, где ключи будут названиями маршрутов
// а значения, адресами для запросов к API
// Текущая погода (принимает так же язык и систему измерения) - https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
// Прогноз на 5 дней (принимает так же язык и систему измерения) - api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
// Состояние воздуха (нет доп. аргументов) - http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API key}

function getUrlByInput(lat, lon) {
  let weatherUrlsObject = {
    currentWeather: `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${apiKey}&units=${units}&lang=${lang}`,
    forecastWeather: `https://api.openweathermap.org/data/2.5/forecast?lat=${lat}&lon=${lon}&appid=${apiKey}&units=${units}&lang=${lang}`,
    airPollution: `http://api.openweathermap.org/data/2.5/air_pollution?lat=${lat}&lon=${lon}&appid=${apiKey}`,
  };
  return weatherUrlsObject;
}

async function getWeather(url) {
  const response = await fetch(url);
  if (response.ok) {
    console.log("Получен успешный ответ от URL: " + url);
    return await response.json();
  } else {
    console.error("Ошибка при получении данных от URL: " + url);
    throw new Error(`HTTP-код ошибки: ${response.status}`);
  }
}

formButton.addEventListener("click", async (event) => {
  event.preventDefault();
  let geoData = await getGeoByCityName();
  console.log(geoData);
  let urlsObject = getUrlByInput(geoData.lat, geoData.lon);
  console.log(urlsObject);

  // Получаем данные о погоде (вариант по очереди)
  // let currentWeather = await getWeather(urlsObject.currentWeather);
  // console.log(currentWeather);
  // let forecastWeather = await getWeather(urlsObject.forecastWeather);
  // console.log(forecastWeather);
  // let airPollution = await getWeather(urlsObject.airPollution);
  // console.log(airPollution);

  // Получаем данные о погоде (вариант параллельно)
  let weatherData = await Promise.all([
    getWeather(urlsObject.currentWeather),
    getWeather(urlsObject.forecastWeather),
    getWeather(urlsObject.airPollution),
  ]);
  // weatherData - массив из из объектов с данными о погоде
  // В том же порядке как и вызовы

  let resultWeatherData = {
    currentWeather: weatherData[0],
    forecastWeather: weatherData[1],
    airPollution: weatherData[2],
  };

  console.log(resultWeatherData);

  // Состояние воздуха
  displayAirPollution(resultWeatherData.airPollution);
});

// list.main.aqi - Где лежит цифра с качеством воздуха?
// Оценивается от 1 до 5, где 1 - лучшее, 5 - хуже

// Функция которая принимает объект с состоянием воздуха, и опираясь на airPollutionDescriptionObj в airPollution меняет классы и текст

function displayAirPollution(airPollution) {
  const airPollutionDescription = airPollutionDescriptionObj[airPollution.list[0].main.aqi];
//  Проверяем сколько классов на элемнете airPollution
  const airPollutionClasses = airPollutionDiv.classList;
  // Если классов больше 1, то удаляем последний
  if (airPollutionClasses.length > 1) {
    airPollutionDiv.classList.remove(airPollutionClasses[airPollutionClasses.length - 1]);
  }
  // Добавляем классы
  airPollutionDiv.classList.add(airPollutionDescription.bsClass);
  // Добавляем текст
  airPollutionDiv.textContent = airPollutionDescription.description;
}

// Функция которая в forecastDiv в конец добавляет наследника table и рисует BS5 таблицу с прогнозом погоды
//

// "list": [
//     {
//       "dt": 1661871600,
//       "main": {
//         "temp": 296.76,
//         "feels_like": 296.98,
//         "temp_min": 296.76,
//         "temp_max": 297.87,
//         "pressure": 1015,
//         "sea_level": 1015,
//         "grnd_level": 933,
//         "humidity": 69,
//         "temp_kf": -1.11
//       },
//       "weather": [
//         {
//           "id": 500,
//           "main": "Rain",
//           "description": "light rain",
//           "icon": "10d"
//         }
//       ],