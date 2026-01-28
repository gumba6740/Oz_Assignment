const pBar = document.querySelector("#HP");
const remainingHp = document.querySelector("h2");
const masage1 = document.querySelector("#masage11");
let hp = 1000
/* id를 숫자로 하지 말것 */

//
function sleep(ms) {
    return new Promise(resolve => {
        setTimeout(resolve, ms);
    });
}


async function battle() {
    while (hp > 0) {
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
            continue;
        }

        hp -= dmg;


        if (hp <= 0) {
            hp = 0;
            masage1.textContent = "괴물이 쓰러졌습니다";
            remainingHp.textContent = `남은 체력: ${hp}`;
            pBar.value = hp;
        }
        else {
            remainingHp.textContent = `남은 체력: ${hp}`;
            masage1.textContent = `${dmg}의 데미지를 입혔습니다`;
            pBar.value = hp;
        }

        await sleep(1000);

    }
}

battle();