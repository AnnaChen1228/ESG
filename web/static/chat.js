//chatbot&generator_report
function switchTab(element) {
    var items = document.querySelectorAll('.menu-item');
    items.forEach(function(item) {
        item.classList.remove('active');
    });
    element.classList.add('active');
}


function toggleHint() {
    const hint = document.querySelector('.hint');
    const arrow = document.querySelector('.toggle-arrow');
    // const headerText = document.querySelector('.hint-header');
    
    hint.classList.toggle('collapsed');
    
    if (hint.classList.contains('collapsed')) {
        arrow.innerHTML = '&#10094;'; // 左箭头
        // headerText.innerHTML = '撰寫指引 <span class="toggle-arrow">&#10094;</span>';
    } else {
        arrow.innerHTML = '&#10095;'; // 右箭头
        // headerText.innerHTML = '撰寫指引 <span class="toggle-arrow">&#10095;</span>';
    }
}


// menu
function toggleMenu() {
    const menu = document.querySelector('.menu');
    const arrow = document.querySelector('.toggle-arrow_menu');
    // const headerText = document.querySelector('.menu-header');
    // const ul = document.querySelector('.menu-content');
    menu.classList.toggle('collapsed');
    
    if (menu.classList.contains('collapsed')) {
        arrow.innerHTML = '&#10095;'; // 左箭头
        // headerText.innerHTML = 'Menu <span class="toggle-arrow_menu">&#10094;</span>';
    } else {
        arrow.innerHTML = '&#10094;'; // 右箭头
        // headerText.innerHTML = 'Menu <span class="toggle-arrow_menu">&#10095;</span>';
    }
}

function toggleCheckHint() {
    const hint = document.querySelector('.check-box');
    const arrow = document.querySelector('.toggle-arrow');
    // const headerText = document.querySelector('.hint-header');
    
    hint.classList.toggle('collapsed');
    
    if (hint.classList.contains('collapsed')) {
        arrow.innerHTML = '&#10094;'; // 左箭头
        // headerText.innerHTML = '撰寫指引 <span class="toggle-arrow">&#10094;</span>';
    } else {
        arrow.innerHTML = '&#10095;'; // 右箭头
        // headerText.innerHTML = '撰寫指引 <span class="toggle-arrow">&#10095;</span>';
    }
}
