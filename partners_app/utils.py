def add_image_to_model(image, image_model, parent_instance, parent_instance_id):
    new_image = image_model()
    setattr(new_image, parent_instance, parent_instance_id)
    new_image.image = image
    new_image.save()


def get_data_to_field(form, model,  request):
    data = {k:v for k, v in request.POST.items() if k not in ['csrfmiddlewaretoken', 'submit']}
    new_form = form(data=data)
    if new_form.is_valid():
        new_element = new_form.save()
        new_element_id = new_element.id
        new_element_name = str(new_element.__str__).split(':')[1].lstrip()[:-2]
        print(new_element_name)
    else:
        print(new_form)
    return {'new_element_id': new_element_id, 'new_element_name': new_element_name}