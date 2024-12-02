```sh
── 13:47:44 - Firmware upgrades ────────────────────────────────────────────────
Updating lvfs
Downloading…             [************************************** ]
Successfully downloaded new metadata: 1 local device supported
Devices with no available firmware updates:
 • CT4000T705SSD5
 • System Firmware
 • TPM
Alienware Alienware Aurora R15 AMD
│
└─UEFI dbx:
  │   Device ID:          snip
  │   Summary:            UEFI revocation database
  │   Current version:    262
  │   Minimum Version:    262
  │   Vendor:             UEFI:Linux Foundation
  │   Install Duration:   1 second
  │   GUID:               snip
  │   Device Flags:       • Internal device
  │                       • Updatable
  │                       • Supported on remote server
  │                       • Needs a reboot after installation
  │                       • Device is usable for the duration of the update
  │                       • Only version upgrades are allowed
  │                       • Signed Payload
  │
  └─Secure Boot dbx Configuration Update:
        New version:      371
        Remote ID:        lvfs
        Release ID:       35287
        Summary:          UEFI Secure Boot Forbidden Signature Database
        Variant:          x64
        License:          Proprietary
        Size:             21.2 kB
        Created:          2023-05-09
        Urgency:          High
        Tested by Lenovo:
          Tested:         2024-11-20
          Distribution:   fedora 39 (workstation)
          Old version:    217
          Version[fwupd]: 1.9.20
        Tested by Wistron:
          Tested:         2024-06-06
          Distribution:   ubuntu 22.04
          Old version:    267
          Version[fwupd]: 1.9.15
        Tested by HP:
          Tested:         2024-06-04
          Distribution:   fedora 39 (workstation)
          Old version:    77
          Version[fwupd]: 1.9.20
        Tested by HP:
          Tested:         2024-04-24
          Distribution:   ubuntu 22.04
          Old version:    83
          Version[fwupd]: 1.9.16
        Tested by HP:
          Tested:         2024-03-21
          Distribution:   fedora 39 (workstation)
          Old version:    217
          Version[fwupd]: 1.9.15
        Tested by Lenovo:
          Tested:         2024-02-20
          Distribution:   fedora 39 (workstation)
          Old version:    77
          Version[fwupd]: 1.9.5
        Tested by Lenovo:
          Tested:         2024-01-12
          Distribution:   fedora 39 (workstation)
          Old version:    220
          Version[fwupd]: 1.9.11
        Tested by DMC Group:
          Tested:         2023-07-11
          Distribution:   fedora 38 (workstation)
          Old version:    211
          Version[fwupd]: 1.9.2
        Tested by Jabra:
          Tested:         2023-07-03
          Distribution:   ubuntu 22.04
          Old version:    220
          Version[fwupd]: 1.9.3
        Vendor:           Linux Foundation
        Duration:         1 second
        Release Flags:    • Trusted metadata
                          • Is upgrade
        Description:
        Insecure versions of the Microsoft Windows boot manager affected by Black Lotus were added to the list of forbidden signatures due to a discovered security problem.This updates the dbx to the latest release from Microsoft.

        Before installing the update, fwupd will check for any affected executables in the ESP and will refuse to update if it finds any boot binaries signed with any of the forbidden signatures.Applying this update may also cause some Windows install media to not start correctly.
        Issue:            CVE-2022-21894
        Checksum:         fc3feb015df2710fcfa07583d31b5975ee398357016699cfff067f422ab91e13
```
