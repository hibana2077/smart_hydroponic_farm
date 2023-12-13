# Build ubuntu core image

## Requirements

- Ubuntu Operating System
- Micro SD card (8GB or more)
- Ubuntu One account
- Raspberry Pi 3

## Steps

1. Install snapcraft

    ```bash
    sudo apt install snapcraft
    ```

2. Login to Ubuntu One

    ```bash
    snapcraft login
    ```

3. Clone the assertion json file

    ```bash
    wget -O my-model.json https://raw.githubusercontent.com/snapcore/models/master/ubuntu-core-20-pi-arm64.json
    ```

4. Customize the assertion json file

    ```bash
    nano my-model.json
    ```
    - Change the `authority-id` to your Snap account-id
    - Change the `brand-id` to your Snap account-id</br>
    **Note:** You can find your account-id by running `snap whoami`

5. Create a Key

    - Check if you have a key

        ```bash
        snapcraft keys
        ```

    - If you don't have a key, create one

        ```bash
        snapcraft create-key <name>
        ```

6. Register the key

    - Register the key

        ```bash
        snapcraft register-key <name>
        ```
    
    - Check if the key is registered

        ```bash
        snapcraft keys
        ```

7. Update timestamp

    ```bash
    date -Iseconds --utc
    ```
    - Copy the output and paste it in the `timestamp` field of the assertion json file

    
8. Sign the assertion json file

    ```bash
    snap sign -k <name> my-model.json > my-model.model
    ```

9. Build the image

    - Download the ubuntu-image tool

        ```bash
        sudo snap install ubuntu-image --classic
        ```

    - Build the image

        ```bash
        ubuntu-image snap -O my-model.img my-model.model
        ```

    - Verify the image

        ```bash
        sudo apt-get install binutils-arm-linux-gnueabi
        arm-linux-gnueabi-objdump -D -b binary -marm my-model.img/pi.img > test.txt
        ```
        - Check if the output is asm code

10. Flash the image

    you can use [balenaEtcher](https://www.balena.io/etcher/) to flash the image to the SD card

    --燒錄要等開發版送到才能測試--