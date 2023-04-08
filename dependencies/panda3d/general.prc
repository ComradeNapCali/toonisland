# This is the PRC configuration file for settings that are
# used by both developer & production instances of Toon Island: Aftermath.

# Window settings
win-size 1280 720
win-origin -1 -1
load-display pandagl
audio-library-name p3openal_audio

# Notify settings
notify-level-collide warning
notify-level-chan warning
notify-level-gobj warning
notify-level-loader warning
notify-integrate false
notify-timestamp true
default-directnotify-level info

# Server settings
TIA-specific-login true

# Resources settings
# Art assets:
model-path /
default-model-extension .bam

# Display settings
depth-bits 24

# GUI settings
direct-wtext false
on-screen-debug-font AveriaSansLibre.ttf

# Chat settings
parent-password-set true
allow-secret-chat true
force-avatar-understandable true
force-player-understandable true

# Toon News settings
want-news-page false
want-news-tab false

# Gameplay settings
want-gardening true
want-cogdominiums true
want-emblems true

# Misc. settings
respect-prev-transform true
language english
vfs-case-sensitive false
inactivity-timeout 180
merge-lod-bundles false
early-event-sphere true
server-data-folder dependencies/astron/backups/
isclient-check false
