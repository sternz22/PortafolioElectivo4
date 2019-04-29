from django.db import models

class Home(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    under_title = models.CharField(max_length=200, verbose_name="Sub Título")
    image = models.ImageField(upload_to="projects", verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Inicio"
        verbose_name_plural = "Inicio"
        ordering = ["-created"]

    def __str__(self):
        return self.title


class About(models.Model):
    titleAbout = models.CharField(max_length=200, verbose_name="Título")
    nameAbout = models.CharField(max_length=200, verbose_name="Nombre")
    headerAbout = models.CharField(max_length=200, verbose_name="Cabeza")
    descriptionAbout = models.TextField(verbose_name="Descripción")
    descriptionDosAbout = models.TextField(verbose_name="Descripción dos", blank="true", null="true")
    under_titleAbout = models.CharField(max_length=200, verbose_name="Sub Título")
    imageAbout = models.ImageField(upload_to="projects", verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"
        ordering = ["-created"]

    def __str__(self):
        return self.titleAbout

class Contact(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    descriptionDos = models.TextField(verbose_name="Descripción Dos")
    descriptionTres = models.TextField(verbose_name="Descripción Tres")
    descriptionCuatro = models.TextField(verbose_name="Descripción Cuatro")
    subDescripcionDos = models.TextField(verbose_name="Sub Descripción Dos")
    subDescripcionTres = models.TextField(verbose_name="Sub Descripción Tres")
    subDescripcionCuatro = models.TextField(verbose_name="Sub Descripción Cuatro")
    under_title = models.CharField(max_length=200, verbose_name="Sub Título")
    image = models.ImageField(upload_to="projects", verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact"
        ordering = ["-created"]

    def __str__(self):
        return self.title

class Social(models.Model):
    title = models.CharField(max_length=200, verbose_name="Títulos")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to="projects",  verbose_name="Imagen")
    link = models.URLField(null=True, blank=True, verbose_name="Dirección Web")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Social"
        ordering = ["-created"]

    def __str__(self):
        return self.title
    
class Red(models.Model):
    title = models.CharField(max_length=200, verbose_name="Títulos")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to="projects",  verbose_name="Imagen")
    link = models.URLField(null=True, blank=True, verbose_name="Dirección Web")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Social"
        ordering = ["-created"]

    def __str__(self):
        return self.title