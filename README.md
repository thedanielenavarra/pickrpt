# PICKRPT

## _Definitions_

#### Message
Original user-typed text message or file
#### CMI
_The CMI (Coded Modulating Information) corresponds to the original information crypted based on the **key**_
#### CMF
_The CMF (Carrier Media File) is a media file choosen by the user (although it needs to match the constraints indicated by **pickrpt**) that will be edited in order to include the cyphered information_
#### MMF
_The MMF (Modulated Media File) is the final product of **pickrpt**: it's a media file containing the original cyphered information in a way that is "hidden" and not readable without **pickrpt** and the original **passphrase**_
#### Passphrase
_The passphrase is a string choosen by the user, needed to decrypt a MMF_
#### Key
_The key is the SHA512 digest of a passphrase choosen by the user, it can be represented as a series of variables and instructions that define the whole process_

# Process
![README](README.md)
