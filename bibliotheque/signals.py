import fitz  # PyMuPDF
from PIL import Image
from io import BytesIO
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.base import ContentFile
from .models import Livre


@receiver(post_save, sender=Livre)
def generate_cover_image(sender, instance, created, **kwargs):
    """
    Extrait automatiquement la première page du fichier PDF du livre
    et la sauvegarde comme image de couverture.
    """
    if instance.fichier and (not instance.cover_image):

        try:
            pdf_path = instance.fichier.path
            pdf_document = fitz.open(pdf_path)

            # Charger la première page
            page = pdf_document.load_page(0)
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # haute résolution

            # Convertir en image Pillow
            image = Image.open(BytesIO(pix.tobytes("png")))
            buffer = BytesIO()
            image.save(buffer, format="PNG")

            # Nom du fichier image
            image_name = f"{instance.titre}_cover.png".replace(" ", "_")

            # Sauvegarde dans le champ cover_image
            instance.cover_image.save(image_name, ContentFile(buffer.getvalue()), save=False)
            instance.save(update_fields=['cover_image'])

            pdf_document.close()
        except Exception as e:
            print("Erreur lors de la génération de la couverture :", e)
