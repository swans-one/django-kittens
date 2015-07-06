from django.shortcuts import render_to_response

from .models import Kitten
from . import constants


def random_kitten_view(request, *args, **context):
    kitten = Kitten.objects.get_random()
    context['kitten'] = kitten
    context['kittens_home'] = constants.KITTEN_HOMEPAGE
    return render_to_response("kittens/random.html", context)


def kitten_up(request, *args, **context):
    kitten = Kitten.objects.get(id=context['id'])
    kitten.votes_up += 1
    kitten.save()
    context['kitten'] = kitten
    context['kittens_home'] = constants.KITTEN_HOMEPAGE
    return render_to_response("kittens/kitten_up.html", context)


def kitten_down(request, *args, **context):
    kitten = Kitten.objects.get(id=context['id'])
    kitten.votes_down += 1
    kitten.save()
    context['kitten'] = kitten
    context['kittens_home'] = constants.KITTEN_HOMEPAGE
    return render_to_response("kittens/kitten_down.html", context)


def top_kittens(request, *args, **context):
    top = Kitten.objects.extra(
        select={'net_score': 'votes_up - votes_down'}
    ).extra(where=['net_score > 0'], order_by=['-net_score'])[0:10]
    context['kittens'] = top
    context['kittens_home'] = constants.KITTEN_HOMEPAGE
    return render_to_response("kittens/top.html", context)
