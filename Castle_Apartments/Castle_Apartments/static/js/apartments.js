$(document).ready(function() {
    $('#search-btn').on('click', function (e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        var apartment_type = $('#type').val();
        var apartment_rooms = $('#rooms').val();
        var apartment_zip = $('#zip').val();
        var apartment_address_ordering = $('#address_order').val();
        var apartment_price_ordering = $('#price_order').val();
        var apartment_date_ordering = $('#date_order').val();

        $.ajax({
            url: '/apartments?search_filter=' + searchText + '&type=' + apartment_type + '&rooms=' + apartment_rooms + '&zip=' + apartment_zip + '&date_order=' + apartment_date_ordering + '&price_order=' + apartment_price_ordering + '&address_order=' + apartment_address_ordering,
            type: 'GET',
            success: function (resp) {
                var newHtml = resp.data.map(d => {
                    return   `
                        
                             <div class="container">
                                 <div class="column">
                                    <div class="card mb-4 shadow-sm">
                                        <a href="/apartments/${d.id}">
                                           <div class="card-body" style="border-style: solid; border-color: black; border-width: 0.5%; background-color: lightgray; color: black;">
                                               <img class="apartment-img" style=" width: 400px;" src="${d.firstimage}" />
                                                <h4>${d.address} </h4>
                                                <p>${d.price} kr.</p>    
                                                <p>${d.size} fermetrar</p>                                  
                                            </div>
                                        </a>
                                    </div>
                                </div>
                            </div>`

                });
                $('.row2').html(newHtml.join(''));
                $('#search-box').val('');
                $('#type').val('');
                $('#rooms').val('');
                $('#zip').val('');
                $('#address').val('');
            },
            error: function (xhr, status, error) {
                //TODO: show toastr
                console.error(error);
            }
        });
    });
// this below has purpose to disable the other inputs when order input is chosen
    $('#date_order').change(function () {
        var x = document.getElementById("date_order").value;
        if (x != "Not_selected") {
            $('#price_order').attr('disabled','disabled');
            $('#address_order').attr('disabled','disabled');
        } else  {
            $('#price_order').removeAttr('disabled');
            $('#address_order').removeAttr('disabled');
        }
    })
    $('#price_order').change(function () {
        var x = document.getElementById("price_order").value;
        if (x != "Not_selected") {
            $('#date_order').attr('disabled','disabled');
            $('#address_order').attr('disabled','disabled');
        } else  {
            $('#date_order').removeAttr('disabled');
            $('#address_order').removeAttr('disabled');
        }
    })
    $('#address_order').change(function () {
        var x = document.getElementById("address_order").value;
        if (x != "Not_selected") {
            $('#price_order').attr('disabled','disabled');
            $('#date_order').attr('disabled','disabled');
        } else  {
            $('#price_order').removeAttr('disabled');
            $('#date_order').removeAttr('disabled');
        }
    })
});