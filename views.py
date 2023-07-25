from django.http import JsonResponse
from django.shortcuts import render, redirect
import json

def page_builder(request):
    components = PageComponent.objects.all()
    choices = PageComponent.COMPONENT_TYPES
    return render(request, 'front/page_builder.html', {'components': components, 'choices': choices,})

def save_components(request):
    if request.method == 'POST':
        components_json = request.POST.get('components', '[]')
        components = json.loads(components_json)

        # Save the components to the database
        for component_data in components:
            component_type = component_data.get('type')
            content = component_data.get('content')
            order = component_data.get('order')

            # Assuming PageComponent model has a field named 'component_type'
            # and 'content' to store the component type and content.
            PageComponent.objects.create(component_type=component_type, content=content, order=order)

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'})
