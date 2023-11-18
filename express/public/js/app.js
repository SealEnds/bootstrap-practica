function get(id){
    return document.getElementById(id);
}

let h1 = document.getElementsByTagName('h1')[0];
let select_artist = get('artists');
let home = get('volver');

if (typeof(select_artist) != 'undefined' && select_artist != null){
    select_artist.addEventListener('change', () => {
        selection = select_artist.value;
        let target = `/album/${selection}`;
        let url = `${window.location.protocol}${target}`;
        window.location.href = url;
    });
}
if (typeof(home) != 'undefined' && home != null){
    home.addEventListener('click', () => {
        let target = `/index`;
        let url = `${window.location.protocol}${target}`;
        window.location.href = url;
    });
}
