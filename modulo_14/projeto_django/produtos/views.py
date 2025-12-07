from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from django.core.paginator import Paginator

# LISTAR
def lista_produtos(request):
    busca = request.GET.get('q', '')

    # Filtrar por nome se tiver busca
    if busca:
        produtos = Produto.objects.filter(nome__icontains=busca)
    else:
        produtos = Produto.objects.all()

    # Paginação (5 por página)
    paginator = Paginator(produtos, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'produtos/lista.html', {
        'page_obj': page_obj,
        'busca': busca
    })
# CRIAR
def criar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')

        Produto.objects.create(
            nome=nome,
            descricao=descricao,
            preco=preco,
            quantidade=quantidade
        )
        return redirect('lista_produtos')

    return render(request, 'produtos/form.html')

# EDITAR
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == 'POST':
        produto.nome = request.POST['nome']
        produto.descricao = request.POST['descricao']
        produto.preco = request.POST['preco']
        produto.quantidade = request.POST['quantidade']
        produto.save()
        return redirect('lista_produtos')

    return render(request, 'produtos/form.html', {'produto': produto})

# EXCLUIR
def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('lista_produtos')
