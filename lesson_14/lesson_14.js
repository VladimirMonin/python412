// Функции

// // Функции в JS определяются ключевым словом function
// // параметры функции - переменные которые будут передаваться в функцию
// function getSum(a, b) {
//   console.log(a + b);
// }

// getSum(2, 2);

// function messageName(message, name) {
//   console.log(`Message: ${message}, Name: ${name}`);
// }

// messageName("Привет", "Фёдор");

// messageName("Привет"); // Второй аргумент undefined
// messageName("Привет", "Николай", "Петрович"); // Третий проигнорируется

// // Значение по умолнчаию в функциях JS

// function consoleMsg(message, name = "Гость") {
//   console.log(`Message: ${message}, Name: ${name}`);
// }

// consoleMsg("Привет");
// consoleMsg("Привет", "Николай");

// // Такой вариант не будет работать как ожидаете
// // Потому что значение по-умолчанию должно быть последним аргументом
// function consoleMsg2(name = "Гость", message) {
//   console.log(`Message: ${message}, Name: ${name}`);
// }

// consoleMsg2("Привет");

// let result = getSum(2, 2); // undefined

// function getSum2(a, b) {
//   sum = a + b;
//   return sum;
// }

// let result2 = getSum2(2, 2); // 4 - получим данные, потому что функция отдает значение

// const users = [
//   { name: "Ирина", age: 25 },
//   { name: "Сергей", age: 30 },
//   { name: "Анна", age: 22 },
//   { name: "Дмитрий", age: 35 },
// ];

const users2 = [
    { name: "Nicola", age: 25 },
    { name: "Sergio", age: 30 },
    { name: "Anny", age: 22 },
    { name: "Dimitry", age: 35 },
  ];

// console.log(getUserNames(users2))

// // 1. **Создание функции для приветствия**:
// // Напишите функцию `greet`, которая принимает имя пользователя в качестве аргумента и возвращает строку приветствия. Например, вызов `greet("Алексей")` должен вернуть `"Привет, Алексей!"`. Это поможет вам понять, как работать с аргументами функции и возвращаемыми значениями.

// function greet(name) {
//   return `Привет, ${name}!`;
// }

// // 2. **Функция для фильтрации по возрасту**:
// // Создайте функцию `filterByAge`, которая принимает массив объектов пользователей и возраст, и возвращает новый массив, содержащий только тех пользователей, чей возраст больше указанного. Например, вызов `filterByAge(users, 28)` должен вернуть массив с пользователями, возраст которых больше 28 лет.

function filterByAge(usersArray, age) {
  let ageFilteredArray = [];
  for (user of usersArray) {
    if (user.age > age) {
      ageFilteredArray.push(user);
    }
  }
  return ageFilteredArray;
}

function filterByAge2(usersArray, age) {
  let ageFilteredArray = usersArray.filter((user) => user.age > age);
  return ageFilteredArray;
}

// let filterResult = filterByAge(users2, 28);
// // console.log(filterResult);

// // console.log(filterByAge(users, 28))


// 3. **Функция для поиска по имени**:
// Реализуйте функцию `findUserByName`, которая принимает массив объектов пользователей и имя, и возвращает объект пользователя с указанным именем. Если пользователь не найден, функция должна возвращать `null`. Например, вызов `findUserByName(users, "Анна")` должен вернуть объект `{ name: "Анна", age: 22 }`.

// function findUserByName(users, name) {
//   for (user of users) {
//     if (user.name === name) {
//       return user;
//     }
//   }
//   return null;
// }

function findUserByName2(users, name) {
  return users.filter((user) => user.name === name);
}

// // 4. **Функция для подсчета количества пользователей**:
// // Напишите функцию `countUsers`, которая принимает массив объектов пользователей и возвращает количество пользователей в этом массиве. Например, вызов `countUsers(users)` должен вернуть `4`.

// function countUsers(users) {
//   return users.length;
// }

// // 5. **Функция для преобразования массива имен**:
// // Реализуйте функцию `getUserNames`, которая принимает массив объектов пользователей и возвращает массив только с именами пользователей. Например, вызов `getUserNames(users)` должен вернуть массив `["Ирина", "Сергей", "Анна", "Дмитрий"]`.

// function getUserNames(users) {
//   let userNames = [];
//   for (user of users) {
//     userNames.push(user.name);
//   }
//   return userNames;
// }

// ОБЛАСТИ ВИДИМОСТИ В JS
// 1. Глобальная область видимости - данные доступны во всем коде
// 2. Локальная область видимости - данные доступны только в пределах функции
// 3. Блочная область видимости - данные доступны только в пределах блока кода

// let user = "Nicola Tesla"; 

// function logUser() {
//   console.log(user); // Переменная из глобальной области видимости
// }

// logUser();


// function logUser2(user) {
//   console.log(user); // Локальная область видимости
// }

// // Локальная переменная user не переопределила глобальную
// logUser2("Daniel");
// logUser();


// function logUser3(userName) {
//   // Если тут не поставить let - объявление переменной
//   // Мы перезаписываем глобальную переменную с тем же именем user
//   let user = userName
//   console.log(user); // Локальная область видимости
// }
// logUser3("Rafael");
// logUser();

// // Блочная область видимости
// if (true) {
//   let user = "Сергей Блок";
//   let blockUser = "Пользователь объявленный в блоке"
//   console.log(user);
//   console.log(blockUser);
//   logUser3('Вызов из блока')
// }

// logUser();
// console.log(blockUser);


// Стрелочные функции
const sum = (a, b) => a + b;

function sum2(a, b) {
  return a + b;
}

const fruits = ['apple', 'banana', 'orange'];

// На месте этой функции могла бы быть логика добавления данных в HTML файл
function logFruits(fruit) {
  console.log(fruit);
}

fruits.forEach((fruit) => {
  logFruits(fruit);
});


const numbers = [1, 2, 3, 4];
const doubled = numbers.map((number) => number * 2);

console.log(doubled); // [2, 4, 6, 8]


let userNums = prompt("Введите числа через запятую").split(","); // Разделяем введённые пользователем числа на массив
userNums = userNums.map((num) => Number(num)); // Преобразуем строки массива в числа

// Фильтр

const numbers2 = [5, 10, 15, 20, 25];

// Функция фильтрации: выбирает только числа больше 15
const greaterThanFifteen = numbers2.filter((number) => number > 15);

console.log(greaterThanFifteen); // [20, 25]