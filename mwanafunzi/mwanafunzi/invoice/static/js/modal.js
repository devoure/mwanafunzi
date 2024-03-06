const modal = document.getElementById('modal')
const closeBtn = document.getElementById('close-btn')
const payBtn = document.getElementById('pay-btn')

payBtn.addEventListener('click', openModal)
closeBtn.addEventListener('click', closeModal)
window.addEventListener('click', outsideClose)

function openModal(){
  modal.style.display = 'flex'
}
function closeModal(){
  modal.style.display = 'none'
}
function outsideClose(e){
  if(e.target == modal){
    modal.style.display = 'none'
  }
}

