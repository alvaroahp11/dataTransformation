from django.contrib import admin
from django import forms
from .models import CreateCBSStructure, CreateEstimate
from django.http import FileResponse
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile

# Register your models here

class AbstractFileUploaderAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['file']})
    ]

    def process_file(self, uploaded_file):
        return uploaded_file

    def changelist_view(self, request, extra_context=None):
        """Redirect to the add view instead of showing the list view"""
        return self.add_view(request)       

    def add_view(self, request, form_url='', extra_context=None):
        """
        Handle file upload directly in the admin interface and return it for download.
        """
        if request.method == "POST":
            uploaded_file = request.FILES.get('file')
            if uploaded_file:
                new_file = self.process_file(uploaded_file)
                return self.file_download_response(new_file)

        return super().add_view(request, form_url, extra_context)

    def file_download_response(self, uploaded_file):
        """
        Return a FileResponse for the uploaded file without saving it to the database.
        """
        if isinstance(uploaded_file, (InMemoryUploadedFile, TemporaryUploadedFile)):
            # Create a FileResponse from the uploaded file
            response = FileResponse(uploaded_file)
            response['Content-Disposition'] = f'attachment; filename="{uploaded_file.name}"'
            return response

        raise ValueError("Invalid file type received.")


@admin.register(CreateCBSStructure)
class CreateCBSStructureAdmin(AbstractFileUploaderAdmin):
    pass

    
@admin.register(CreateEstimate)
class CreateEstimateAdmin(AbstractFileUploaderAdmin):
    pass

