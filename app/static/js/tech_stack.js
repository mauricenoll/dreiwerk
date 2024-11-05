const observer = new IntersectionObserver( entries => {

    for (const entry of entries) {
        const imgs = entry.target.querySelectorAll('.language-card');

        for (const img of imgs) {
            if (entry.isIntersecting) {
                img.classList.add('language-card-animation');
                // return; // if we added the class, exit the function
            }
        }


        // We're not intersecting, so remove the class!
        // img.classList.remove('service-img-animation');
    }
});

document.addEventListener("DOMContentLoaded", function(){

      observer.observe(document.getElementById('softwaredev_container'));

});