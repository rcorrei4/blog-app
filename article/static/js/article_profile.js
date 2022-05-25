followBtn = document.querySelector('#follow-btn')

if(followBtn != null) {
	followBtn.onclick = function () {
	fetch(`/accounts/follow/${followBtn.dataset.id}`, {
		method: 'GET',
	})
	.then(response => response.json())
	.then(result => {
		followBtn.innerText = result.result
	})
}
}

articlesBody = document.querySelectorAll('.article-body')

articlesBody.forEach((articleBody) => {
	articleBody.innerText = articleBody.innerText.replace('\n\n', ' - ')
})