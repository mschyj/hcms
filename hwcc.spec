# -*- mode: python -*-

block_cipher = None


a = Analysis(['elasticluster/__main__.py'],
             pathex=['.', '/root/hwcc-chenyjie', '/root/hwcc-chenyjie/elasticluster', '/root/hwcc-chenyjie/elasticluster/providers', '/usr/local/lib/python2.7', '/usr/local/lib/python2.7/site-packages', '/usr/local/lib/python2.7/site-packages/openstack', '/usr/local/lib/python2.7/site-packages/openstackclient', '/usr/local/lib/python2.7/site-packages/novaclient', '/usr/local/lib/python2.7/site-packages/novaclient/v2', '/usr/local/lib/python2.7/site-packages/glanceclient', '/root/hwcc'],
             binaries=[],
             datas=[('elasticluster', 'elasticluster')],
             hiddenimports=['packaging', 'packaging.version', 'packaging.specifiers', 'packaging.requirements', 'elasticluster.providers.openstack', 'novaclient', 'novaclient.v2', 'novaclient.v2.client', 'glanceclient.v2', 'cinderclient.v2'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='hwcc',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
