const ul = document.querySelector('ul');
const dots = document.querySelectorAll('.dot');

ul.addEventListener('scroll', () => {
    const index = Math.round(ul.scrollLeft / ul.offsetWidth);
    dots.forEach(d => d.classList.remove('active'));
    dots[index].classList.add('active');
});

dots.forEach((dot, i) => {
    dot.addEventListener('click', () => {
        ul.scrollTo({ left: i * ul.offsetWidth, behavior: 'smooth' });
    });
});