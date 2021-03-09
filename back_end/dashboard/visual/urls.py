from django.urls import path
from visual.views.common_views import index_view
from visual.views.marketing_views import (MarketingListView, MarketingDetailView, 
    MarketingAggregateView)
from visual.views.customer_views import (CustomerListView, CustomerDetailView, 
    CustomerAggregateView)
from visual.views.product_development_views import (ProductDevelopmentListView, 
    ProductDevelopmentDetailView, ProductDevelopmentAggregateView)
from visual.views.product_operation_views import (ProductOperationListView, 
    ProductOperationDetailView)
from visual.views.hr_views import HrListView, HrDetailView
from visual.views.profit_loss_views import (ProfitLossListView, ProfitLossDetailView, 
    ProfitLossAggregateView)



urlpatterns = [
    path('', index_view , name='index_view'),
    path('marketing/', MarketingListView.as_view(), name='marketing_list_view'),
    path('marketing/aggregate/', MarketingAggregateView.as_view(), name='marketing_aggregated_view'),
    path('marketing/<int:pk>/', MarketingDetailView.as_view(), name='marketing_detail_view'),
    path('customer/', CustomerListView.as_view(), name='customer_list_view'),
    path('customer/aggregate/', CustomerAggregateView.as_view(), name='customer_aggregated_view'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail_view'),
    path('product-development/', ProductDevelopmentListView.as_view(), name='product_development_list_view'),
    path('product-development/aggregate/', ProductDevelopmentAggregateView.as_view(), name='product_development_aggregated_view'),
    path('product-development/<int:pk>/', ProductDevelopmentDetailView.as_view(), name='product_development_detail_view'),
    path('product-operation/', ProductOperationListView.as_view(), name='product_operation_list_view'),
    path('product-operation/<int:pk>/', ProductOperationDetailView.as_view(), name='product_operation_detail_view'),
    path('hr/', HrListView.as_view(), name='hr_list_view'),
    path('hr/<int:pk>/', HrDetailView.as_view(), name='hr_detail_view'),
    path('profit-loss/', ProfitLossListView.as_view(), name='profit_loss_list_view'),
    path('profit-loss/aggregate/', ProfitLossAggregateView.as_view(), name='profit_loss_aggregated_view'),
    path('profit-loss/<int:pk>/', ProfitLossDetailView.as_view(), name='profit_loss_detail_view'),
]