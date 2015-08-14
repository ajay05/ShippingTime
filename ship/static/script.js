function toggleOther(el) {
    console.log(el.value);
    if (el.value == "other") {
        $('.other_carrier').show();
    } else {
        $('.other_carrier').hide();
    }
};
