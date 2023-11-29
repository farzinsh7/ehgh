class FieldsMixin():
    def dispatch(self, request, *args, **kwargs):
        self.fields = ['title', 'title_fa', 'slug', 'description', 'description_fa', 'image', 'image_thumbnail', 'publish', 'status', 'keywords', 'keywords_fa', 'seo_description', 'seo_description_fa']

        return super().dispatch(request, *args, **kwargs)