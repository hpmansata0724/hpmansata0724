const arrows = document.querySelectorAll(".arrow");
const mainlist = document.querySelectorAll(".main-list");

arrows.forEach((arrow, i) => {
    const itemNumber=mainlist[i].querySelectorAll("img").length;
    let clickCounter=0;
  arrow.addEventListener("click", () => {
    clickCounter++;
    if(itemNumber-(3+clickCounter)>=0){
    mainlist[i].style.transform = `translateX(${mainlist[i].computedStyleMap()
        .get("transform")[0].x.value - 300}px)`;
    }else{
        mainlist[i].style.transform="translateX(0)";
        clickCounter=0;
    }
  });
  console.log(mainlist[i].querySelectorAll("img").length)
});
const ball = document.querySelector(".toggle-ball");
const items = document.querySelectorAll(".container,.movie-list-title,.navbar-container,.sidebar,.left-menu-icon,.toggle");

ball.addEventListener("click", () => {
    items.forEach(item => {
        item.classList.toggle("active");
    });
});
