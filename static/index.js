let mode = 'dark';
let dark_image = 'Gruvbox 034.jpeg';
let light_image = 'light.jepg';
let theme_button = document.getElementById('theme');
let main_div = document.getElementById('main_div');
document.body.style.backgroundImage = `url('static/${dark_image}')`;
function theme() {
    console.log('theme()');
    if (mode == 'dark') {
        document.body.style.color = 'black';
        mode = 'light';
        theme_button.innerText = 'Light Mode';
        main_div.style.backgroundColor = 'white'
        document.body.style.backgroundImage = `url('static/${light_image}')`;
    } else {
        document.body.style.color = 'white';
        mode = 'dark';
        theme_button.innerText = 'Dark Mode';
        main_div.style.backgroundColor = 'black'
        document.body.style.backgroundImage = `url('static/${dark_image}')`;
    }
}