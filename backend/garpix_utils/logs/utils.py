from django.db.models import ManyToManyRel


def get_changed_fields(obj):
        old_obj = obj.__class__.objects.get(pk=obj.pk)
        changed_fields = {}
        fields = obj._meta.fields
        for field in fields:
            field_name = field.name
            if hasattr(obj, field_name):
                old_value = getattr(old_obj, field_name)
                new_value = getattr(obj, field_name)
                if old_obj and old_value != new_value:
                    changed_fields[field.verbose_name] = {
                        "old": old_value,
                        "new": new_value
                    }
        return changed_fields


def get_changed_m2m_fields(obj, old_obj_fields, exclude_fields=[]):
    changed_fields = {}
    for field in obj._meta.get_fields():
        field_name = field.name
        if field.many_to_many and hasattr(obj, field_name) and field_name not in exclude_fields:
            new_object_manager = getattr(obj, field_name)
            new_relations = set([str(_obj) for _obj in list(new_object_manager.all())])

            added = new_relations - old_obj_fields[field_name]
            removed = old_obj_fields[field_name] - new_relations

            if not (added or removed):
                continue

            key = f'{field.verbose_name}: ' if not isinstance(field, ManyToManyRel) else f'{field.field.verbose_name}: '
            changed_fields[key] = {
                "added": added,
                "removed": removed
            }

    return changed_fields