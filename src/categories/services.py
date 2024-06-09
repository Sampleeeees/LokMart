"""Categories service."""

from django.db.models import QuerySet
from django.http import HttpRequest

from src.categories.exceptions import CategoryListNotFoundExceptionError
from src.categories.exceptions import CategoryNotFoundByIdExceptionError
from src.categories.exceptions import CategoryNotFoundExceptionError
from src.categories.models import Category
from src.categories.schemas import CategorySchema


class CategoryService:
    """Category service class."""

    @staticmethod
    def category_schema(request: HttpRequest, categories: QuerySet[Category]) -> list[CategorySchema]:
        """Parse queryset category to CategorySchema.

        :param request: HttpRequest
        :param categories: Queryset of category model.

        :return: Parsed CategorySchema list.

        """
        host = request.build_absolute_uri("/")
        return [
            CategorySchema(id=category.pk, name=category.name, image=host + category.image.url)
            for category in categories
        ]

    def get_categories(self, request: HttpRequest) -> list[CategorySchema]:
        """Get all categories.

        :return: List of categories.
        """
        categories: QuerySet[Category] = Category.objects.all()
        if not categories:
            raise CategoryListNotFoundExceptionError
        return self.category_schema(request, categories)

    def find_category_by_name(self, request: HttpRequest, name: str):
        """Find category by name.

        :param request: HttpRequest.
        :param name: Name category(str)

        :return: Category object or None
        """
        if categories := Category.objects.search_categories_by_name(name=name):
            return self.category_schema(request=request, categories=categories)
        raise CategoryNotFoundExceptionError(message=f"Category by name {name} not found")

    @staticmethod
    def get_category_by_id(request: HttpRequest, category_id: int) -> CategorySchema | None:
        """Get category by category_id.

        :param request: HttpRequest object.
        :param category_id: category id. (int)

        :return: CategorySchema or None
        """
        if category := Category.objects.filter(pk=category_id).first():
            return CategorySchema(
                id=category.pk, name=category.name, image=request.build_absolute_uri(category.image.url)
            )
        raise CategoryNotFoundByIdExceptionError(message=f"The category not found by number id {category_id}.")
