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
                    var buttons = '<a id="boton-detail" type="button" class="btn btn-primary" href="../category_edit/'+row.id+'"><i class="bi bi-pencil"></i></a> ';
                    buttons += '<a id="boton-detail" type="button" class="btn btn-success" href="../category_delete/'+row.id+'"><i class="bi bi-trash"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json){
        }
    });
});