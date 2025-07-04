document.getElementById('cedula').addEventListener('blur', function () {
  const cedula = this.value;
  fetch(`/comerciantes/api/${cedula}`)
    .then(res => res.json())
    .then(data => {
      if (data) {
        document.getElementById('nombre').value = data.nombre;
        document.getElementById('apellido').value = data.apellido;
      }
    });
});

document.getElementById('fecha_nacimiento').addEventListener('change', function () {
  const fecha = new Date(this.value);
  const hoy = new Date();
  let edad = hoy.getFullYear() - fecha.getFullYear();
  if (hoy.getMonth() < fecha.getMonth() || (hoy.getMonth() === fecha.getMonth() && hoy.getDate() < fecha.getDate())) {
    edad--;
  }
  document.getElementById('edad').value = edad;
});
