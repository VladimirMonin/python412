// Секретное послание
const secretLetter = [
  ["DFВsjl24sfFFяВАДОd24fssflj234"],
  ["asdfFп234рFFdо24с$#afdFFтasfо"],
  ["оafбasdf%^о^FFжа$#af243ю"],
  ["afпFsfайFтFsfо13н"],
  ["fн13Fа1234де123юsdсsfь"],
  ["чFFтF#Fsfsdf$$о"],
  ["и$##sfF"],
  ["вSFSDам"],
  ["пSFоsfнрSDFаSFвSDF$иFFтsfaсSFя"],
  ["FFэasdfтDFsfоasdfFт"],
  ["FяDSFзFFsыSfкFFf"],
];

// Массив с маленькими русскими буквами
const smallRus = [
  "а",
  "б",
  "в",
  "г",
  "д",
  "е",
  "ё",
  "ж",
  "з",
  "и",
  "й",
  "к",
  "л",
  "м",
  "н",
  "о",
  "п",
  "р",
  "с",
  "т",
  "у",
  "ф",
  "х",
  "ц",
  "ч",
  "ш",
  "щ",
  "ъ",
  "ы",
  "ь",
  "э",
  "ю",
  "я",
];

// let resultArray = [];


// for (innerArray of secretLetter) {
//     for (rowString of innerArray) {
//         resultArray.push(' ')
//         for (char of rowString) {
//       if (smallRus.includes(char)) {
//         resultArray.push(char);
//       }
//         }
//     }
// }

// // console.log(resultArray.join(""));
// // // я просто обожаю пайтон надеюсь что и вам понравится этот язык

// for (innerArray of secretLetter) {
//     resultArray.push(' ')
//     for (char of innerArray[0]) {

//         if (smallRus.includes(char)) {
//         resultArray.push(char);
//       }
//         }
//     }

// console.log(resultArray.join(""));
// // я просто обожаю пайтон надеюсь что и вам понравится этот язык


//// Объекты
let personObj = {
  name: "Сергей",
  last_name: "Сергеев",
  age: 22,
  hobbies: ["футбол", "пиво", "асинхронное программирование"],
  isStudent: true,
  isMarried: false,
  "is programmer": true,
}

// Во что превратит его метод объектов entries
let personEntriesArray = [['name', 'Сергей'], ['name', 'Сергей'], ['last_name', 'Сергеев']]

// console.log(personObj.name);
// console.log(personObj.hobbies);
// console.log(personObj["is programmer"]);
// // console.log(personObj."is programmer") - ОШИБКА. Для составных ключей нам нужны квадратные скобки

// let someKey = 'isMarried'
// // ПРИ ПОДСТАНОВКЕ ПЕРЕМЕННЫХ В ОБРАЩЕНИЕ К ОБЪЕКТУ - НАДО ИСПОЛЬЗОВАТЬ КВАДРАТНЫЕ СКОБКИ
// console.log('1', personObj[someKey]);
// console.log('2', personObj.someKey);
// if (personObj.isStudent) {
//   console.log("Студент");
// }
// else {
//   console.log("Не студент");
// }

// Цикл IN перебор ключей объекта
// for (let key in personObj) {
//   console.log(key);
// }

// ЭТОТ ЦИКЛ ПРОСТО ПО ОБЪЕКТУ НЕ РАБОТАЕТ
// for (let item of personObj) {
//     console.log(item);
//   }

// for (let key in personObj) {
//   if (key === "hobbies") {
//     console.log(key)
//     console.log(personObj.key);
//   }
//   }

// Пройдемся по ключам и значениям одновременно
// for (let key in personObj) {
//   console.log(key);
//   console.log(personObj[key]);
// }


// // Object.keys - получаем массив ключей
// console.log(Object.keys(personObj));
// // console.log(personObj.keys())  - ЭТО НЕ РАБОТАЕТ! Это не Пайтон ;)

// // Object.values
// console.log(Object.values(personObj));
// // Object.entries
// // Вариант с двумя переменными цикла 
// console.log(Object.entries(personObj));
// for (let [key, value] of Object.entries(personObj)) {
// //   console.log(key, value);
//   console.log(`Ключ:${key}, Значение:${value}`)
// }


// Практика!
// Введите имя студента let name = prompt
// Введите фамилию студента
// Введите возраст студента
// Соберите данные в объект let studentObj
// Выведите в консоль объект console.log(studentObj)

// let studentName = prompt("Введите имя студента");
// let studentLastName = prompt("Введите фамилию студента");
// let studentAge = prompt("Введите возраст студента");

// let studentObj = {
//   name: studentName,
//   last_name: studentLastName,
//   age: studentAge,
// };
// console.log(studentObj);

// Пользовательский ввод - а сколько вы хотите ввести студентов?
// let count = 3
// let resultArray = []
// Объявляем цикл for (i=0, i<= count, i++) - объявляем все эти переменные и ложим объект в массив методом push
// Выводим массив объектов в консоль

let count = prompt("Введите количество студентов");
count = parseInt(count);

let resultArray = [];

for (let i = 0; i < count; i++) {
  let studentName = prompt("Введите имя студента");
  let studentLastName = prompt("Введите фамилию студента");
  let studentAge = prompt("Введите возраст студента");

  let studentObj = {
    name: studentName,
    last_name: studentLastName,
    age: studentAge,
  };

  resultArray.push(studentObj);
}

console.log(resultArray);


