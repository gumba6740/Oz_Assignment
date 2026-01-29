const form =document.getElementById("form");

form.addEventListener("submit",(event) => {
    event.preventDefault();

    let userId = event.target.id.value;
    let userPw1 = event.target.password.value;
    let userPw2 = event.target.password2.value;
    let userName = event.target.name.value;
    let userTel = event.target.tel.value;
    let userEmail = event.target.email.value;
    let userPosition = event.target.position.value;
    let userGender = event.target.gender.value;
    let userIntro = event.target.intro.value;

    if(userId.length < 6){
        alert("아이디를 6글자 이상으로 정하세요");
    }

    else if(userPw1 !== userPw2){
        alert("비밀번호가 일치하지 않습니다");
    }

    else{
        document.body.innerHTML = `${userId}님 환영합니다!`;
        console.log("엘스 된다");
    }
})

