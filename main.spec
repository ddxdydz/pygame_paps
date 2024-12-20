# -*- mode: python ; coding: utf-8 -*-

added_files = [
    ('data/imgs/icon/icon.ico','data/imgs/icon'),
    ('data/imgs/icon/icon.png','data/imgs/icon'),
    ('data/imgs/menu_imgs/menu_background.jpg', 'data/imgs/menu_imgs'),
    ('data/imgs/game_imgs/other/*.png', 'data/imgs/game_imgs/other'),
    ('data/scene2/imgs/map/game_map.jpg', 'data/scene2/imgs/map'),
    ('data/scene2/imgs/player/*.png', 'data/scene2/imgs/player'),
    ('data/scene2/imgs/enemy/*.png', 'data/scene2/imgs/enemy'),
    ('data/audio/sound/*.wav', 'data/audio/sound')
]
a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['data\\imgs\\icon\\icon.ico'],
)
