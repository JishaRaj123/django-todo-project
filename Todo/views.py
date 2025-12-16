from django.shortcuts import render,redirect,HttpResponse
from . forms import Todoforms
from .models import Todo

# Create your views here.
def todo(request):
    form=Todoforms()
    todos=Todo.objects.all()
    context={
        'forms': form,
        'todos' : todos
    }

    if request.method=='POST':
        form=Todoforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    return render(request,'todos.html',context)


def delete(request,id):
    # display 1 details
    todo=Todo.objects.get(id=id)

    if request.method=='POST':
        todo.delete()
        return redirect('todo')
    
    # print(id) to print id on console
    # return HttpResponse("Its delete Page")

def update(request,id):
    todo=Todo.objects.get(id=id)
    form=Todoforms(instance=todo)

    context={
        'form': form,
        'todo': todo
    }
    if request.method=='POST':
        form=Todoforms(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo')

    return render(request,'updatetodo.html',context)







# first step
# def todo(request):
    # return render(request,'todos.html')


# forms add 2nd step
# def todo(request):
#     form=Todoforms()

#     context={
#         'forms': form
#     }
#     return render(request,'todos.html',context)





# see deatils in admin panel
# def todo(request):
#     form=Todoforms()

#     context={
#         'forms': form
#     }

#     if request.method=='POST':
#         form=Todoforms(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request,'todos.html',context)
#     return render(request,'todos.html',context)




# redirecting many tyms

#          return render(request,'todos.html',context)
#     return render(request,'todos.html',context)



