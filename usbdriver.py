import os
import shutil

usb_mount_path = '/media/yourusername/YourUSBLabel'
destination_folder = os.path.expanduser('~/quarantine')

for root, dirs, files in os.walk(usb_mount_path):
	for file in files:
    	if file.lower().endswith('.pdf'):
        	src = os.path.join(root, file)
        	dst = os.path.join(destination_folder, file)
        	try:
            	shutil.copy2(src, dst)
            	print(f"Copied {src} to {dst}")
        	except Exception as e:
            	print(f"Failed to copy {file}: {e}")
