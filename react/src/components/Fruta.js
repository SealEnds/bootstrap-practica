import React from 'react';

class Fruta extends React.Component {
  constructor() {
    super()
    this.state = {
      precioKg: 1,
      cantidad: 0
    }
  }

  agregar() {
    let step = parseInt(this.getPrecioStep());
    console.log(this.getPrecioStep());
    if (step === 1 || step === 5 || step === 10) {
      this.setState({
        // https://stackoverflow.com/questions/7342957/how-do-you-round-to-one-decimal-place-in-javascript
        precioKg: parseFloat((this.state.precioKg + step / 10).toFixed(1))
      })
    }
  }
  quitar() {
    let step = parseInt(this.getPrecioStep());
    if (step === 1 || step === 5 || step === 10) {
      if (this.state.precioKg - step / 10 > 0) {
        this.setState({
          precioKg: parseFloat((this.state.precioKg - step / 10).toFixed(1))
        })
      }
    }
  }
  limpiar() {
    this.setState({
      precioKg: 0
    })
  }

  agregarUnidad() {
    let step = parseInt(this.getUdStep());
    console.log(this.getUdStep());
    if (step === 1 || step === 5 || step === 10) {
      this.setState({
        cantidad: this.state.cantidad + step
      })
    }
  }
  quitarUnidad() {
    let step = parseInt(this.getUdStep());
    if (step === 1 || step === 5 || step === 10) {
      if (this.state.cantidad - step >= 0) {
        this.setState({
          cantidad: this.state.cantidad - step
        })
      }
    }
  }
  limpiarUnidades() {
    this.setState({
      cantidad: 0
    })
  }

  getPrecioStep() {
    let result = ''
    let radiobtn = document.querySelectorAll('.incremento')
    radiobtn.forEach(element => {
      if (element.checked) {
        result = element.value
        element.checked = "checked"
      } else {
        element.checked = ""
      }
    })
    return result
  }

  getUdStep() {
    let result = ''
    let radiobtn = document.querySelectorAll('.incrementoCantidad')
    radiobtn.forEach(element => {
      if (element.checked) {
        result = element.value
        element.checked = "checked"
      } else {
        element.checked = ""
      }
    })
    return result
  }

  render() {
    const limitToRed = 0;
    const limitToBlue = 4;
    let precioTotal = parseFloat((this.state.precioKg * this.state.cantidad).toFixed(1));
    const changeStylesByValues = {
      // Usar varias condiciones en el operador ternario: https://stackoverflow.com/questions/12548857/multiple-conditions-in-ternary-conditional-operator
      color: this.state.cantidad > limitToBlue ? 'blue' : precioTotal <= limitToRed ? 'red' : 'black',
      fontWeight: this.state.cantidad > limitToBlue ? 'bold' : precioTotal <= limitToRed ? 'bold' : 'normal',
      fontStyle: this.state.cantidad > limitToBlue ? 'italic' : 'normal'
    };
    return (
      <div class="fruta">
        <h2>{this.props.nombre}</h2>
        <div>Origen: {this.props.origen}</div>
        <div>Fecha de Recogida: {this.props.fechaRecogida}</div>
        <div>Precio KG: <span class="value">{this.state.precioKg}</span></div>
        <div class="div_precio_step">
          <input class="incremento" type="radio" name="precio_step" value="1" />
          <label>0.1 €/KG</label>
          <input class="incremento" type="radio" name="precio_step" value="5" />
          <label>0.5 €/KG</label>
          <input class="incremento" type="radio" name="precio_step" value="10" />
          <label>1 €/KG</label>
        </div>
        <div class="buttons">
          <button onClick={this.agregar.bind(this)}>Añadir</button>
          <button onClick={this.quitar.bind(this)}>Quitar</button>
          <button onClick={this.limpiar.bind(this)}>Limpiar</button>
        </div>
        <div>Cantidad:  <span class="value">{this.state.cantidad}</span></div>
        <div class="div_cantidad_step">
          <input class="incrementoCantidad" type="radio" name="cantidad_step" value="1" />
          <label>1 Ud</label>
          <input class="incrementoCantidad" type="radio" name="cantidad_step" value="5" />
          <label>5 Uds</label>
          <input class="incrementoCantidad" type="radio" name="cantidad_step" value="10" />
          <label>10 Uds</label>
        </div>
        <div class="buttons">
          <button onClick={this.agregarUnidad.bind(this)}>Añadir</button>
          <button onClick={this.quitarUnidad.bind(this)}>Quitar</button>
          <button onClick={this.limpiarUnidades.bind(this)}>Limpiar</button>
        </div>
        <div style={changeStylesByValues}>
          <span>Precio Total: </span><span>{precioTotal}</span>
        </div>
        <div>
          <img src={this.props.src} alt={this.props.nombre}></img>
        </div>
      </div>
    )
  }
}

export default Fruta;