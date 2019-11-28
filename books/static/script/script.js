jQuery(function ($) {


    $(".sidebar-dropdown > a").click(function () {
        $(".sidebar-submenu").slideUp(200);
        if (
            $(this)
            .parent()
            .hasClass("active")
        ) {
            $(".sidebar-dropdown").removeClass("active");
            $(this)
                .parent()
                .removeClass("active");
        } else {
            $(".sidebar-dropdown").removeClass("active");
            $(this)
                .next(".sidebar-submenu")
                .slideDown(200);
            $(this)
                .parent()
                .addClass("active");
        }
    });
    
    $("#show-sidebar").click(function () {
        $(".page-wrapper").addClass("toggled");
    });
    $("#close-sidebar").click(function () {
        $(".page-wrapper").removeClass("toggled");
    });

    //Progress bar
     $('.percent').percentageLoader({
                valElement: 'p',
                strokeWidth: 20,
                bgColor: 'transparent',
                ringColor: '#d53f3f',
                textColor: '#ffffff',
                fontSize: '16px',
                fontWeight: 'normal'
    });
});


// if(localStorage.getItem === 'toggled'){
//     alert('test')
// }