odoo.define('x_custom_application.karcel_task',[] ,function (require) {
    "use strict";

console.log("Hey!!")

    $(document).ready(function() {


            $('input[type="checkbox"]').change(function() {

                if ($(this).attr('name') === 'brand') {
                    var brandId = $(this).val();
                    var isChecked = $(this).is(':checked');

                    // Find models with the same parent brand id and check/uncheck them
                    $('input[name="model"][data-brand-id="' + brandId + '"]').each(function() {
                        $(this).prop('checked', isChecked);
                    });
                }

                var form = $('#filter-form').serialize();
                $.ajax({
                    url: "/apply_filter",
                    type: "GET",
                    data: {selected_data:form},
                    success: function(response) {
                        $('.products-list').html($(response).find('.products-list').html());
                    },
                    error: function() {
                        alert('Error while filtering products.');
                    }
                });
            });
    });
});
