// Character Counter

const postContent = document.getElementById("postContent");
const charCount = document.getElementById("charCount");

if (postContent) {

    postContent.addEventListener("input", function () {

        let length = this.value.length;

        charCount.innerText = length;

        if (length > 200) {

            alert("Maximum 200 characters allowed");

            this.value = this.value.substring(0, 200);

            charCount.innerText = 200;
        }
    });
}


// Dark Mode

const darkModeBtn = document.getElementById("darkModeBtn");

if (darkModeBtn) {

    darkModeBtn.addEventListener("click", function () {

        document.body.classList.toggle("dark-mode");

    });
}