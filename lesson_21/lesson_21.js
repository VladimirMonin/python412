// Вставьте ваш API ключ в переменную apiKey
const apiKey = "23496c2a58b99648af590ee8a29c5348";

const units = "metric";
const lang = "ru";
const input = document.getElementById('input');
const formButton = document.getElementById('formButton');
const pResult= document.getElementById('result');


function getUrlByInput() {
    const cityName = input.value;
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${cityName}&appid=${apiKey}&units=${units}&lang=${lang}`;

    return url;
}


async function getWeather(url) {
    const response = await fetch(url);
    if (response.ok) {
        console.log("Получен успешный ответ");
        return await response.json();
    } else {
        console.error("Ошибка при получении данных");
        throw new Error(`HTTP-код ошибки: ${response.status}`);
    }
}

formButton.addEventListener('click', async (event) => {
    event.preventDefault();
    const url = getUrlByInput();
    try {
        const data = await getWeather(url);
        pResult.textContent = `Город: ${data.name}. Температура: ${data.main.temp}, ощущается как ${data.main.feels_like}`;
    } catch (error) {
        console.error("Произошла ошибка:", error);
    }
});