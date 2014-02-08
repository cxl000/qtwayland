#!/bin/sh
for x in brcm_egl nogl xcomposite_egl; do
	cp qtwayland.spec qtwayland-$x.spec
	sed -i "s/wayland_egl$/$x/g" qtwayland-$x.spec
done
