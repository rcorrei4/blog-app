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