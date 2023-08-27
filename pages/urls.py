from django.urls import path
from .views import (HomePageView, AboutPageView, ProductIndexView, 
                    ProductShowView, ProductCreateView, ProductCreateSuccessView, 
                    CartView, CartRemoveAllView, ImageViewFactory, ImageViewNoDI,
                    ImageBasicView, ImageNotDIView, ImageDIView
                    )
from .utils import ImageLocalStorage

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('products/product-created', ProductCreateSuccessView.as_view(), name='product-created'),
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'),
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'),
    path('image/', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_index'),
    path('image/save', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_save'),
    path('imagenotdi/', ImageViewNoDI.as_view(), name='imagenodi_index'),
    path('imagenotdi/save', ImageViewNoDI.as_view(), name='imagenodi_save'),
    path('imagebasic/', ImageBasicView.as_view(), name='imagebasic_index'),
    path('imagebasic/save', ImageBasicView.as_view(), name='imagebasic_save'),
    path('imagesnodi/', ImageNotDIView.as_view(), name='imagesnodi_index'),
    path('imagesnodi/save', ImageNotDIView.as_view(), name='imagesnodi_save'),
    path('imagesdi/', ImageDIView.as_view(), name='imagesdi_index'),
    path('imagesdi/save', ImageDIView.as_view(), name='imagesdi_save'),
]
