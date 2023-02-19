let workingLang = document.getElementById('workingLang');
let langs = document.querySelectorAll('li');
let langDisplay = document.getElementById('langSelect');

langs.forEach(lang => lang.addEventListener('click', function (event) {
    workingLang.name = this.id;
    langDisplay.innerHTML = workingLang.name;
}))