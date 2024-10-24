// Lesson 12 - Switch - case
// Методы массивов
// Объекты, итерация по объектам

// Конструкция switch - case - на примере нажатия стрелок
// Если убрать брейки, и мы попадаем в один из блоков, выполнятся будут ВСЕ ниже идущие
// Если брейки оставить, то выполнится только первый, даже если будет ТАКОЙ же кейс ниже
// default - условный ELSE - заглядываем если ни один не выполнился
let userButton = "up";

switch (userButton) {
  case "up":
    console.log("Вверх");
    break;
  case "down":
    console.log("Вниз");
    break;
  case "left":
    console.log("Влево");
    break;
  case "right":
    console.log("Вправо");
    break;
  case "up":
    console.log("Вверх 2");
    break;

  default:
    console.log("Неизвестная команда");
}

// Методы массивов ///////////////////////////
//push - добавляет элемент в конец массива
//shift - Добавляет
// pop - удаляет элемент с конца массива
// unshift - удаляет
// forEach(callback) — Выполняет указанную функцию для каждого элемента массива. Ничего не возвращает.
// map(callback) — Создает новый массив, состоящий из результатов вызова функции для каждого элемента.
// filter(callback) — Создает новый массив с элементами, прошедшими проверку, заданную в функции.
// reduce(callback, initialValue) — Применяет функцию к аккумулятору и каждому элементу массива (слева направо), сводя массив к единственному значению.
// find(callback) — Возвращает первый элемент массива, который удовлетворяет условию, заданному в функции.
// findIndex(callback) — Возвращает индекс первого элемента, который удовлетворяет условию, заданному в функции.
// some(callback) — Проверяет, удовлетворяет ли хотя бы один элемент массива условию, заданному в функции.
// every(callback) — Проверяет, удовлетворяют ли все элементы массива условию, заданному в функции.
// sort(compareFunction) — Сортирует элементы массива на месте и возвращает отсортированный массив.
// reverse() — Изменяет порядок элементов в массиве на обратный.
// concat(value) — Объединяет два или более массива, возвращая новый массив.
// slice(start, end) — Возвращает новый массив, содержащий копию части исходного массива от start до end (не включая end).
// splice(start, deleteCount, item1, item2, ...) — Изменяет содержимое массива, удаляя существующие элементы и/или добавляя новые.
// indexOf(searchElement) — Возвращает первый индекс, по которому данный элемент может быть найден в массиве, или -1, если такого элемента нет.
// includes(value) — Проверяет, содержит ли массив определённый элемент, возвращает true или false.
// join(separator) — Объединяет все элементы массива в строку, используя указанный разделитель.
// flat(depth) — Возвращает новый массив с объединенными подмассивами на указанную глубину.
// flatMap(callback) — Применяет функцию к каждому элементу и затем объединяет результаты в новый массив.
// reduceRight(callback, initialValue) — Применяет функцию к аккумулятору и каждому элементу массива (справа налево), сводя массив к единственному значению.
// fill(value, start, end) — Заполняет все элементы массива от начального до конечного индекса указанным значением.
// from(arrayLike, mapFn, thisArg) — Создает новый массив из подобного массива или итерируемого объекта.
// copyWithin(target, start, end) — Копирует часть массива в другую позицию внутри того же массива, не изменяя его размер.

// Методы массивов

let search = "Коньяк";
let productList = ["Хлеб", "Сметана", "Коньяк", "Молоко", "Сыр"];
console.log(productList);

// Получим индекс элемента в массиве
let index = productList.indexOf(search);
console.log(index);

// Удалим последний аргумент (даже если пытаться переать значение)
// Он удалит последний элемент из массива и вернет его (положет в переменную)
// let lastItem = productList.pop();
// console.log(lastItem);

// Пример от Ивана
// productList.splice(index, 1);
// console.log(productList);

// slice старт и стоп, не включая стоп по индексу
// console.log(productList.slice(1, 3));

// splice - splice(start, deleteCount, item1, item2, ...)
// start - индекс, с которого начинается удаление
// deleteCount - сколько элементов удалить
// item1, item2, ... - элементы, которые нужно добавить в массив
let index2 = 2;
productList.splice(index2, 2, "Пиво", "Рыба");
console.log(productList);
// Мы удаляем элемент с индексом 2 (И СЛЕДУЮЩИЙ, согласно второго аргумента) и в это место добавляем два элемента

// Переопределим элемент с индексом 3
productList[3] = "Чипсы";
console.log(productList);

// push - ложит в конец массива
let newItem = "Ананас";
productList.push(newItem);
console.log(productList);

// shift - удаляет первый элемент массива
productList.shift();
console.log(productList);
// unshift - добавляет элемент в начало массива
productList.unshift("Ананас");
console.log(productList);
// forEach - проходит по всем элементам массива и выполняет функцию для каждого элемента
let stringNumsArray = ["1", "2", "3", "4", "5"];

// Отинтуем все элементы массива в число через forEach
stringNumsArray.forEach((element) => {
  console.log(Number(element));
});
console.log(stringNumsArray);

// map - создает новый массив, состоящий из результатов вызова функции для каждого элемента
let newArray = stringNumsArray.map((element) => {
  return Number(element);
});
console.log(newArray);

// sort - сортирует элементы массива на месте и возвращает отсортированный массив
console.log(productList.sort());
// reverse - изменяет порядок элементов в массиве на обратный
console.log(productList.reverse());
// concat - объединяет два или более массива, возвращая новый массив
console.log(newArray.concat(productList, stringNumsArray));
// flat - возвращает новый массив с объединенными подмассивами на указанную глубину
console.log(newArray.flat(2)); 
// fill - заполняет все элементы массива от начального до конечного индекса (не включительно!) указанным значением
console.log(productList.fill("Колбаса!", 2, 4));


// // 1. Добудим из документа ul#result
// let ulResult = document.querySelector("#result");
// // 2. Добавим в массив все элементы списка let startUl
// let startUl = ["Шматрица", "Братсво Кольца", "Буря в стакане"]

// // for (film of startUl) {
// //     ulResult.innerHTML += `<li>${film}</li>`;
// //   }

// // 3. Запросим prompt с вопросом введите названия фильмов через запятую
// let userInput = prompt("Введите названия фильмов через запятую и пробел");
// // 4. Разделим строку на массив через split
// let usersFilm = userInput.split(", ");
// // 5. Сложим эти два списка
// let finalUl = startUl.concat(usersFilm);

// // 6. Опустошим ul#result
// ulResult.innerHTML = "";
// // 7. Добавим в ul#result все элементы массива циклом элементы
// for (film of finalUl) {
//   ulResult.innerHTML += `<li>${film}</li>`;
// }

// Задачка! Проверить слово на палиндромность (чтение в обе стороны одинаковое)
// Примеры:
// А роза упала на лапу Азора
// Аргентина манит негра
// дед,

let word = "дед";
let sentence = "А роза упала на лапу Азора";

// 1. Приведем к нижнему регистру методом toLowerCase
// 2. Удалим все пробелы методом replace
// 3. Разделим строку на массив через split
// 4. Сравним массив с перевернутым массивом

let rawWord = sentence.toLowerCase().replaceAll(" ", "").split("");
let reversedWord = rawWord.slice().reverse();

console.log(rawWord);
console.log(reversedWord);

if (rawWord.join("") === reversedWord.join("")) {
  console.log(`${sentence} - Палиндром`);
} else {
  console.log(`${sentence} - НЕ палиндром`);
}

// Объекты

let personObj = {
  name: "Иван",
  age: 25,
  isMarried: true,
  isStudent: true,
  children: ["Маша", "Петя", "Вася"],
  "favorite Food": "Пицца",
};

console.log(personObj);
console.log(personObj.name);
console.log(personObj.children[0]);
// Перечислим всех детей через запятую .join
console.log(personObj.children.join(", "));


let wheater = {
  coord: { lon: 37.6156, lat: 55.7522 },
  weather: [{ id: 800, main: "Clear", description: "ясно", icon: "01n" }],
  base: "stations",
  main: {
    temp: 17.71,
    feels_like: 16.69,
    temp_min: 16.29,
    temp_max: 18.52,
    pressure: 1032,
    humidity: 44,
    sea_level: 1032,
    grnd_level: 1013,
  },
  visibility: 10000,
  wind: { speed: 2.46, deg: 72, gust: 5.4 },
  clouds: { all: 1 },
  dt: 1725558072,
  sys: {
    type: 2,
    id: 2094500,
    country: "RU",
    sunrise: 1725504159,
    sunset: 1725552847,
  },
  timezone: 10800,
  id: 524901,
  name: "Москва",
  cod: 200,
};


/////////////////////////////////////////////////////

// while(true) {
//   console.log("Купи слона!")
// }

// let i = 0;
// while (i <= 10) {
//   console.log(i);
//   i++;
// }

// Пропустим четные числа
let j = 0;

while (j <= 10) {
  // % - оператор деления по модулю
  if (j % 2 === 0) {
    j++;
    // Пропуск итерации - оператор continue
    continue;
  }
  console.log(j);
  j++;
}

// do while 

let k = 0;

do {
  console.log(k);
  k++;
  if (k === 5) {
    break;
  }
} while (k < 10);

////////////////////////
// Практика.

// Промптом спросим сколько вы хотите ввести данных о студентах
// Это будет количество итараций цикла while
// В цикле по очереди будем спрашивать фамилия, имя, группа итого студента
// Упаковываем все в объект
// Добавляем в массив
// Выводим консоль

let howManyStudents = prompt("Сколько студентов вы хотите ввести?");
let students = [];
let i = 0;
while (i < howManyStudents) {
  let student = {};
  student.firstName = prompt(`Введите имя студента №${i + 1}`);
  student.lastName = prompt(`Введите фамилию студента №${i + 1}`);
  student.group = prompt(`Введите группу студента №${i + 1}`);
  students.push(student);
  i++;
}

console.log(students);


// Вывести всех студентов по очереди циклом for of шаблонной строкой
for (student of students) {
  console.log(
    `Студент ${student.firstName} ${student.lastName} из группы ${student.group}`
  );
}
let userInput = prompt("Введите продукты через запятую и пробел").split(", ");

let userNum = prompt("Введите число");
let userNumInteger = parseInt(userNum);

alert(userInput[userNumInteger]);
