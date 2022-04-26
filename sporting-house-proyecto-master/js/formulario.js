const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');

const expresiones = {

    nombre: /^[a-zA-ZÀ-ÿ\s]{3,40}$/, // Letras y espacios, pueden llevar acentos.
    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
}

const campos = {
    username: false,
    email: false
}

const validarFormulario = (e) => {
    switch (e.target.name) {
        case "username":
            if (expresiones.nombre.test(e.target.value)) {
                document.getElementById('contacto_nombre').classList.add('formulario_contacto-incorrecto');
                document.getElementById('contacto_nombre').classList.remove('formulario_contacto-correcto');
                document.querySelector('#contacto_nombre .formulario__input-error').classList.remove('formulario__input-error-activo')
                campos['username'] = false;

            } else {

                document.getElementById('contacto_nombre').classList.remove('formulario_contacto-incorrecto');
                document.querySelector('#contacto_nombre .formulario__input-error').classList.add('formulario__input-error-activo')
                document.getElementById('contacto_nombre').classList.add('formulario_contacto-correcto');
                campos['username'] = true;
            }
            break;
        case "email":
            if (expresiones.correo.test(e.target.value)) {
                document.getElementById('contacto_correo').classList.add('formulario_contacto-incorrecto');
                document.getElementById('contacto_correo').classList.remove('formulario_contacto-correcto');
                document.querySelector('#contacto_correo .formulario__input-error').classList.remove('formulario__input-error-activo')
                campos['email'] = false;

            } else {
                document.getElementById('contacto_correo').classList.remove('formulario_contacto-incorrecto');
                document.getElementById('contacto_correo').classList.add('formulario_contacto-correcto');
                document.querySelector('#contacto_correo .formulario__input-error').classList.add('formulario__input-error-activo')
                campos['email'] = true;

            }

            break;
    }

}
inputs.forEach((input) => {
    input.addEventListener('keyup', validarFormulario);
    input.addEventListener('blur', validarFormulario);
});
formulario.addEventListener('submit', (e) => {
    e.preventDefault();
    const terminos = document.getElementById('terminos');
    if (campos.username && campos.email) {
        formulario.reset();
        document.getElementById('formulario__mensaje-exito').classList.add('formulario__mensaje-exito-activo');
        setTimeout(() => {
            document.getElementById('formulario__mensaje-exito').classList.remove('formulario__mensaje-exito-activo');
        }, 5000);
    } else {
        document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo');
    }
});