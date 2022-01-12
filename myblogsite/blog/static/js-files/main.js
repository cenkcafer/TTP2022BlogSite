const getDate = document.querySelector(".date");

const openWindow = document.querySelector(".topics-show");
const topicBox = document.querySelector(".topic-box");
const closeWindow = document.querySelector(".close");

// creating a date
const date = new Date();
getDate.textContent = date.getFullYear();

closeWindow.addEventListener("click",()=>{
    topicBox.classList.toggle('show')
    openWindow.classList.toggle('dont-show')

});

openWindow.addEventListener("click", () => {
    topicBox.classList.toggle('show')
    openWindow.classList.toggle('dont-show')
    console.log(topicBox.classList)
});
