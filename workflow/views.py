from django.shortcuts import redirect, render

from .compatibility import ALL_FEATURE_SLUGS, BRANDS, FEATURE_GROUPS, evaluate_brands

_BRAND_NAMES = {b.slug: b.name for b in BRANDS}


def _get_selected(request) -> set[str]:
    raw = request.session.get("selected_features", [])
    if not isinstance(raw, list):
        return set()
    return {s for s in raw if s in ALL_FEATURE_SLUGS}


def _set_selected(request, slugs: list[str]) -> None:
    request.session["selected_features"] = [s for s in slugs if s in ALL_FEATURE_SLUGS]


def welcome(request):
    return render(request, "workflow/welcome.html", {"active": "welcome"})


def features(request):
    selected = _get_selected(request)
    if request.method == "POST":
        keys = request.POST.getlist("feature")
        _set_selected(request, keys)
        return redirect("brands")
    ctx = {
        "feature_groups": FEATURE_GROUPS,
        "selected": selected,
        "active": "features",
    }
    return render(request, "workflow/features.html", ctx)


def brands(request):
    selected = _get_selected(request)
    rows = evaluate_brands(selected)
    ctx = {
        "brands": rows,
        "selected_count": len(selected),
        "selected": selected,
        "active": "brands",
    }
    return render(request, "workflow/brands.html", ctx)


def dashboard(request):
    selected = _get_selected(request)
    brand_slugs = request.GET.getlist("pick")
    picked = brand_slugs[:6]
    picked_labels = [_BRAND_NAMES.get(s, s.replace("_", " ").title()) for s in picked]
    ctx = {
        "selected": selected,
        "selected_count": len(selected),
        "picked_brands": picked,
        "picked_labels": picked_labels,
        "active": "dashboard",
    }
    return render(request, "workflow/dashboard.html", ctx)


def reset(request):
    request.session.flush()
    return redirect("welcome")
