document.getElementById("submit").onclick = function() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    
    if (!username || !password) {
        return alert('请输入内容');
    }
    // Form submission is handled by the browser
};
