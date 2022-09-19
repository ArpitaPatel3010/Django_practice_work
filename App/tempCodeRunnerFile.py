for k,v in request.POST.items():
        new_data = data["form_data"].setdefault(k,v)
        print(new_data)