const pBar = document.querySelector("#HP");
const remainingHp = document.querySelector("h2");
const masage1 = document.querySelector("#masage11");
let hp = 1000
/* id를 숫자로 시작하지 말것 */



/* 무기는 검, 활, 도끼, 마법 총 4종류가 있습니다.
무기 입력 프롬프트가 랜덤하게 나타난다고 느낄 수 있습니다.
setInterval은 프롬프트 입력을 기다리지 않고 1.5초가 지나면 다음 작업을 수행합니다.
따라서, 무기 입력 시간이 1.5초보다 길면 다음 프롬프트는 순식간에 등장하고,
1.5초보다 짧으면 1.5초가 마저 지나간 이후 프롬프트가 등장합니다.*/
const battle = setInterval(() => {

        const sword = Math.floor(Math.random() * 21) + 50;
        const axe = Math.floor(Math.random() * 41) + 40;
        const magic = Math.floor(Math.random() * 61) + 30;
        const arrow = Math.floor(Math.random() * 11) + 55;

        let weapon = prompt("무기를 고르시오");
        let dmg = 0;

        if (weapon == "검") {
            dmg += sword;
        } else if (weapon == "도끼") {
            dmg += axe;
        } else if (weapon == "마법") {
            dmg += magic;
        } else if (weapon == "활") {
            dmg += arrow;
        } else {
            alert("올바른 무기를 고르세요");
        }

        hp -= dmg;


        if (hp <= 0) {
            hp = 0;
            masage1.textContent = "괴물이 쓰러졌습니다";
            remainingHp.textContent = `남은 체력: ${hp}`;
            pBar.value = hp;
            clearInterval(battle)
        }
        else {
            remainingHp.textContent = `남은 체력: ${hp}`;
            masage1.textContent = `${dmg}의 데미지를 입혔습니다`;
            pBar.value = hp;
        }
}, 1500)

