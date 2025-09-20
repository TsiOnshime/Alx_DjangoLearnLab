from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required, login_required
from .models import Document
from django.views import View

@permission_required('users.can_view', raise_exception=True)
def document_list(request):
    docs = Document.objects.all()
    return render(request, 'document_list.html', {'documents': docs})

@permission_required('users.can_create', raise_exception=True)
def document_create(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Document created!")
    else:
        form = DocumentForm()
    return render(request, 'document_form.html', {'form': form})

@permission_required('users.can_edit', raise_exception=True)
def document_edit(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    return HttpResponse(f"Edit document {doc.title}")

@permission_required('users.can_delete', raise_exception=True)
def document_delete(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    return HttpResponse(f"Delete document {doc.title}")

class RegisterView(View):
    def get(self, request):
        return HttpResponse("Register page")

class ProfileView(View):
    def get(self, request):
        return HttpResponse("Profile page")