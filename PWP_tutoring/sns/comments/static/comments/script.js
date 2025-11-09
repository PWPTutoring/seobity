document.addEventListener('DOMContentLoaded', function() {
    const submitBtn = document.querySelector('.btn-submit');

    submitBtn.addEventListener('click', function(e) {
        const input = document.querySelector('.comment-input');
        if (input && input.value.trim().length < 2) {
            alert('댓글은 2글자 이상 입력해주세요.');
            e.preventDefault();
        }
    });
});