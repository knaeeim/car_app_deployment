from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.decorators import login_required

# Create your views here.
class AddCarView(CreateView):
    model = CarModel
    form_class = CarModelForm
    template_name = 'add_car.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Car added successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Add Car'
        return context
    
class AddBrandView(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = "add_car.html"
    success_url = reverse_lazy('addBrand')

    def form_valid(self, form):
        messages.success(self.request, 'Brand added successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = "Add Brand"
        return context
    
class EditCarView(UpdateView):
    model = CarModel
    form_class = CarModelForm
    template_name = 'add_car.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        messages.success(self.request, 'Car updated successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Edit Car'
        return context

class EditBrandView(UpdateView):
    model = Brand
    form_class = BrandForm
    template_name = 'add_car.html'
    success_url = reverse_lazy('home') 
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        messages.success(self.request, 'Brand updated successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Edit Brand'
        return context
    

def details_post_view(request, id):
    # Get the car object or return a 404 error if not found
    car = get_object_or_404(CarModel, id=id)

    # Handle POST request for submitting a comment
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = car  # Assign the car object to the comment
            new_comment.save()
            messages.success(request, "Comment added successfully")
            return redirect('show_details', id=id)  # Redirect to the same page to show the updated comments list
    else:
        form = CommentForm()

    # Fetch the comments related to the current car
    comments = Comment.objects.filter(post=car)

    # Prepare context for the template
    context = {
        'car': car,
        'comments': comments,
        'form': form,
    }

    return render(request, 'show_details.html', context)

class DetailsPostView(DetailView):
    model = CarModel
    template_name = "show_details.html"
    pk_url_kwarg = 'id'

    def post(self, request, *args, **kwargs):
        form = CommentForm(self.request.POST)
        post = self.get_object()
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post # Assign the post to the comment
            new_comment.save()
            messages.success(self.request, "Comment added successfully")
        return self.get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        form = CommentForm()
        context['comments'] = comments
        context['form'] = form
        return context

@login_required
def buy_now(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    car = CarModel.objects.get(id=id)
    if car:
        if car.quantity <= 0:
            messages.warning(request, 'Car not available')
            return redirect('profile')
        car.quantity -=1 
        car.save()
        BuyNow.objects.create(car=car, user=request.user).save()
        messages.success(request, 'Car bought successfully')
        return redirect('profile')
   
    messages.error(request, 'Car not available')
    return redirect('profile')

def view_car_by_brand(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    cars = CarModel.objects.filter(brand=brand)
    all_brands = Brand.objects.all()  # Get all brands for display
    return render(request, 'brand.html', {'brand': brand, 'cars': cars, 'all_brands': all_brands})