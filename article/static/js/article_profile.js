followBtn = document.querySelector('#follow-btn')

followBtn.onclick = function () {
	fetch(`/accounts/follow/${followBtn.dataset.id}`, {
		method: 'GET',
	})
	.then(response => response.json())
	.then(result => {
		followBtn.innerText = result.result
	})
}