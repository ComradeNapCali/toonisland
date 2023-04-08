from panda3d.core import VirtualFileSystem, ConfigVariableList, Filename

if __debug__:
    from panda3d.core import loadPrcFile
    loadPrcFile('dependencies/panda3d/general.prc')
    loadPrcFile('dependencies/panda3d/dev.prc')
else:
    import sys
    sys.path = ['']

# The VirtualFileSystem, which has already initialized, doesn't see the mount
# directives in the panda3d(s) yet. We have to force it to load those manually:
vfs = VirtualFileSystem.getGlobalPtr()
mounts = ConfigVariableList('vfs-mount')
for mount in mounts:
    mountFile, mountPoint = (mount.split(' ', 2) + [None, None, None])[:2]
    vfs.mount(Filename(mountFile), Filename(mountPoint), 0)

from toontown.launcher.TIAQuickLauncherLOCAL import TIAQuickLauncherLOCAL
launcher = TIAQuickLauncherLOCAL()
launcher.notify.info('Reached end of StartTIAQuickLauncher.py.')
