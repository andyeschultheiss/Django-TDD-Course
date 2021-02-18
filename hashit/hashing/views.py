from django.shortcuts import render, redirect
from .forms import HashForm
from .models import Hash
import hashlib
from django.http import JsonResponse

def home(request):
    if request.method == 'POST':
        filled_form = HashForm(request.POST)
        if filled_form.is_valid():
            text = filled_form.cleaned_data['text']
            text_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
            try:
                Hash.objects.get(hash_text=text_hash)
            except Hash.DoesNotExist:
                new_hash = Hash()
                new_hash.text = text
                new_hash.hash_text = text_hash
                new_hash.save()
            return redirect('hash', hash=text_hash)
    form = HashForm()
    return render(request, 'hashing/home.html', {'form': form})

def hash(request, hash):
    hash = Hash.objects.get(hash_text=hash)
    return render(request, 'hashing/hash.html', {'hash': hash})

def quickhash(request):
    text = request.GET['text']
    return JsonResponse({'hash': hashlib.sha256(text.encode('utf-8')).hexdigest()})