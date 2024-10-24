let personObj = {
  name: "Марго",
  age: 20,
  hobby: "html",
  isMarried: false,
  creditHistory: null,
  getInfo() {
    console.log(`${this.name}, ${this.age}`);
  },
};

// Как нам преобразовать объект в строку JSON?
let personObjectJSON = JSON.stringify(personObj);

// Консоль лог
console.log(personObj);
console.log(personObjectJSON);

// Преобразуем обратно из JSON в объект
let personObjectFromJSON = JSON.parse(personObjectJSON);

function getInfo() {
  console.log(`Имя ${this.name}, ${this.age} лет`);
}

// Вложим функцию в полученный объект из JSON
personObjectFromJSON.getInfo = getInfo;

personObjectFromJSON.getInfo();

// ID параграфа
const pResult = document.getElementById("result");

let WeatherObject = {
  coord: { lon: 37.6156, lat: 55.7522 },
  weather: [{ id: 800, main: "Clear", description: "ясно", icon: "01n" }],
  base: "stations",
  main: {
    temp: 15.89,
    feels_like: 14.97,
    temp_min: 13.94,
    temp_max: 16.88,
    pressure: 1021,
    humidity: 55,
    sea_level: 1021,
    grnd_level: 1002,
  },
  visibility: 10000,
  wind: { speed: 4.42, deg: 73, gust: 11.8 },
  clouds: { all: 0 },
  dt: 1727796817,
  sys: {
    type: 2,
    id: 2095214,
    country: "RU",
    sunrise: 1727753558,
    sunset: 1727795128,
  },
  timezone: 10800,
  id: 524901,
  name: "Москва",
  cod: 200,
};


// Функция которая возьмет погодный объект и выдаст очищенный погодный объект
// температура main.temp
// ощущаемая температура main.feels_like
// сила ветра wind.speed


// function getClearWeatherObject(weatherObj) {
//     let clearWeather = {};
    
//     clearWeather.temperature = weatherObj.main.temp;
//     clearWeather.feelTemperature = weatherObj.main.feels_like;
//     clearWeather.windSpeed = weatherObj.wind.speed;
//     clearWeather.name= weatherObj.name;
//     clearWeather.getWeatherInfo = getWeatherInfo;
//     clearWeather.displayWeather = displayWeather;
//     return clearWeather;
// }

// function getWeatherInfo() {
//     return `Город: ${this.name}. Температура: ${this.temperature}, ощущаемая температура: ${this.feelTemperature}, сила ветра: ${this.windSpeed}`;
// }

// function displayWeather() {
//     pResult.textContent = this.getWeatherInfo();
// }

function getClearWeatherObject(weatherObj) {
  let clearWeather = {
      temperature: weatherObj.main.temp,
      feelTemperature: weatherObj.main.feels_like,
      windSpeed: weatherObj.wind.speed,
      name: weatherObj.name,
      
      getWeatherInfo: function() {
          return `Город: ${this.name}. Температура: ${this.temperature}, ощущаемая температура: ${this.feelTemperature}, сила ветра: ${this.windSpeed}`;
      },
      
      displayWeather: function() {
          pResult.textContent = this.getWeatherInfo();
      }
  };
  
  return clearWeather;
}


let clearWeather = getClearWeatherObject(WeatherObject);
clearWeather.displayWeather();
console.log(clearWeather.getWeatherInfo());