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