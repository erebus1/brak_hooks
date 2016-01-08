def isort_hook(ui, repo, hooktype, node, pending, **kwargs):
    try:
        import isort
    except ImportError:
        ui.warn('You need the isort python module to use the isorthook')
        return True  # Failure

    errors = 0
    ctx = repo[node]
    if 'no-isort' in ctx.description():
        return 0

    for filename in ctx.files():
        attempt = isort.SortImports(file_path=filename, check=True)
        if attempt.incorrectly_sorted:
            errors += 1
    return errors
