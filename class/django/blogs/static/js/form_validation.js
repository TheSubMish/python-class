// Helper to show error messages
function addError(form, message) {
    let errorMsg = form.querySelector('.error-msg');
    if (!errorMsg) {
        errorMsg = document.createElement('div');
        errorMsg.className = 'error-msg';
        form.prepend(errorMsg);
    }
    errorMsg.textContent = message;
}

function clearError(form) {
    let errorMsg = form.querySelector('.error-msg');
    if (errorMsg) {
        errorMsg.remove();
    }
}

// Author form validation (example: Name required)
function setupAuthorFormValidation(formId) {
    const form = document.getElementById(formId);
    if (!form) return;
    form.addEventListener('submit', function(e) {
        clearError(form);
        const name = form.querySelector('input[name="name"]');
        if (name && name.value.trim() === '') {
            addError(form, "Name is required.");
            name.focus();
            e.preventDefault();
            return false;
        }
    });
}

// Blog form validation (example: Title and Content required)
function setupBlogFormValidation(formId) {
    const form = document.getElementById(formId);
    if (!form) return;
    form.addEventListener('submit', function(e) {
        clearError(form);
        const title = form.querySelector('input[name="title"]');
        const content = form.querySelector('textarea[name="content"]');
        if (title && title.value.trim() === '') {
            addError(form, "Blog title is required.");
            title.focus();
            e.preventDefault();
            return false;
        }
        if (content && content.value.trim() === '') {
            addError(form, "Blog content is required.");
            content.focus();
            e.preventDefault();
            return false;
        }
    });
}

// Comment form validation (example: Text required)
function setupCommentFormValidation(formId) {
    const form = document.getElementById(formId);
    if (!form) return;
    form.addEventListener('submit', function(e) {
        clearError(form);
        const text = form.querySelector('textarea[name="text"]');
        if (text && text.value.trim() === '') {
            addError(form, "Comment text is required.");
            text.focus();
            e.preventDefault();
            return false;
        }
    });
}