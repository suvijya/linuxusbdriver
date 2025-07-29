# linuxusbdriver

### **Part 1: Prerequisites & Setup**

Before running either script, you need to ensure your system has the necessary tools.

#### 1. Install `bindfs`
The `driver.sh` script depends on a tool called `bindfs`, which is not installed by default. You can install it from the official Ubuntu repositories.

Open a terminal and run:
```bash
sudo apt update
sudo apt install bindfs
```

#### 2. Save the Scripts
You need to save the code you provided into files.

*   **For `driver.sh`:**
    *   Open a text editor (like `nano` or Gedit).
    *   Copy and paste the shell script code into it.
    *   Save the file in your home directory as `driver.sh`.

*   **For `usbdriver.py`:**
    *   Open a text editor.
    *   Copy and paste the Python code into it.
    *   Save the file in your home directory as `usbdriver.py`.

### **Part 2: Running `driver.sh` (The Read-Only PDF Viewer)**

This script requires careful setup because you need to provide the correct device path for your USB drive.

#### Step 1: Make the Script Executable
In your terminal, give the script permission to be executed:
```bash
chmod +x driver.sh
```

#### Step 2: Find Your USB Device Name
This is the most critical step. The script uses `/dev/sdb1`, which is just an example. Your USB drive will likely have a different name.

1.  Plug in your USB drive.
2.  In the terminal, run the `lsblk` command (List Block Devices):
    ```bash
    lsblk
    ```
3.  Look at the output. You need to identify your USB drive, usually by its size. It might look something like this:

    ```
    NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
    sda           8:0    0 238.5G  0 disk 
    ├─sda1        8:1    0   512M  0 part /boot/efi
    └─sda2        8:2    0   238G  0 part /
    sdb           8:16   1  14.9G  0 disk 
    └─sdb1        8:17   1  14.9G  0 part /media/user/MyUSB
    ```
    In this example, the USB drive is `sdb` and its partition is `sdb1`. **Your drive might be `sdc1`, `sdd1`, etc.**

#### Step 3: Edit the Script
Now, you must replace the placeholder `/dev/sdb1` in the script with the actual partition name you found in the previous step.

1.  Open the script for editing: `nano driver.sh`
2.  Change this line:
    ```bash
    sudo mount /dev/sdb1 ~/usb_mount
    ```
    ...to match your device. For example, if your partition was `sdc1`, it would be:
    ```bash
    sudo mount /dev/sdc1 ~/usb_mount
    ```
3.  Save the file and exit the editor (in `nano`, press `Ctrl+X`, then `Y`, then `Enter`).

#### Step 4: Run the Script
Now you can execute the script.
```bash
./driver.sh
```
It will ask for your password because it uses `sudo`. After it runs, you can check the `~/pdf_only` directory. It should contain only the PDF files from your USB, and you will not be able to write or delete them.

#### Step 5: Unmounting When You're Done
When you are finished and want to safely eject the USB drive, you must unmount both locations:
```bash
sudo umount ~/pdf_only
sudo umount ~/usb_mount
```

---

### **Part 3: Running `usbdriver.py` (The PDF Copier)**

This script is generally safer as it doesn't require `sudo` and uses the mount path, which is more predictable.

#### Step 1: Find Your USB Mount Point
When Ubuntu automatically detects and mounts a USB drive, it places it in `/media/your_username/USB_LABEL`.

1.  Make sure your USB drive is plugged in.
2.  Use the `lsblk` command again as in Part 2, Step 2.
3.  Look for the `MOUNTPOINT` column for your USB partition. In the example above, it was `/media/user/MyUSB`.

#### Step 2: Edit the Script
You need to update the script with your specific username and the correct mount point.

1.  Open the script for editing: `nano usbdriver.py`
2.  Change this line:
    ```python
    usb_mount_path = '/media/yourusername/YourUSBLabel'
    ```
    ...to match the mount point you just found. For example:
    ```python
    usb_mount_path = '/media/user/MyUSB'
    ```
3.  Save the file and exit the editor.

#### Step 3: Create the Destination Folder
The script is set to copy files to a folder named `quarantine` in your home directory. Create it first:
```bash
mkdir -p ~/quarantine```

#### Step 4: Run the Script
Execute the Python script using the `python3` interpreter:
```bash
python3 usbdriver.py
```
You will see output in the terminal for each PDF file it successfully copies.

#### Step 5: Verify the Result
Check the contents of the `quarantine` folder to see your copied PDFs:
```bash
ls ~/quarantine
```