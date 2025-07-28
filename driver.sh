
mkdir -p ~/usb_mount
mkdir -p ~/pdf_only

# Replace /dev/sdb1 with your actual USB partition
sudo mount /dev/sdb1 ~/usb_mount

# Only bind PDF files
bindfs --perms=a-w --create-forbidden=outside ~/usb_mount ~/pdf_only --exclude='.*' --include='.*\.pdf'
