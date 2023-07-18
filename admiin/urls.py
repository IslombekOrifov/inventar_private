from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', Admin_index, name='admin-index'),
    path('unknown-devices', Unknown_Devices, name='unknown-devices'),
    path('category-create/excel-file', UploadExcelFile, name='create-by-excel'),
    path('index/base/<int:pk>', baseview, name='base-view'),
    path('index/base/<int:pk>/add-equipment', EquipmentCreateView, name='equipment-create'),
    path('add-equipments/excel', product_create_excel, name='equipment-create-excel'),
    path('index/base/<int:pk>/admin-detail-of-product/', ProductDetailView, name='product-detail'),
    path('index/base/<int:pk>/product-update', ProductUpdateView, name='product-update'),
    path('index/base/<int:pk>/product-delete', ProductDeleteView, name='product-delete'),
    # path('index/rooms-add', RoomsCreateView.as_view(), name='rooms-add'),
    path('index/model-create', ModelCreateView.as_view(), name='model-create'),
    path('search', SearchResultsView.as_view(), name='admin-search'),

    path('models', AdminModels, name='admin-models'),
    path('model-edit/<int:pk>', AdminModelEdit, name='model-edit'),
    path('model-delete/<int:pk>', AdminModelDelete, name='model-delete'),

    # category
    path('index/category-create', CategoryCreateView.as_view(), name='category-create'),
    path('categories', AdminCategories, name='admin-categories'),
    path('category-edit/<int:pk>', AdminCategoryEdit, name='category-edit'),
    path('category-delete/<int:pk>', AdminCategoryDelete, name='category-delete'),

    # rooms
    path('rooms', AdminRooms, name='admin-rooms'),
    path('rooms/floor/<int:pk>', AdminRoomFloor, name='admin-rooms-floors'),
    path('room-detail/<str:slug>', AdminRoomDetail, name='admin-room-details'),

    # departments
    path('department/', department_list, name='department-list'),
    path('department-delete/<int:pk>/', AdminDepartmentDelete, name='department-delete'),
    path('department/edit/<int:pk>/', department_edit, name='department-edit'),
    path('department/create', DepartmentCreateView.as_view(), name='department-create'),

    # responsible admin
    path('responsibles/<int:pk>/', AdminResponsibles, name='admin-responsibles'),
    path('index/responsible-create/<int:pk>/', ResponsibleCreateView.as_view(), name='responsible-create'),
    path('index/responsible-create/', ResponsibleCreateView.as_view(), name='responsible-create-noid'),
    path('responsible-edit/<int:pk>/', AdminResponsibleEdit, name='responsible-edit'),
    path('responsible/password/<int:pk>/', responsible_password_change, name='responsible_pass_change'),
    path('responsible-delete/<int:pk>', AdminResponsibleDelete, name='responsible-delete'),
    path('responsible/<int:pk>/products', AdminResponsibleProducts, name='responsible-index'),

    # profile
    path('profile/password/', password_change, name='pass_change'),
    path('profile/', profile_edit, name='profile_edit'),

    # responsible user
    path('responsible/index/base/', responsible_baseview, name='responsiblepage-index'),
    path('responsible/index/my/', responsible_myproduct, name='responsiblepage-myproducts'),
    path('responsible/application/', responsible_application, name='responsiblepage-application'),
    path('responsibles/', AdminResponsibles, name='responsiblepage-liderrespon'),

    # actions
    path('actions/all/', actions_view, name='actions-all'),

    path('building', test),
]
