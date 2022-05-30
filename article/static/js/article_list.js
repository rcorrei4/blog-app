articlesBody = document.querySelectorAll('.article-body')

articlesBody.forEach((articleBody) => {
	articleBody.innerText = articleBody.innerText.replace('\n\n', ' - ')
})