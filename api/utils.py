def obj_to_post(obj, card=False):
    """
        card=True 이면 obj에 카드에 필요한 데이터만 담아보낸다
    """
    post = dict(vars(obj))
    print("::=>", post)
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
        post['image'] = "https://via.placeholder.com/900x300"

    if obj.created_at:
        post['created_at'] = obj.created_at.strftime("%Y-%m-%d %H:%M")
    else:
        post['created_at'] = "0000-00-00 00:00"

    if obj.updated_at:
        post['updated_at'] = obj.updated_at.strftime("%Y-%m-%d %H:%M")

    else:
        post['updated_at'] = "0000-00-00 00:00"

    del post['_state'], post['category_id']

    if card:
        del post['content'], post['updated_at'], post['description'], post['tags']

    return post


def prev_next_post(obj):
    try:
        next = obj.get_next_by_updated_at()
        nextPost = {
            "id": next.id,
            "title": next.title,
            "description": next.description
        }
    except obj.DoesNotExist:
        nextPost = {}
    try:
        prev = obj.get_previous_by_updated_at()

        prevPost = {
            "id": prev.id,
            "title": prev.title,
            "description": prev.description
        }

    except obj.DoesNotExist:
        prevPost = {}

    return prevPost, nextPost
