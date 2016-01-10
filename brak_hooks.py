import os


def isort_hook(ui, repo, hooktype, node, **kwargs):
    try:
        import isort
    except ImportError:
        ui.warn('install isort (outside virtual env) to run this hook')
        return True  # Failure

    if '3.9.5' < isort.__version__ < '4.2.3':
        if not os.environ.get('VIRTUAL_ENV'):
            ui.warn('isort_hook can only be run from CLI, with virtual env enabled\n\n')
            return True
    elif isort.__version__ >= '4.2.3':
        isort_config = isort.SortImports().config
        virtual_env = isort_config.get('virtual_env') or os.environ.get('VIRTUAL_ENV')
        if not virtual_env:
            ui.warn(
                'This hook requires you to either:\n\n'
                'a) set path to your virtualenv explicitly in isort settings [*], for example:\n'
                '# .isort.cfg'
                '[settings]\n'
                'virtual_env=/home/user/.pyenv/versions/2.7.10/envs/your_project\n\n'
                'b) be in a virtualenv, this will work only for CLI, not your repo tools or IDE\n\n'
                '[*] https://github.com/timothycrosley/isort/wiki/isort-Settings\n\n'
            )
            return True
    else:
        ui.warn('isort_hook requires isort>=3.9.5\n\n')
        return True
    ctx = repo[node]
    if 'no-isort' in ctx.description():
        return 0

    files_not_sorted = []
    for filename in ctx.files():
        attempt = isort.SortImports(file_path=filename, check=True)
        if attempt.incorrectly_sorted:
		    files_not_sorted.append(filename)
    if files_not_sorted:
	    ui.warn('%s\nneed to be isorted\n\n' % '\n'.join(files_not_sorted))
    return len(files_not_sorted)
