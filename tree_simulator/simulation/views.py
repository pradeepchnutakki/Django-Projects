from django.shortcuts import render
from .models import Tree, Branch

def simulate_tree(request):
    tree, _ = Tree.objects.get_or_create(name='My Tree')
    if tree.branches.count() == 0:
        for _ in range(3):
            tree.branches.add(Branch.objects.create())

    if request.GET.get("grow") == "1":
        tree.grow()

    context = {
        "tree": tree,
        "branches": tree.branches.all(),
    }
    return render(request, "simulation/tree.html", context)
