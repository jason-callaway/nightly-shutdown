# nightly-shutdown
Nightly shutdown tool for AWS EC2 cost-control

## Why

When you've got lots of people working on the same AWS capacity, it's easy for
somebody to forget to spin down their instances when they're not in use. This
tool stops, but does not terminate, any instances in EC2 whose instance-id is
not in the whitelist in [nightly-shutdown.yml](nightly_shutdown.yml).

## How to use it

Run the following commands as root.

1. Ensure [boto](https://github.com/boto/boto) is installed.

    ```bash
    yum install -y python-pip
    pip install boto
    ```
2. Clone this repo

    ```bash
    git clone https://github.com/jason-callaway/nightly-shutdown
    ```
3. Put the [nightly-shutdown.yml](nightly_shutdown.yml) config file in 
```/etc```. Don't forget to change mode and ownership to root-only to protect 
your access and secret keys.

    ```bash
    cp nightly-shutdown/nightly-shutdown.yml /etc
    chown root:root /etc/nightly-shutdown.yml
    chmod 600 /etc/nightly-shutdown.yml
    ```
4. Add your access and secret keys to the config file. White list any instances
you'd like to opt-out of the nightly shutdown.

    ```yaml
    region: us-east-1
    access_key: eggseggseggseggs
    secret_key: spamspamspamspam
    whitelist:
      - i-abcdefgh
      - i-ijklmnop
    ```
5. Copy the [utility](nightly_shutdown.py) to cron.daily.

    ```bash
    cp nightly-shutdown/nightly-shutdown.py /etc/cron.daily/nightly-shutdown
    chmod 755 /etc/cron.daily/nightly-shutdown
    ```
