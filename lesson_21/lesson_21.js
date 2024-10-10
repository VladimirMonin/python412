// Вставьте ваш API ключ в переменную apiKey
const apiKey = "23496c2a58b99648af590ee8a29c5348";

const units = "metric";
const lang = "ru";
const input = document.getElementById("input");
const formButton = document.getElementById("formButton");
const airPollutionDiv = document.getElementById("airPollution");
const forecastDiv = document.getElementById("forecastDiv");
const currentWeatherDiv = document.getElementById("currentWeather");

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
  

async function getGeoByCityName(cityName) {
  const url = `http://api.openweathermap.org/geo/1.0/direct?q=${cityName}&limit=1&appid=${apiKey}`;
  const response = await fetch(url);
  if (response.ok) {
    const data = await response.json();


    // Проверка на пустой массив. И Alert
    if (data.length === 0) {
      showModal("Город не найден");
      throw new Error("Город не найден");
    }

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
  const cityName = input.value;
  localStorage.setItem("cityName", cityName);
  displayAllWeather(cityName);
});

// Добавим листнер на документ, чтобы по загрузке страницы проверяли наличие города в localStorage и если он там есть, он ставился бы в value инпута и вызывался бы метод displayAllWeather по этому городу

document.addEventListener("DOMContentLoaded", () => {
  const cityName = localStorage.getItem("cityName");
  if (cityName) {
    input.value = cityName;
    displayAllWeather(cityName);}

  })

async function displayAllWeather(cityName) {
  let geoData = await getGeoByCityName(cityName);
  console.log(geoData);
  let urlsObject = getUrlByInput(geoData.lat, geoData.lon);
  console.log(urlsObject);

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
  // Текущая погода
  displayCurrentWeather(resultWeatherData.currentWeather);
  // Прогноз на 5 дней
  displayForecastWeather(resultWeatherData.forecastWeather);
}


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

function getIconUrl(iconCode, size) {
  if (size === undefined) {
    size = "";
  }
  else if (size === "4x") {
    size = "@4x";
  }
  else if (size === "2x") {
    size = "@2x";
  }
  else {
    throw new Error("Неизвестный размер");
  }

  return `https://openweathermap.org/img/wn/${iconCode}${size}.png`;
}

function displayCurrentWeather(currentWeather){
  const cityName = currentWeather.name;
  const iconID = currentWeather.weather[0].icon;
  const iconUrl = getIconUrl(iconID, "4x");
  const temp = currentWeather.main.temp;
  const feelsLike = currentWeather.main.feels_like;
  const windSpeed = currentWeather.wind.speed;

  //  Первый параграф
  firstP = document.createElement("p");
  iconImg = document.createElement("img");
  iconImg.src = iconUrl;
  console.log(iconImg);
  firstP.appendChild(iconImg);
  textContentFirstP = `Город: ${cityName}`;
  firstP.innerHTML += textContentFirstP;
  currentWeatherDiv.appendChild(firstP);

  // Второй параграф (второй способ))
  secontPContent = `<p>Температура: ${temp}, ощущается как ${feelsLike}, ветер: ${windSpeed}</p>`;

  currentWeatherDiv.innerHTML += secontPContent;
}

function displayForecastWeather(forecastWeather) {

  // Создаем элементы
  const table = document.createElement("table");
  // Добавляем классы table table-striped table-hover
  table.classList.add("table", "table-striped", "table-hover");
  
  // Первая строка
  const firstRow = "<tr><th>Дата</th><th>Иконка</th><th>Температура</th><th>Ветер</th></tr>";
  table.innerHTML = firstRow;

  // Объявляем цикл который перебирает массив forecastWeather.list
  // и создает строки таблицы

  for (let weatherObj of forecastWeather.list) {
    // Получаем данные из очередного объекта
      
    const dateTime = weatherObj.dt_txt; // "2022-08-30 15:00:00"
    const date = dateTime.split(" ")[0]; // "2022-08-30"
    const time = dateTime.split(" ")[1].split(":")[0] + "ч."; // "15ч."
    const finalDateTime = date + " " + time;
    const idIcon = weatherObj.weather[0].icon;
    const iconUrl = getIconUrl(idIcon);
    const temp = weatherObj.main.temp;
    const windSpeed = weatherObj.wind.speed;

    // Создаем строку таблицы
    const row = `<tr><td>${finalDateTime}</td><td><img src="${iconUrl}" alt="Иконка погоды"></td><td>${temp}</td><td>${windSpeed}</td></tr>`;

    // Добавляем строку в таблицу
    table.innerHTML += row;
  }
  // Добавляем таблицу в forecastDiv
  forecastDiv.appendChild(table);
}

function showModal(message) {
  const modalHtml = `
    <div class="modal fade" id="errorModal" tabindex="-1" aria-labelledby="errorModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="errorModalLabel">Ошибка</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            ${message}
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
          </div>
        </div>
      </div>
    </div>
  `;

  document.body.insertAdjacentHTML('beforeend', modalHtml);
  const modal = new bootstrap.Modal(document.getElementById('errorModal'));
  modal.show();

  document.getElementById('errorModal').addEventListener('hidden.bs.modal', function () {
    this.remove();
  });
}