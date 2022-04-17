const API_URL = "https://dt.miet.ru/ppo_it_final"
const API_X_AUTH_TOKEN = "hnzqhpuc"
let btn = document.querySelector("#btn")

btn.addEventListener('click', () => {
    fetch(API_URL, {
        headers: {
            "X-Auth-Token": API_X_AUTH_TOKEN
        },
        mode: "no-cors"
    }).then((r) => console.log(r))
})