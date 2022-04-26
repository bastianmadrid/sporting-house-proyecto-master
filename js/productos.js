$(document).ready(() => {
    $("#stock").hide();
    $("#ocultar").hide();
    $("#buscar").click(function() {
        $.ajax({
            type: 'GET',
            url: 'json/BD.json',
            dataType: 'json',
        }).done((data) => {
            $.each(data, function(indice, objeto) {
                let fila = $(`<tr>`);
                fila.append($(`<td><img scr='${objeto.img}'></td>`));
                fila.append($(`<td>${objeto.nombre}</td>`));
                fila.append($(`<td>${objeto.id}</td>`));
                fila.append($(`<td>${objeto.costo}</td>`));

                $('#stock tbody').append(fila);
            })
            $('#stock').show();
        })
        $("#buscar").hide();
        $("#ocultar").show();
    })

    $("#ocultar").click(function() {
        $.ajax({
            type: 'GET',
            url: 'json/BD.json',
            dataType: 'json',
        }).done((data) => {
            $.each(data, function(indice, objeto) {
                let fila = $(`<tr>`);
                fila.append($(`<td><img scr=></td>`));
                fila.append($(`<td></td>`));
                fila.append($(`<td></td>`));
                fila.append($(`<td></td>`));

                $('#stock tbody').append(fila);
            })
            $("#stock").hide();
            $("#buscar").show();
            $("#ocultar").hide();
        })
    })
});