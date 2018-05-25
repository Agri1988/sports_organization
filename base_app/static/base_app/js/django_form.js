function bootstrap_form(selector) {
    var form = document.querySelector(selector);
    form.setAttribute('role',"form");
    //form.setAttribute('class',"form-inline")
    var element_in_form = Array.from(form.getElementsByTagName('p'));
    element_in_form.forEach(function (value, index) {
        var wrapper = document.createElement('div');
        wrapper.setAttribute('class', 'form-group')
        wrapper.innerHTML = value.innerHTML;
        value.parentNode.replaceChild(wrapper,value)
    });
    var form = document.querySelectorAll(selector+' div :not(label) ' );
    form.forEach(function(item, i, arr){
    console.log(form[i].setAttribute('class','form-control'))
});
}
function django_date_to_datefield(selector) {
    var date_field = $(selector);
    var date_field_value = date_field.val();
    date_field.prop('type', 'date');
    console.log(date_field_value.substring(2,3));
    if (date_field_value.substring(2,3) == '.'){

        date_field.val(date_field_value.substring(6)+'-'+date_field_value.substring(3,5)+'-'+date_field_value.substring(0,2))
    }
}