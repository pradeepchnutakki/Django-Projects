from django.shortcuts import render
from django.http import JsonResponse
from .models import Branch

def simulate_tree(request):
    # Grow logic (if grow=1 in URL)
    return render(request, "simulation/tree.html")

def tree_data(request):
    data = {
        "branches": [
            {
                "id": branch.id,
                "fruits": [
                    {
                        "size": fruit.size,
                        "ripeness": fruit.ripeness
                    } for fruit in branch.fruit_set.all()
                ]
            }
            for branch in Branch.objects.all()
        ]
    }
    return JsonResponse(data)
