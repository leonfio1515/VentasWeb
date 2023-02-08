$(function (){
    $('#tabla').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {"action":"searchdata"},
            dataSrc:"",
        },
        columns: [
            {'data':'id'},
            {'data':'name'},
            {'data':'id'},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data,type, row){
                    return '<b>Boton</b>';
                }
            },
        ],
        initComplete: function (settings, json){
            alert('Tabla cargada');
        }
    });
});