from django import views
from django.urls import path
from django.urls.conf import include

from bio.views import bio, education, experience, portfolio, skills, services

urlpatterns = [
    path("bio/", bio.ListCreateBioAPIView.as_view()),
    path("bio/<int:pk>/", bio.RetrieveUpdateDestroyBioAPIView.as_view()),
    path("education/", education.ListCreateEducationAPIView.as_view()),
    path(
        "education/<int:pk>/",
        education.RetrieveUpdateDestroyEducationAPIView.as_view(),
    ),
    path("experience/", experience.ListCreateExperienceAPIView.as_view()),
    path(
        "experience/<int:pk>/",
        experience.RetrieveUpdateDestroyExperienceAPIView.as_view(),
    ),
    path("portfolio/", portfolio.ListCreatePortfolioAPIView.as_view()),
    path(
        "portfolio/<int:pk>/",
        portfolio.RetrieveUpdateDestroyPortfolioAPIView.as_view(),
    ),
    path("skills/", skills.ListCreatePortfolioAPIView.as_view()),
    path(
        "skills/<int:pk>/",
        skills.RetrieveUpdateDestroyPortfolioAPIView.as_view(),
    ),
    path("services/", services.ListCreatePortfolioAPIView.as_view()),
    path(
        "services/<int:pk>/",
        services.RetrieveUpdateDestroyPortfolioAPIView.as_view(),
    ),
]
