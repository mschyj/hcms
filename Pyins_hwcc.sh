rm -fr dist
rm -fr build
pyinstaller --paths=. \
            --paths=.:./elasticluster \
            --paths=./elasticluster/providers \
            --paths=/usr/local/lib/python2.7:/usr/local/lib/python2.7/site-packages \
            --paths=/usr/local/lib/python2.7/site-packages/openstack \
            --paths=/usr/local/lib/python2.7/site-packages/openstackclient \
            --paths=/usr/local/lib/python2.7/site-packages/novaclient \
            --paths=/usr/local/lib/python2.7/site-packages/novaclient/v2 \
            --paths=/usr/local/lib/python2.7/site-packages/glanceclient \
            --hidden-import=packaging \
            --hidden-import=packaging.version \
            --hidden-import=packaging.specifiers \
            --hidden-import=packaging.requirements  \
            --hidden-import=elasticluster.providers.openstack  \
            --hidden-import=novaclient \
            --hidden-import=novaclient.v2 \
            --hidden-import=novaclient.v2.client \
            --hidden-import=glanceclient.v2 \
            --hidden-import=cinderclient.v2 \
            --add-data="elasticluster:elasticluster" \
            --onefile \
            -n hwcc -y \
            ./elasticluster/__main__.py 
#cp -fr elasticluster ./dist/



#pyinstaller --clean \
#            --hidden-import=packaging \
#            --hidden-import=packaging \
#            --hidden-import=packaging.version \
#            --hidden-import=packaging.specifiers \
#            --hidden-import=packaging.requirements \
#            --hidden-import=novaclient \
#            --hidden-import=novaclient.client \
#            --hidden-import=novaclient.api_versions \
#              script/vm.py -y -F -d
