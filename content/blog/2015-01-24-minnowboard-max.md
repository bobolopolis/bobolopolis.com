Title: Gentoo on a Minnowboard MAX
Date: 2015-01-24 04:53
Modified: 2016-03-17 22:57
Category: blog
Tags: gentoo, linux, minnowboard
Authors: bobolopolis
Summary: Installing Gentoo on a Minnowboard MAX

<!--- #date: 04:53 01/24/2015 # UTC
--->

A few months ago, I purchased a [Minnowboard MAX](http://www.minnowboard.org/)
to replace a Raspberry Pi that was a bit short on horsepower. Its been running
Ubuntu happily, but I decided that it really needed to be running my favorite
distro: Gentoo. It took more effort than I expected to get it working, so here
are my notes in case anyone else is having trouble (and for my own future
reference...).

The higher spec Minnowboard MAX has an Intel Atom E3825 processor, which is a
standard 64 bit x86 processor. One catch with this particular board, however,
is that legacy BIOS is not supported. It's UEFI or bust. This isn't a big deal,
but it does change the usual Gentoo install process. In particular, I could not
get the normal minimal Gentoo install ISO to boot. I ended up using
[SystemRescueCd](http://www.sysresccd.org) to boot the board into a Linux
environment. SystemRescueCd is also Gentoo based, so its trivial to use it as a
starting point to install Gentoo.

#Initial Boot
As of version 4.1.1, the standard kernel for SystemRescueCd (version 3.10)
cannot boot the Minnowboard MAX. Selecting the alternate kernel (version 3.14)
does work fine. From here on, the install process is pretty normal. For me, the
SD card showed up as /dev/mmcblk0 and my SystemRescueCd USB drive was /dev/sda.

#SD Card Partitioning
The following is the partition layout that I used. Note that UEFI requires the
boot partition to be formatted with the FAT file system.

    GNU Parted 3.2
    Using /dev/mmcblk0
    Welcome to GNU Parted! Type 'help' to view a list of commands.
    (parted) p
    Model: SD SD (sd/mmc)
    Disk /dev/mmcblk0: 64.8GB
    Sector size (logical/physical): 512B/512B
    Partition Table: gpt
    Disk Flags:

    Number  Start   End     Size    File system     Name    Flags
     1      1049kB  3146kB  2097kB  fat32           grub    bios_grub
     2      3146kB  137MB   134MB   fat16           boot    boot, esp
     3      137MB   2285MB  2147MB  linux-swap(v1)  swap
     4      2285MB  64.8GB  62.5GB  btrfs           rootfs

I did deviate slightly from the standard file system layout in that my boot
partition is not mounted at /boot. The boot partition is at /boot/efi. The
following is my /etc/fstab for reference (note that not all SD cards support
the discard flag).

    /dev/mmcblk0p2          /boot/efi       vfat    defaults,noatime        1 2
    /dev/mmcblk0p3          none            swap    sw                      0 0
    /dev/mmcblk0p4          /               btrfs   discard,noatime         0 1

#Setting make.conf
When configuring make.conf, add the following line to make installing GRUB
easier:

    GRUB_PLATFORMS="efi-64"

Otherwise you'll get errors when trying to install GRUB to the SD card later.

#Configuring GRUB
This turned out to be the hardest part of the install. Every time I booted the
board after installing everything, I'd get a kernel panic saying that the root
file system device didn't exist. I assumed this was due to missing a driver in
the kernel, but nothing worked. I even tried using the same kernel
configuration as SystemRescueCD with an initramfs, which obviously could boot
correctly since I used it for the install, but still got the same kernel panic.
After hours of searching with trial and error, I came across
[this post](http://forums.gentoo.org/viewtopic-p-7671340.html#7671340)
regarding similar embedded board. The point mentioned in that post is to tell
GRUB to add a delay.

It seems that the kernel is loading too fast and the SD card is not yet
initialized when the kernel attempts to mount the root file system. The
solution mentioned in the post is to add a delay to GRUB. After emerging
GRUB, edit the file /etc/default/grub and add the line "rootdelay=8" to the
GRUB_CMDLINE_LINUX_DEFAULT option. Then continue with installing GRUB to the
SD card.

    GRUB_CMDLINE_LINUX_DEFAULT="rootdelay=8"

The choice of eight seconds is arbitrary and I'm sure a lower value could be
used with some experimentation.

With Gentoo up and running, I'm quite impressed with the the performance of the
dual core Minnowboard MAX. It's usually faster than the old Athlon 64 2600+
I use to run this and a few other websites.
