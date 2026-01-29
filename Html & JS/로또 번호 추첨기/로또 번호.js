// 버튼을 누르면 번호 출력
// n번째 숫자는 머시기

const btn = document.querySelector("#button")
const numArray = document.querySelector("#numArray")
let numArray2 = []
let count = 0
const notice = document.querySelector("#notice")



btn.addEventListener("click", () => {
    if(numArray2.length === 6){
        numArray.textContent = "";
        numArray2 = [];
        notice.innerHTML = "";
    }

    let lottoNumber = Math.floor((Math.random()*45) + 1);
    if(numArray2.includes(lottoNumber)){
        alert("중복된 숫자입니다")
    }
    else{
        numArray2.push(lottoNumber);
        numArray.textContent = numArray2.join(", ");
        const p = document.createElement("p")
        p.textContent = `${numArray2.length}번째 번호는 ${lottoNumber}입니다!`
        notice.append(p)
    }



})

