def obj_to_post(obj):
    post = dict(vars(obj))

    if obj.category:
        post['category'] = obj.category.name
    else:
        post['category'] = "none"

    if obj.tags:
        post['tags'] = [v.name for v in obj.tags.all()]

    else:
        post['tags'] = []

    if obj.image:
        post['image'] = obj.image.url
    else:
        post['image'] = "https://via.placeholder.com/900x400"

    if obj.create_at:
        post['create_at'] = obj.create_at.strftime("%Y-%m-%d %H:%M")
    else:
        post['create_at'] = "0000-00-00 00:00"

    if obj.update_at:
        post['update_at'] = obj.update_at.strftime("%Y-%m-%d %H:%M")

    else:
        post['update_at'] = "0000-00-00 00:00"

    del post['_state'], post['category_id']

    return post
