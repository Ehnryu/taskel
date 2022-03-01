@function clean:
rm -rf dist
rm -rf taskel.egg-info
\endfunc

@function build:
@q python -m pip install --upgrade build
@q python -m pip install --upgrade twine
@q python -m build
\endfunc

@function upload:
python3 -m twine upload --repository pypi dist/*
\endfunc
