from django.urls import path, include
from django.contrib import admin
from jokersapp import views

urlpatterns=[
    path('',views.base, name='base'),
    path('',views.home, name='home'),
    path('articulo/',views.ArticuloListView.as_view(), name='articulo-lista'),
    path('cliente/',views.ClienteListView.as_view(), name='cliente-lista'),
    path('factura/',views.FacturaListView.as_view(), name='factura-lista'),
    path('detalle/',views.DetalleListView.as_view(), name='detalle-lista'),
    path('proveedor/',views.ProveedorListView.as_view(), name='proveedor-lista'),
    path('compra/',views.CompraListView.as_view(), name='compra-lista'),
    path('nfactura/',views.FacturaCreate.as_view(),name='nfactura'),
    path('narticulo/',views.ArticuloCreate.as_view(),name='narticulo'),
    path('ncliente/',views.ClienteCreate.as_view(),name='ncliente'),
    path('ndetalle/',views.DetalleCreate.as_view(),name='ndetalle'),
    path('nproveedor/',views.ProveedorCreate.as_view(),name='nproveedor'),
    path('ncompra/',views.CompraCreate.as_view(),name='ncompra'),
    
    #path('category/',views.category,name='category-list'),
    #path('category/<int:category_id>/detail/',views.category_detail, name='category-detail'),
    #path('photo/',views.PhotoListView.as_view(), name='photo-list'),
    #path('photo/<int:pk>/detail/', views.PhotoDetailView.as_view(), name='photo-detail'),
    #Update
    #path('photo/<int:pk>/update',views.PhotoUpdate.as_view(), name='photo-update'),
    #Create
    #path('photo/create',views.PhotoCreate.as_view(), name='photo-create'),
    #Delete
    #path('photo/<int:pk>/delete',views.PhotoDelete.as_view(), name='photo-delete'),
    #path('accounts/', include('registration.backends.default.urls')),
    
]