
document.addEventListener("DOMContentLoaded", () => {
  // Afficher le formulaire de réponse
  document.querySelectorAll(".reply-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const form = document.getElementById(`reply-form-${btn.dataset.commentId}`);
      form.classList.toggle("d-none");
    });
  });

  // Déplier les réponses
 document.querySelectorAll('.toggle-replies').forEach(btn => {
    btn.addEventListener('click', () => {
      const replies = document.querySelector(btn.dataset.target);
      const icon = btn.querySelector('i');

      replies.classList.toggle('d-none'); // Affiche/masque les réponses
      icon.classList.toggle('fa-chevron-down');
      icon.classList.toggle('fa-chevron-up');
    });
  }); 
});

