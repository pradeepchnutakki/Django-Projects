#from django.shortcuts import render
#from django.http import JsonResponse
#from .models import Branch

#def simulate_tree(request):
#    # Grow logic (if grow=1 in URL)
#    return render(request, "simulation/tree.html")

from django.shortcuts import render, redirect
from .models import Branch, Fruit
import random

def simulate_tree(request):
    if request.GET.get("grow") == "1":
        # Step 1: Clear old data
        Fruit.objects.all().delete()
        Branch.objects.all().delete()

        # Step 2: Create new tree data
        for i in range(3):  # e.g., 3 branches
            branch = Branch.objects.create()
            for j in range(random.randint(1, 3)):
                Fruit.objects.create(
                    branch=branch,
                    size=random.randint(1, 5),
                    ripeness=random.randint(0, 100)
                )
        return redirect("/")  # reload the main page

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
