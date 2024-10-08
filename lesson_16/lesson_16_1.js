// 1. Добыть данные из поля ввода id = inputText
// 2. Найти параграф с pFormOutput id
// 3. Переписать текстовое содержимое параграфа

function displayFormContent (event) {
    
    // Блокируеем отправку формы по умолчанию, как это происиходит при клике на кнопку
    event.preventDefault(); // Предотвращаем стандартное поведение формы (отправка с обновлением страницы)
    
    // Получаем данные из поля ввода id = inputText
    let inputText = document.getElementById('inputText');
    
    let pFormOutput = document.getElementById('pFormOutput');

    let intputVaue = inputText.value; 

    pFormOutput.textContent = intputVaue;
    console.log(intputVaue);

}
