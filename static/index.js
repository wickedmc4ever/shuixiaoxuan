//显示与隐藏控件
window.onload = function() {
    var username = document.getElementById('username').textContent;
    if (username) {
        document.getElementById('isVisible').style.display = 'none';
    } else {
        document.getElementById('logout').style.display = 'none';
    }
}
