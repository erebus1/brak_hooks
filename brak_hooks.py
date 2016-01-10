def isort_hook(ui, repo, hooktype, node, **kwargs):
    try:
        import isort
    except ImportError:
        ui.warn('install isort (outside virtual env) to run this hook')
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
