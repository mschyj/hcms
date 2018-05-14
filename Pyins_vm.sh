rm -fr dist
rm -fr build
pyinstaller --clean \
            --hidden-import=packaging \
            --hidden-import=packaging \
            --hidden-import=packaging.version \
            --hidden-import=packaging.specifiers \
            --hidden-import=packaging.requirements \
            --hidden-import=novaclient \
            --hidden-import=novaclient.client \
            --hidden-import=novaclient.api_versions \
            script/vm.py -y -F -d 
