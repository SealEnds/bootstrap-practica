function get(id){
    return document.getElementById(id);
}

let h1 = document.getElementsByTagName('h1')[0];
let select_country = get('countries');
let home = get('homelink');

if (typeof(select_country) != 'undefined' && select_country != null){
    select_country.addEventListener('change', () => {
        selection = select_country.value;
        let target = `/pais/${selection}`;
        let url = `${window.location.protocol}${target}`;
        window.location.href = url;
    });
}
// volver al menú de inicio (no muestra detalles de ningún artista)
if (typeof(home) != 'undefined' && home != null){
    home.addEventListener('click', () => {
        let target = `/index`;
        let url = `${window.location.protocol}${target}`;
        window.location.href = url;
    });
}
