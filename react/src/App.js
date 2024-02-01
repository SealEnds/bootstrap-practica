
import './App.css';
import Fruta from './components/Fruta';
import romanescu_file from './assets/romanescu.jpg';
import pitahaya_file from './assets/pitahaya.jpg';
import chirimoya_file from './assets/chirimoya.jpg';
import yuca_file from './assets/yuca.jpg';
import datil_file from './assets/datil.jpg';

const Frutas = [
  {
    "nombre": "Romanescu",
    "origen": "Italia",
    "recogida": "20/11/2023",
    "src": romanescu_file
  },
  {
    "nombre": "Pitahaya",
    "origen": "México",
    "recogida": "20/11/2023",
    "src": pitahaya_file
  },
  {
    "nombre": "Chirimoya",
    "origen": "Granada",
    "recogida": "20/11/2023",
    "src": chirimoya_file
  },
  {
    "nombre": "Yuca",
    "origen": "Paraguay",
    "recogida": "20/11/2023",
    "src": yuca_file
  },
  {
    "nombre": "Dátil",
    "origen": "Magreb",
    "recogida": "21/11/2023",
    "src": datil_file
  }
]

function App() {
  return (
    <div id="main">
      <h1>Frutas Con React</h1>
      <div class="center">
        <section>
          <Fruta nombre={Frutas[0].nombre} origen={Frutas[0].origen} fechaRecogida={Frutas[0].recogida} src={Frutas[0].src}/>
          <Fruta nombre={Frutas[1].nombre} origen={Frutas[1].origen} fechaRecogida={Frutas[1].recogida} src={Frutas[1].src}/>
          <Fruta nombre={Frutas[2].nombre} origen={Frutas[2].origen} fechaRecogida={Frutas[2].recogida} src={Frutas[2].src}/>
          <Fruta nombre={Frutas[3].nombre} origen={Frutas[3].origen} fechaRecogida={Frutas[3].recogida} src={Frutas[3].src}/>
          <Fruta nombre={Frutas[4].nombre} origen={Frutas[4].origen} fechaRecogida={Frutas[4].recogida} src={Frutas[4].src}/>
        </section>
      </div>
    </div>
  );
}

export default App;
