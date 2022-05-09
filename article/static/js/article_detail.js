likeBtn = document.querySelector('#like-btn')

likeBtn.onclick = function () {
	fetch(`/article/${likeBtn.dataset.slug}/like`, {
		method: 'GET',
	})
	.then(response => response.json())
	.then(result => {
		likeBtn.innerText = result.result
	})
}

saveBtn = document.querySelector('#save-btn')

saveBtn.onclick = function () {
	fetch(`/article/${saveBtn.dataset.slug}/save`, {
		method: 'GET',
	})
	.then(response => response.json())
	.then(result => {
		saveBtn.innerText = result.result
	})
}