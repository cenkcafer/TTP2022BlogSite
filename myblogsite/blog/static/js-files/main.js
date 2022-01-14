//Get the elements from class .date in HTML and store into getDate
const getDate = document.querySelector(“.date”);
// Get the element with class .topocs-show  from html and store in openWindow
const openWindow = document.querySelector(“.topics-show”);
// Get the element with class .topocs-box  from html and store in topicBox
const topicBox = document.querySelector(“.topic-box”);
// Get the element with class .close  from html and store in topicBox
const closeWindow = document.querySelector(“.close”);
// creating a date element using JS
const date = new Date();
//storing the full year date in getDate.textContent
getDate.textContent = date.getFullYear();
//adding event in closeWindow class, topic bolx gets show property and openWindow gets dont-show property on click event.
closeWindow.addEventListener(“click”,()=>{
    topicBox.classList.toggle(‘show’)
    openWindow.classList.toggle(‘dont-show’)
});
//adding event in openWindow class, topicbox gets show property and
//openWindow gets dont-show property on click event.
openWindow.addEventListener(“click”, () => {
    topicBox.classList.toggle(‘show’)
    openWindow.classList.toggle(‘dont-show’)
    //print the value of topicBOl.classList in console, used for debugginh purpose
    console.log(topicBox.classList)
});
