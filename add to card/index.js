
import { add } from "../function.js"

console.log(add(1,7));
const appSetting =  {
    databaseURL: "https://addcart-de1ed-default-rtdb.asia-southeast1.firebasedatabase.app/"
}

const inputfieldEl =  document.getElementById("input-field")
const addButtonEl = document.getElementById("add-button")


addButtonEl.addEventListener("click",function(){

    let inputValue= inputfieldEl.value;
    // console.log(inputValue);
})