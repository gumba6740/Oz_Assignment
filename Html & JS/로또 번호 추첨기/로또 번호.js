/* 버튼을 누르면 1~45의 숫자가 랜덤하게 출력됩니다.
중복되는 숫자가 출력될 시, 경고창이 뜨고 해당 숫자를 무효화합니다. 
최대 6개의 숫자가 출력됩니다. 6개의 숫자가 출력된 상태에서 버튼을 누르면
숫자의 개수가 1개인 상태로 돌아갑니다. */
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

