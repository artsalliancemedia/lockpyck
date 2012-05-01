"""
Unit tests for the Lockpick client module
"""
import unittest

from lockpyck import Lockpyck

# For unit testing only; this user doesn't exist in production. Seriously, don't even bother trying ...
_TESTHOST = 'https://localhost:3001'
_TESTUSER = 'test'
_TESTPASS = 'test'
        
# Test XML

_TESTKDM =\
"""
<?xml version="1.0" encoding="UTF-8" standalone="no" ?><DCinemaSecurityMessage xmlns="http://www.smpte-ra.org/schemas/430-3/2006/ETM" xmlns:dsig="http://www.w3.org/2000/09/xmldsig#" xmlns:enc="http://www.w3.org/2001/04/xmlenc#">
  <!-- Generated by Wailua Version 0.5.29 -->
  <AuthenticatedPublic Id="ID_AuthenticatedPublic">
    <MessageId>urn:uuid:4a8c103c-8d55-4cea-b665-b08d8053e576</MessageId>
    <MessageType>http://www.smpte-ra.org/430-1/2006/KDM#kdm-key-type</MessageType>
    <AnnotationText>COLD-SOULS_FTR_F_EN-ru_UK_51_2K_WRKS_20091006_AAM ~ KDM for SM.Dolby256-CAT862-0007ca4d</AnnotationText>
    <IssueDate>2012-03-29T13:35:38+00:00</IssueDate>
    <Signer>
      <dsig:X509IssuerName>dnQualifier=vVfvxXz1gOzEDwm2NoiJtcy4REQ=,CN=.192.168.254.3,OU=.cc-ra-1a.s430-2.ca.cinecert.com,O=.ca.cinecert.com</dsig:X509IssuerName>
      <dsig:X509SerialNumber>38981</dsig:X509SerialNumber>
    </Signer>
    <RequiredExtensions>
      <KDMRequiredExtensions xmlns="http://www.smpte-ra.org/schemas/430-1/2006/KDM">
        <Recipient>
          <X509IssuerSerial>
            <dsig:X509IssuerName>dnQualifier=4dl0oY64k/gzxFwgTB0eISmnFhg=,CN=.Cinea.MFGCA.1,O=DC256.Cinea.Com,OU=MFGCA1.DC256.Cinea.Com</dsig:X509IssuerName>
            <dsig:X509SerialNumber>2482</dsig:X509SerialNumber>
          </X509IssuerSerial>
          <X509SubjectName>dnQualifier=Gio9Szty8daEiFpFUVMv2uiackk=,CN=SM.Dolby256-CAT862-0007ca4d,O=DC256.Cinea.Com,OU=DolbyMediaBlock</X509SubjectName>
        </Recipient>
        <CompositionPlaylistId>urn:uuid:6b3f9ef8-f9c4-42b9-aff0-645cb0b11e06</CompositionPlaylistId>
        <ContentTitleText>COLD-SOULS_FTR_F_EN-ru_UK_51_2K_WRKS_20091006_AAM</ContentTitleText>
        <ContentKeysNotValidBefore>2009-01-01T00:00:00+00:00</ContentKeysNotValidBefore>
        <ContentKeysNotValidAfter>2012-12-31T00:00:00+00:00</ContentKeysNotValidAfter>
        <AuthorizedDeviceInfo>
          <DeviceListIdentifier>urn:uuid:6b08bf00-c13d-4c75-ae73-86a8ae34223c</DeviceListIdentifier>
          <DeviceList>
            <CertificateThumbprint>2jmj7l5rSw0yVb/vlWAYkK/YBwk=</CertificateThumbprint>
          </DeviceList>
        </AuthorizedDeviceInfo>
        <KeyIdList>
          <TypedKeyId>
            <KeyType>MDIK</KeyType>
            <KeyId>urn:uuid:b1569244-4fa8-481c-8ce3-647e37f09beb</KeyId>
          </TypedKeyId>
          <TypedKeyId>
            <KeyType>MDAK</KeyType>
            <KeyId>urn:uuid:235156e9-d20a-48a2-973c-1bbd4f45c272</KeyId>
          </TypedKeyId>
        </KeyIdList>
        <ForensicMarkFlagList>
          <ForensicMarkFlag>http://www.smpte-ra.org/430-1/2006/KDM#mrkflg-picture-disable</ForensicMarkFlag>
          <ForensicMarkFlag>http://www.smpte-ra.org/430-1/2006/KDM#mrkflg-audio-disable</ForensicMarkFlag>
        </ForensicMarkFlagList>
      </KDMRequiredExtensions>
    </RequiredExtensions>
    <NonCriticalExtensions/>
  </AuthenticatedPublic>
  <AuthenticatedPrivate Id="ID_AuthenticatedPrivate"><enc:EncryptedKey xmlns:enc="http://www.w3.org/2001/04/xmlenc#">
<enc:EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#rsa-oaep-mgf1p">
<ds:DigestMethod xmlns:ds="http://www.w3.org/2000/09/xmldsig#" Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/>
</enc:EncryptionMethod>
<enc:CipherData>
<enc:CipherValue>EFCJ2fPWlGsMMhhhEVCVt8WhbqbyCSMTiJn7UbM6QNBAs7JyVpPJ4BYQaED41gLEaictuttK1toA
Ipe9fALHsu/EvGIJB6Fq11me1tkk6lTS/dkccoLMBfW/O2Rn7flic9KHpH6a1Gu9yBra81LV4RRR
8UB61d20f+oHLH8pP4eUQAzFOLFX26bDZJfdwGAAHrjlAawauBtQgIeIaFupQSafa//Gnoz1t1kU
/OCGImHUVxgLcSllgJ8wobcY40UpqfQ270190XCsZyrkBhKNMYfgTa+6BPOgRIHGHy9m26anHj7R
I8+0xTjjexxXaTdbaled0Y+Wjp3eSuGHSL29oQ==</enc:CipherValue>
</enc:CipherData>
</enc:EncryptedKey><enc:EncryptedKey xmlns:enc="http://www.w3.org/2001/04/xmlenc#">
<enc:EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#rsa-oaep-mgf1p">
<ds:DigestMethod xmlns:ds="http://www.w3.org/2000/09/xmldsig#" Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/>
</enc:EncryptionMethod>
<enc:CipherData>
<enc:CipherValue>qZsCwmLMVPYsNxb9NFGown7gSa6vFbTK4UFuXoNUshwwIZj/kiffXlbrJrbgEXar62gZ6wchZ7PK
52qD+dyejNusukp15pfVUmR1UHBFLf0INv5vKOOgwNDg5vJ8bTu4Wr53Q9X901d/vfOlguHvrl5H
ZsGN5GRGzde2sGVebZVVmseUijnKwTgANtbeMUABWQ0ERokcUFsg1TTqXzH8n7IRWEwqok+9MWIj
QNe1zfhYg4Hn1bbJ5PxjXiLZgYb1ZDUweSxzdukw8qsXo+bZ2/g90zh69M4YEB2XPVF90zXi9IeF
7DsQbYfgY6+nsu7T6hisgEzT8RDlzIxCeUb+qg==</enc:CipherValue>
</enc:CipherData>
</enc:EncryptedKey></AuthenticatedPrivate>
  <dsig:Signature xmlns:dsig="http://www.w3.org/2000/09/xmldsig#">
    <dsig:SignedInfo>
      <dsig:CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments"/>
      <dsig:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>
      <dsig:Reference URI="#ID_AuthenticatedPublic">
        <dsig:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
        <dsig:DigestValue>gcTbgyszeLJFajnE/3lhYwEDT7p4d2iERBNJFXcssRA=</dsig:DigestValue>
      </dsig:Reference>
      <dsig:Reference URI="#ID_AuthenticatedPrivate">
        <dsig:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
        <dsig:DigestValue>NhYl0nDJW17dFmQlBIhyEMzP83r4CcHmQIQBLFBbD6U=</dsig:DigestValue>
      </dsig:Reference>
    </dsig:SignedInfo>
    <dsig:SignatureValue>ZLyCn8C0T1vp2Bbhk4W04WwWahdTJgO0n18ZA+EY1MI+0cfExIrfmN3zfd8bs8WT
3X7f8YgGZgUgymqaSmnxOUpmuuU/QEX6wWwiR4WRY6OSW8SwGuHoqzNatjhtqCnY
QDn/yXA4bGXJyFJNbEH7oPSere7cGAS3vwLTjAPvhij9ZywWJtWa5vUVycOc2i/F
gF9QKSuxz/29P3o56OHdlOkitnr1/irzUXneDTDGKbcDLpeIWY1MDlvTWwbahjNn
Svc4Fe90zBzjwGZcelqgho2Vb2M8+L7SxI2Xzcbs4NN8eJwR5diJapM6TwOM8gVv
K6mG6ZSii5c4LUls9iwlIQ==</dsig:SignatureValue>
  <dsig:KeyInfo>
<dsig:X509Data>
<dsig:X509IssuerSerial>
<dsig:X509IssuerName>dnQualifier=vVfvxXz1gOzEDwm2NoiJtcy4REQ=,CN=.192.168.254.3,OU=.cc-ra-1a.s430-2.ca.cinecert.com,O=.ca.cinecert.com</dsig:X509IssuerName>
<dsig:X509SerialNumber>38981</dsig:X509SerialNumber>
</dsig:X509IssuerSerial>
<dsig:X509Certificate>MIIEeDCCA2CgAwIBAgIDAJhFMA0GCSqGSIb3DQEBCwUAMIGGMRkwFwYDVQQKExAu
Y2EuY2luZWNlcnQuY29tMSkwJwYDVQQLEyAuY2MtcmEtMWEuczQzMC0yLmNhLmNp
bmVjZXJ0LmNvbTEXMBUGA1UEAxMOLjE5Mi4xNjguMjU0LjMxJTAjBgNVBC4THHZW
ZnZ4WHoxZ096RUR3bTJOb2lKdGN5NFJFUT0wHhcNMDgwNjE5MjI0NzI2WhcNMjQx
MjMwMDAwMDAwWjCBgjEZMBcGA1UEChMQLmNhLmNpbmVjZXJ0LmNvbTEpMCcGA1UE
CxMgLmNjLXJhLTFhLnM0MzAtMi5jYS5jaW5lY2VydC5jb20xEzARBgNVBAMTClNN
LmRlZmF1bHQxJTAjBgNVBC4THHF0WXI1QzBuMkZBNy9ZSkNXeTBwSno4eEJwTT0w
ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDkNr9C7ahGRVajMzt0cIp0
7d6V4h4DkzLTbFTMYPU0xXqmPGLmvpIZ66ooZfm7dJcokEdpOh6VgfNBHnKmsQUx
cg8F1ofKgR10bzA858wxscaZLiuidlxnvX8ih/0lCYvkyQGqBXm0YboVPQz08uyD
VzQPLRBfbHwt/ZCXwAMDLRs5Qlm4uZaSP6R296BxJ0vT7jnfGX42OffZaJlm+uoX
d0vKYLGtywLuR3prGjwtB3iD4NTc3P3W6uKS5AAOAXcefhsYCQNkeYM0iWTFYlo6
8fZ35Zc4aIsp2MaL0RVquwfN1hRw0+Tuwr0E2c5fB9AkGpFea/VHm85H/JXpWNXv
AgMBAAGjgfAwge0wCwYDVR0PBAQDAgSwMAwGA1UdEwEB/wQCMAAwHQYDVR0OBBYE
FKrWK+QtJ9hQO/2CQlstKSc/MQaTMIGwBgNVHSMEgagwgaWAFL1X78V89YDsxA8J
tjaIibXMuEREoYGHpIGEMIGBMRkwFwYDVQQKExAuY2EuY2luZWNlcnQuY29tMSkw
JwYDVQQLEyAuY2MtcmEtMWEuczQzMC0yLmNhLmNpbmVjZXJ0LmNvbTESMBAGA1UE
AxMJLmNjLXJhLTJjMSUwIwYDVQQuExxkRmtrUW9oMWNJekJ1TmJDQjlUV3liaG1L
b0U9ggMAgIIwDQYJKoZIhvcNAQELBQADggEBAGY7W0x3zGauJSGZhjYG8OP3AXN9
dvRjChn6z1zXRFIlQ9ECmbZBOZTwHYEl1115gJECH6GEHNSPeKUDy9+naeUNdVYm
NL535xA7lwTyRXp+0D2I8VXf0vE/x7Q8rEkYLlQ+JvPr4YmiFcbit24/U55ehOJ9
2pVdtpglh0nmtd1mvvPjY3+ZtIkc6It82yV13AV1aj7pXUz4ec6ZnOQ5GI9UFQW/
b5hObV8X7VOb9jIKL3zzLwKuSgcjpDoIqrynEoC+x2PWLkmS6tYDZxasixwbUBLY
cAcS6BoN9Qmn188npCiiruBkwPyMs0TUIT3h0pt6+tjp3c9dDCGv2tjgpD8=
</dsig:X509Certificate>
</dsig:X509Data>
<dsig:X509Data>
<dsig:X509IssuerSerial>
<dsig:X509IssuerName>dnQualifier=dFkkQoh1cIzBuNbCB9TWybhmKoE=,CN=.cc-ra-2c,OU=.cc-ra-1a.s430-2.ca.cinecert.com,O=.ca.cinecert.com</dsig:X509IssuerName>
<dsig:X509SerialNumber>32898</dsig:X509SerialNumber>
</dsig:X509IssuerSerial>
<dsig:X509Certificate>MIIEcTCCA1mgAwIBAgIDAICCMA0GCSqGSIb3DQEBCwUAMIGBMRkwFwYDVQQKExAu
Y2EuY2luZWNlcnQuY29tMSkwJwYDVQQLEyAuY2MtcmEtMWEuczQzMC0yLmNhLmNp
bmVjZXJ0LmNvbTESMBAGA1UEAxMJLmNjLXJhLTJjMSUwIwYDVQQuExxkRmtrUW9o
MWNJekJ1TmJDQjlUV3liaG1Lb0U9MB4XDTA4MDYxOTIyNDY1MVoXDTI0MTIzMTAw
MDAwMFowgYYxGTAXBgNVBAoTEC5jYS5jaW5lY2VydC5jb20xKTAnBgNVBAsTIC5j
Yy1yYS0xYS5zNDMwLTIuY2EuY2luZWNlcnQuY29tMRcwFQYDVQQDEw4uMTkyLjE2
OC4yNTQuMzElMCMGA1UELhMcdlZmdnhYejFnT3pFRHdtMk5vaUp0Y3k0UkVRPTCC
ASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMPBTSPhpKBPe9U81+hAgaV1
yo05zLbqrpfyXuM53NVUZ8EE1uFaK3zqolABYtWM8LAUXzv2LD+/og0DRPfPAj66
pT4DA34Xf5mNjYzHt60Mfm6clUxSQ42vdqto8fb9XnGcwgKuSyzGpYrJ5tTD/aiP
pD6FA/0IQ3ecAXWXKDXOIP/tEzQxcPwo9AkvSXp/Ne0MBovia3EoDx75DFs5BJ16
UTFOkATpDxw8e7rLeNkXrwGIpNw9vWYn3NiZwFRTN2w3Ck6APeJNmns2dRciy44m
Glw5GV4DJh5d8ZXiCnRk2nhY3V/UxY4FXhoHxWE+wKwEPzHKfcnxaHO1zPCoAM8C
AwEAAaOB6jCB5zALBgNVHQ8EBAMCAQYwEgYDVR0TAQH/BAgwBgEB/wIBADAdBgNV
HQ4EFgQUvVfvxXz1gOzEDwm2NoiJtcy4REQwgaQGA1UdIwSBnDCBmYAUdFkkQoh1
cIzBuNbCB9TWybhmKoGhfKR6MHgxGTAXBgNVBAoTEC5jYS5jaW5lY2VydC5jb20x
IDAeBgNVBAsTFy5zNDMwLTIuY2EuY2luZWNlcnQuY29tMRIwEAYDVQQDEwkuY2Mt
cmEtMWExJTAjBgNVBC4THEsrRERkcDF5R1dsbmVXYVgzVUlvSVh0QVFUMD2CAwCP
xzANBgkqhkiG9w0BAQsFAAOCAQEAGL/6PXYURL2DOJmhCQ65Sv8CJTBaNWJagVdM
AYOWAJHENot0nPd60CEuM7Ct0cdyEPpeGgBRFRqdNie2JshCeF+AJo04suBmrv1w
9Kd9CyAHsRSuMX3GcNq8r5MekxuzX9DOmke4xZIn29XgqM0iq3JcfKvPeAFrPPPg
o7chlGljzgIV8KyeA3bIDxunP5akKE84wYD0DUDhsp5+BxTazMT6vTq9ekHVvjxP
p9dR1EPV96PJ3zno7Y47wYy2x6P7z/EhEmA0MHLV7F6Xgdh/6JXWRMpxoqaGis+F
XXihVTpytQYDjkszHzu+HTFKHmIUKzePAdT9qZr/dwFZ5Gdivg==
</dsig:X509Certificate>
</dsig:X509Data>
<dsig:X509Data>
<dsig:X509IssuerSerial>
<dsig:X509IssuerName>dnQualifier=K\+DDdp1yGWlneWaX3UIoIXtAQT0=,CN=.cc-ra-1a,OU=.s430-2.ca.cinecert.com,O=.ca.cinecert.com</dsig:X509IssuerName>
<dsig:X509SerialNumber>36807</dsig:X509SerialNumber>
</dsig:X509IssuerSerial>
<dsig:X509Certificate>MIIEWTCCA0GgAwIBAgIDAI/HMA0GCSqGSIb3DQEBCwUAMHgxGTAXBgNVBAoTEC5j
YS5jaW5lY2VydC5jb20xIDAeBgNVBAsTFy5zNDMwLTIuY2EuY2luZWNlcnQuY29t
MRIwEAYDVQQDEwkuY2MtcmEtMWExJTAjBgNVBC4THEsrRERkcDF5R1dsbmVXYVgz
VUlvSVh0QVFUMD0wHhcNMDcwMzI3MDcxMzU2WhcNMjUwMTAxMDAwMDAwWjCBgTEZ
MBcGA1UEChMQLmNhLmNpbmVjZXJ0LmNvbTEpMCcGA1UECxMgLmNjLXJhLTFhLnM0
MzAtMi5jYS5jaW5lY2VydC5jb20xEjAQBgNVBAMTCS5jYy1yYS0yYzElMCMGA1UE
LhMcZEZra1FvaDFjSXpCdU5iQ0I5VFd5YmhtS29FPTCCASIwDQYJKoZIhvcNAQEB
BQADggEPADCCAQoCggEBAOxGeJOQ2NzJ6mEAu4Ni+YGrI0fqwhZvKylDgbafJtFB
3/2GTEyYZgCETXyX2YugAh3iie34SUikY3YeF61cSNMGUvKMYxogoo98eK4KjA5l
T6xPZcRvBL7ln7GgKd4IdwdG/3EzUjIqR78tNcnl/cgJ10bGWGgcNzAzW1Wh+lfG
b+R34liZxaQ8snb1rSJ/VVkf39ueq2V0EhYs2qzFEcHU9Kha5VTtdP44xDvOF5Sy
22ig75CdKcJHdgDs/8PJsbrFkvVzb7sEdS4lQ+STJdEwMTrDRk0i+iG5hxCpZJAc
NFr4bXLu5W8MFCQMDfIHpjaEy84xaGtlLhzvHK6mUAECAwEAAaOB4TCB3jALBgNV
HQ8EBAMCAQYwEgYDVR0TAQH/BAgwBgEB/wIBAzAdBgNVHQ4EFgQUdFkkQoh1cIzB
uNbCB9TWybhmKoEwgZsGA1UdIwSBkzCBkIAUK+DDdp1yGWlneWaX3UIoIXtAQT2h
c6RxMG8xGTAXBgNVBAoTEC5jYS5jaW5lY2VydC5jb20xGTAXBgNVBAsTEC5jYS5j
aW5lY2VydC5jb20xEDAOBgNVBAMTBy5zNDMwLTIxJTAjBgNVBC4THDhPOFc4b1lI
bGY5N1k4bjBrZEFnTVU3L2pVVT2CAwDHFjANBgkqhkiG9w0BAQsFAAOCAQEA3Qqg
ixs7PWXx0lT+b7KUAtQ6yIwqJWJ6ZP6AiVi+uo/yiKMgziKw4D+/x5Uq2qOgorlc
+jTPVr+Gln7IV/HwSvc3HdduGeNy5dg2LomkP8gqIXRkd8UcePji3KUtnuax0jpy
LXymO+mQzZiFPJY99xthgOTI0ksjZK1ryxbC9S3JqmRDtj0kvZyT/lvDHS3xwitO
vm3Y7nYOIXLDdC6NZdsi/GaSSOOO0KQJzgJ6afFOlzYMbz1/sSiOd60tmIuztSbf
exEP1qeNXRCHIRntXOfBlXJvGLu9vwVOeOMK43MZjsQLxgfv8MxLYYwx6crkhWRm
Nk28wnTwGFz93rhRSg==
</dsig:X509Certificate>
</dsig:X509Data>
<dsig:X509Data>
<dsig:X509IssuerSerial>
<dsig:X509IssuerName>dnQualifier=8O8W8oYHlf97Y8n0kdAgMU7/jUU=,CN=.s430-2,OU=.ca.cinecert.com,O=.ca.cinecert.com</dsig:X509IssuerName>
<dsig:X509SerialNumber>50966</dsig:X509SerialNumber>
</dsig:X509IssuerSerial>
<dsig:X509Certificate>MIIETDCCAzSgAwIBAgIDAMcWMA0GCSqGSIb3DQEBCwUAMG8xGTAXBgNVBAoTEC5j
YS5jaW5lY2VydC5jb20xGTAXBgNVBAsTEC5jYS5jaW5lY2VydC5jb20xEDAOBgNV
BAMTBy5zNDMwLTIxJTAjBgNVBC4THDhPOFc4b1lIbGY5N1k4bjBrZEFnTVU3L2pV
VT0wHhcNMDcwMzI3MDcxMzA4WhcNMjYwMTAxMDAwMDAwWjB4MRkwFwYDVQQKExAu
Y2EuY2luZWNlcnQuY29tMSAwHgYDVQQLExcuczQzMC0yLmNhLmNpbmVjZXJ0LmNv
bTESMBAGA1UEAxMJLmNjLXJhLTFhMSUwIwYDVQQuExxLK0REZHAxeUdXbG5lV2FY
M1VJb0lYdEFRVDA9MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA8ztG
Pz71+8WrCu6NwAbIUetNjBORWcqXt7a62UCEHu5mbb/ca+OAV90gRPLL1LqbzsJU
u8DoptMYhsQ/+d+Ln1fIUjsJhQIJKn5lQxIhiIPJ6iGeKo0+srN/ugAOKru9h/9e
I9upHpCOo4lfyIKHhkHZAWkkIeSzyM8/VqYF66TGsndjofiwHW8LG964EFpRWouO
j1reAP5CUc9Ftj8IVdEUcIcexClzwcJqwePWQpjXne5e3w4lRI8TgBiCz0VSgXk1
9oSEud3n4Pdo+FjvDCOCIWYHMYyjLB+/atnpShCbsstYJ/cc68ad+W27y88HOYSM
9PGYuamQbUtid9zsIQIDAQABo4HnMIHkMAsGA1UdDwQEAwIBBjASBgNVHRMBAf8E
CDAGAQH/AgEEMB0GA1UdDgQWBBQr4MN2nXIZaWd5ZpfdQighe0BBPTCBoQYDVR0j
BIGZMIGWgBTw7xbyhgeV/3tjyfSR0CAxTv+NRaFzpHEwbzEZMBcGA1UEChMQLmNh
LmNpbmVjZXJ0LmNvbTEZMBcGA1UECxMQLmNhLmNpbmVjZXJ0LmNvbTEQMA4GA1UE
AxMHLnM0MzAtMjElMCMGA1UELhMcOE84VzhvWUhsZjk3WThuMGtkQWdNVTcvalVV
PYIJALhGwbfi5fVsMA0GCSqGSIb3DQEBCwUAA4IBAQAPYRpoaH9vKLut/HngT3q7
x2GWz+QKMxbDKNY21VTEleADF3jdWWz+pUf8adnBS3TScMQtmWWUDIXSpXeUQI07
4ptSOze0pk13hP2VqZWu5DYosL2Y9mDhW+fxN/15EjbzwpM7/KUPGPOdL4ytSqqT
wKSApLAK/9yWrchF5OJup1/zcIBuzNP0v5wi63XPByVU1RhcWseyYbwxo452mPB2
3JOUq6tr3vvFfXagVf8/0wFTV3wtAXpNPQKjhMvz5n4/N/EFqXrknnlcY9dWopFI
uLIrGE9FVxvsNJ1YzANC9Y6/vCKaRalwQ62W1nClQ/WzQn0C46hkuNxTI4diIm3+
</dsig:X509Certificate>
</dsig:X509Data>
<dsig:X509Data>
<dsig:X509IssuerSerial>
<dsig:X509IssuerName>dnQualifier=8O8W8oYHlf97Y8n0kdAgMU7/jUU=,CN=.s430-2,OU=.ca.cinecert.com,O=.ca.cinecert.com</dsig:X509IssuerName>
<dsig:X509SerialNumber>13278513546878383468</dsig:X509SerialNumber>
</dsig:X509IssuerSerial>
<dsig:X509Certificate>MIIESTCCAzGgAwIBAgIJALhGwbfi5fVsMA0GCSqGSIb3DQEBCwUAMG8xGTAXBgNV
BAoTEC5jYS5jaW5lY2VydC5jb20xGTAXBgNVBAsTEC5jYS5jaW5lY2VydC5jb20x
EDAOBgNVBAMTBy5zNDMwLTIxJTAjBgNVBC4THDhPOFc4b1lIbGY5N1k4bjBrZEFn
TVU3L2pVVT0wHhcNMDcwMzEyMTQ1MjEyWhcNMjcwMzA3MTQ1MjEyWjBvMRkwFwYD
VQQKExAuY2EuY2luZWNlcnQuY29tMRkwFwYDVQQLExAuY2EuY2luZWNlcnQuY29t
MRAwDgYDVQQDEwcuczQzMC0yMSUwIwYDVQQuExw4TzhXOG9ZSGxmOTdZOG4wa2RB
Z01VNy9qVVU9MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAph/idpSe
h3CuscvGWmU+i2nZcyQAWJkztubSvukI9OMyLdLcXA4b1sRpxzkzFJ4NGyloHoVG
OW3dhm/HrUdbiICHgEzMOJq33bBvZvf8OIw6zbSkTJCu2NbX8rBkjxs72i2ANjXJ
LBJz4hHi3KQ0027fZRQ80uksUA96pN4xSkUEdz9cm2IrjmIRTXBKxxL7VvG2sK4j
DodedAOQPMczKYeA4CC64cFpPyl9s4mbZJ6roNahBX3p5zmxk9C/qWDEZeiJoPQS
+gDEfRJFTLOkH2/onrE1Gw5/ErBzhZcfh6uOYUt3YlEYZDN6cJuUyPr3BaSI2rC2
vB/Ex8HioTm4rwIDAQABo4HnMIHkMB0GA1UdDgQWBBTw7xbyhgeV/3tjyfSR0CAx
Tv+NRTCBoQYDVR0jBIGZMIGWgBTw7xbyhgeV/3tjyfSR0CAxTv+NRaFzpHEwbzEZ
MBcGA1UEChMQLmNhLmNpbmVjZXJ0LmNvbTEZMBcGA1UECxMQLmNhLmNpbmVjZXJ0
LmNvbTEQMA4GA1UEAxMHLnM0MzAtMjElMCMGA1UELhMcOE84VzhvWUhsZjk3WThu
MGtkQWdNVTcvalVVPYIJALhGwbfi5fVsMBIGA1UdEwEB/wQIMAYBAf8CAQUwCwYD
VR0PBAQDAgIEMA0GCSqGSIb3DQEBCwUAA4IBAQBXNS39cY/a0bIUJRqL+LfI7lIw
EY6sXABbwmUUO42Y/eS7gbpacJnSKrGtdRFWhoC0cCNR1QWrn4IOsKNRi3ed0kCo
ccMjlaUFnUhjLUW5xQSx2w09v+bUkPlUm2hjFxOneFPbSCiWTrlmDFRqPz8+rvpT
Q7tMBqEDNFtjrB/8KJmJwajf5CaamyFPqc2aMYj9B7GPtzcKPQlbQeAGf+x4l7Iz
Y5iOkXqv8VqwxV3ngjV9RlLfPN3OhoBH9jTXV8kNe+mkzqQhhf6HYI50FDOVR6yC
C7Fa0KtH0mnRwmZZKW/8vPOIeffauUs2BVVGz/K6Xvk1XWPz2O34IfGIC8r9
</dsig:X509Certificate>
</dsig:X509Data>
</dsig:KeyInfo>
</dsig:Signature>
</DCinemaSecurityMessage>
"""

class TestLockpick(unittest.TestCase):
    """
        Units tests for the Lockpick Python client
        """
    
    def setUp(self):
        self.lockpyck = Lockpyck(_TESTUSER, _TESTPASS, _TESTHOST)
    
    def test_version(self):
        self.assertTrue(self.lockpyck.version == 0.01)
    
    def test_kdm(self):
        kdm = self.lockpyck.kdm('daf5f223-5924-4a43-8f3b-e34a0b13f4b4')
        for k in kdm.keys():
            self.assertTrue(k in ('id', 'text', 'subject', 'valid_from', 'valid_to', 'cpl_id', 'cpl_text', 'xml', 'status', 'user', 'signer',))
        for k in kdm['subject'].keys():
            self.assertTrue(k in ('thumbprint', 'name', 'org', 'unit',))
        self.assertEqual(kdm['subject']['thumbprint'], 'dCxHtnikb+RSfBAuRkIVqPxaY4I=')
    
    def test_save_kdm(self):
        result = self.lockpyck.save_kdm(_TESTKDM)
        self.assertTrue(not 'errors' in result.keys())
        self.assertEqual(result['message'], 'Saved KDM')
	kdm = self.lockpyck.kdm('4a8c103c-8d55-4cea-b665-b08d8053e576')
	self.assertEqual(kdm['xml'], _TESTKDM)

    def test_kdms_from_thumbprint(self):
        kdms = self.lockpyck.kdms_from_thumbprint('Gio9Szty8daEiFpFUVMv2uiackk=')
        self.assertTrue(len(kdms))

    def test_kdm_bundle(self):
	# Add the test KDM
        self.lockpyck.save_kdm(_TESTKDM)
	# Retrieve the bundle
	filename, tarball = self.lockpyck.kdm_bundle('6b3f9ef8-f9c4-42b9-aff0-645cb0b11e06',
			                             '1a2a3d4b3b72f1d684885a4551532fdae89a7249')
	self.assertEqual(filename, 'KDMb-6b3f9ef8-f9c4-42b9-aff0-645cb0b11e06.tar')
	self.assertTrue(tarball.find('<AnnotationText language="en">Locksmith KDM Bundle</AnnotationText>') != -1)

if __name__ == '__main__':
    unittest.main()
