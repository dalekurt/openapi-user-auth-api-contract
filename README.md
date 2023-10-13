---
title: User Authentication API
viewport: 'width=device-width, initial-scale=1'
---

::: {#redoc}
::: {.sc-dvUynV .fDfMfd .redoc-wrap}
::: {.sc-eWnToP .coDLND .menu-content style="top:0px;height:calc(100vh - 0px)"}
::: {.sc-kizEQm .bUGKYA role="search"}
:::

::: {.sc-iklJeh .leCKhp .scrollbar-container .undefined}
-   [admin]{.sc-hzUIXc .ylzCN title="admin"}
    -   [get]{.sc-ikXwFM .ecAtVr .operation-type .get
        type="get"}[Retrieve User Information]{.sc-hzUIXc .jYJtsM
        width="calc(100% - 38px)"}
    -   [patch]{.sc-ikXwFM .ecAtVr .operation-type .patch
        type="patch"}[Update User Information]{.sc-hzUIXc .jYJtsM
        width="calc(100% - 38px)"}
    -   [del]{.sc-ikXwFM .ecAtVr .operation-type .delete
        type="delete"}[Delete User]{.sc-hzUIXc .jYJtsM
        width="calc(100% - 38px)"}
    -   [post]{.sc-ikXwFM .ecAtVr .operation-type .post
        type="post"}[Create New User]{.sc-hzUIXc .jYJtsM
        width="calc(100% - 38px)"}
    -   [get]{.sc-ikXwFM .ecAtVr .operation-type .get type="get"}[Get
        All Users]{.sc-hzUIXc .jYJtsM width="calc(100% - 38px)"}
-   [users]{.sc-hzUIXc .ylzCN title="users"}
    -   [get]{.sc-ikXwFM .ecAtVr .operation-type .get
        type="get"}[Retrieve User Information]{.sc-hzUIXc .jYJtsM
        width="calc(100% - 38px)"}
    -   [patch]{.sc-ikXwFM .ecAtVr .operation-type .patch
        type="patch"}[Update User Information]{.sc-hzUIXc .jYJtsM
        width="calc(100% - 38px)"}
    -   [post]{.sc-ikXwFM .ecAtVr .operation-type .post
        type="post"}[Create New User]{.sc-hzUIXc .jYJtsM
        width="calc(100% - 38px)"}

::: {.sc-kYPZxB .blYhnj}
[API docs by Redocly](https://redocly.com/redoc/)
:::
:::
:::

::: {.sc-kTCsyW .ceJzZm}
::: {.sc-irKDMX .eOSIAa}
:::
:::

::: {.sc-jtiXyc .kRuFuS .api-content}
::: {.sc-eCApnc .jlMQbh}
::: {.sc-iCoGMd .gLxhOh}
::: {.sc-hKFxyN .juinod .api-info}
User Authentication API (1.0) {#user-authentication-api-1.0 .sc-fujyAs .sc-dFRpbK .bpZWeL .fdKBSs}
=============================

Download OpenAPI specification:[Download]{.sc-bsatvv .gidAUi}

::: {.sc-iJCRrE .sc-ciSkZP .jCdxGr .QGruV}
::: {.sc-euEtCV .jOrOKn}
::: {.sc-fHCHyC .bpQNnD}
[Dale-Kurt Murray: <dalekurt@lunarops.io>]{.sc-gIvpjk .dnRviY} [URL:
<https://www.lunarops.io>]{.sc-gIvpjk .dnRviY} [License: [Apache
2.0](https://www.apache.org/license/LICENSE-2.0.html)]{.sc-gIvpjk
.dnRviY}
:::
:::
:::

::: {.sc-iJCRrE .sc-ciSkZP .jCdxGr .QGruV data-role="redoc-summary"}
User Authentication and Authorization API
:::

::: {.sc-iJCRrE .sc-ciSkZP .jCdxGr .QGruV data-role="redoc-description"}
This API facilitates user authentication and authorization processes
efficiently, offering functionalities for user creation, retrieval, and
updates while ensuring security.
:::
:::
:::
:::

::: {#tag/admin .sc-eCApnc .jlMQbh section-id="tag/admin"}
::: {.sc-iCoGMd .gLxhOh}
::: {.sc-hKFxyN .juinod}
[](#tag/admin){.sc-crzoAE .iUxAWq}admin {#admin .sc-fujyAs .bpZWeL}
=======================================
:::
:::

::: {.sc-hKFxyN .bJcDWV}
::: {.sc-iJCRrE .sc-ciSkZP .jCdxGr .QGruV .redoc-markdown}
Access to user management as an admin
:::
:::
:::

::: {#tag/admin/operation/get-admin-users-userid .sc-eCApnc .liLqNm section-id="tag/admin/operation/get-admin-users-userid"}
::: {#operation/get-admin-users-userid .sc-iCoGMd .gLxhOh section-id="operation/get-admin-users-userid"}
::: {.sc-hKFxyN .juinod}
[](#tag/admin/operation/get-admin-users-userid){.sc-crzoAE .iUxAWq}Retrieve User Information {#retrieve-user-information .sc-pNWdM .eftmgB}
--------------------------------------------------------------------------------------------

::: {.sc-iGkqmO .hCTIhr}
::: {.sc-iJCRrE .sc-ciSkZP .jCdxGr .QGruV}
Retrieve specific user details by their unique ID, mobile number, or
email address.
:::
:::

<div>

##### path Parameters {#path-parameters .sc-iqAclL .eONCmm}

+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcnRwz}[userid]{.property-name}  |                                   |
|                                   | <div>                             |
| ::: {.sc-                         |                                   |
| oeezt .sc-hhIiOg .dLCGMn .hIkHYw} | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
| required                          | .jrLlAa}[string]{.sc-laZMeE       |
| :::                               | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | The unique identifier of the      |
|                                   | user.                             |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+

</div>

<div>

##### query Parameters {#query-parameters .sc-iqAclL .eONCmm}

+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcnRwz}[mobile]{.property-name}  |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | Filter users by their mobile      |
|                                   | number.                           |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcnRwz}[email]{.property-name}   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | Filter users by their email       |
|                                   | address.                          |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+

</div>

<div>

### Responses {#responses .sc-fIxmyt .DvFer}

<div>

**200** []{.sc-jcwpoC .eDjFAZ}

User Found

</div>

<div>

**404** []{.sc-jcwpoC .eDjFAZ}

User Not Found

</div>

</div>
:::

::: {.sc-jSFjdj .sc-gKAaRy .gBjRyf .gcushC}
::: {.sc-EZqKI .fWsqvQ}
[get]{.sc-fmdNqN .ihNycv .http-verb .get
type="get"}[/admin/users/{userid}]{.sc-jXcxbT .fCEUju}

::: {.sc-ljsmAU .flIrdF aria-hidden="true"}
::: {.sc-jlZJtj .fQkroN}
::: {.sc-iJCRrE .sc-ciSkZP .jCdxGr .lhENGb}
:::

::: {tabindex="0" role="button"}
::: {.sc-dTSzeu .dfUAUz}
http://localhost:8000/admin/users/{userid}
:::
:::
:::
:::
:::

<div>

### Response samples {#response-samples .sc-kEqXSa .iXmHCl}

::: {.sc-cxNHIi .gxohHo rttabs="true"}
-   [200]{#react-tabs-0}

::: {#react-tabs-1 .react-tabs__tab-panel .react-tabs__tab-panel--selected role="tabpanel" aria-labelledby="react-tabs-0"}
<div>

::: {.sc-Arkif .jojbRz}
[Content type]{.sc-cOifOu .hlhNtL}

::: {.sc-bBjRSN .kQSIAz}
application/json
:::
:::

::: {.sc-jgPyTC .dSaTNC}
::: {.sc-Arkif .jojbRz}
[Example]{.sc-cOifOu .hlhNtL}

::: {.sc-hiKfDv .sc-khIgEk .bycQNU .hLNtis}
Get User Jane SmithGet User John DoeGet User Jane Smith
:::
:::

<div>

::: {.sc-jNnpgg .esZIbL}
::: {.sc-giAqHp .hMPeqJ}
::: {.sc-carFqZ .UksDl}
Copy
:::
:::

::: {.sc-iJCRrE .jCdxGr .sc-dPaNzc .gyljjx}
::: {.redoc-json}
`{`

-   ::: {.hoverable}
    [\"id\"]{.property .token .string}: [136]{.token .number}[,]{.token
    .punctuation}
    :::

-   ::: {.hoverable}
    [\"first\_name\"]{.property .token .string}: [\"Jane\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"last\_name\"]{.property .token .string}: [\"Smith\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"email\"]{.property .token .string}:
    [\"jane.smith\@gmail.com\"]{.token .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"mobile\"]{.property .token .string}: [\"347-123-4567\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"username\"]{.property .token .string}: [\"janesmith\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"password\"]{.property .token .string}: [\"s3cretPwd\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"email\_verified\"]{.property .token .string}: [true]{.token
    .boolean}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"is\_active\"]{.property .token .string}: [true]{.token
    .boolean}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"created\_at\"]{.property .token .string}: [\"2023-09-15
    00:00:00\"]{.token .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"updated\_at\"]{.property .token .string}: [\"2023-09-15
    00:00:00\"]{.token .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"last\_login\"]{.property .token .string}: [\"2023-09-15
    00:00:00\"]{.token .string}
    :::

[}]{.token .punctuation}
:::
:::
:::

</div>
:::

</div>
:::
:::

</div>
:::
:::
:::

::: {#tag/admin/operation/patch-admin-users-userid .sc-eCApnc .liLqNm section-id="tag/admin/operation/patch-admin-users-userid"}
::: {#operation/patch-admin-users-userid .sc-iCoGMd .gLxhOh section-id="operation/patch-admin-users-userid"}
::: {.sc-hKFxyN .juinod}
[](#tag/admin/operation/patch-admin-users-userid){.sc-crzoAE .iUxAWq}Update User Information {#update-user-information .sc-pNWdM .eftmgB}
--------------------------------------------------------------------------------------------

::: {.sc-iGkqmO .hCTIhr}
::: {.sc-iJCRrE .sc-ciSkZP .jCdxGr .QGruV}
Modify user information, including first name, last name, email, mobile
number, password, and activation status.
:::
:::

<div>

##### path Parameters {#path-parameters-1 .sc-iqAclL .eONCmm}

+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcnRwz}[userid]{.property-name}  |                                   |
|                                   | <div>                             |
| ::: {.sc-                         |                                   |
| oeezt .sc-hhIiOg .dLCGMn .hIkHYw} | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
| required                          | .jrLlAa}[string]{.sc-laZMeE       |
| :::                               | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | The unique identifier of the      |
|                                   | user.                             |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+

</div>

<div>

##### query Parameters {#query-parameters-1 .sc-iqAclL .eONCmm}

+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcnRwz}[mobile]{.property-name}  |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | Filter users by their mobile      |
|                                   | number.                           |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcnRwz}[email]{.property-name}   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | Filter users by their email       |
|                                   | address.                          |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+

</div>

##### Request Body schema: [application/json]{.sc-cBoqAE .eKyrDP} {#request-body-schema-applicationjson .sc-iqAclL .eONCmm}

::: {.sc-iJCRrE .sc-ciSkZP .jCdxGr .QGruV}
:::

+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcn                              |                                   |
| Rwz}[first\_name]{.property-name} | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bc                               |                                   |
| nRwz}[last\_name]{.property-name} | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcnRwz}[email]{.property-name}   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}[      |
|                                   | \<email\> ]{.sc-laZMeE .sc-jffHpj |
|                                   | .jWaWWE .cThoNa}                  |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | Providing a new email temporarily |
|                                   | sets the email verification       |
|                                   | status to false.                  |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcnRwz}[mobile]{.property-name}  |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | Providing a new email temporarily |
|                                   | sets the email verification       |
|                                   | status to false.                  |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .                                 |                                   |
| bcnRwz}[password]{.property-name} | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}[      |
|                                   | \<password\> ]{.sc-laZMeE         |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bc                               |                                   |
| nRwz}[is\_active]{.property-name} | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[boolean]{.sc-laZMeE      |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | [ Default: ]{.sc-laZMeE .jWaWWE}  |
|                                   | [true]{.sc-laZMeE .sc-ckTSus      |
|                                   | .jWaWWE .fElSEN}                  |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+

<div>

### Responses {#responses-1 .sc-fIxmyt .DvFer}

<div>

**200** []{.sc-jcwpoC .eDjFAZ}

User Updated

</div>

<div>

**404** []{.sc-jcwpoC .eDjFAZ}

User Not Found

</div>

<div>

**409** []{.sc-jcwpoC .eDjFAZ}

Email Already Taken

</div>

</div>
:::

::: {.sc-jSFjdj .sc-gKAaRy .gBjRyf .gcushC}
::: {.sc-EZqKI .fWsqvQ}
[patch]{.sc-fmdNqN .cDAiVX .http-verb .patch
type="patch"}[/admin/users/{userid}]{.sc-jXcxbT .fCEUju}

::: {.sc-ljsmAU .flIrdF aria-hidden="true"}
::: {.sc-jlZJtj .fQkroN}
::: {.sc-iJCRrE .sc-ciSkZP .jCdxGr .lhENGb}
:::

::: {tabindex="0" role="button"}
::: {.sc-dTSzeu .dfUAUz}
http://localhost:8000/admin/users/{userid}
:::
:::
:::
:::
:::

<div>

### Request samples {#request-samples .sc-kEqXSa .iXmHCl}

::: {.sc-cxNHIi .gxohHo rttabs="true"}
-   [Payload]{#react-tabs-2}

::: {#react-tabs-3 .react-tabs__tab-panel .react-tabs__tab-panel--selected role="tabpanel" aria-labelledby="react-tabs-2"}
<div>

::: {.sc-Arkif .jojbRz}
[Content type]{.sc-cOifOu .hlhNtL}

::: {.sc-bBjRSN .kQSIAz}
application/json
:::
:::

::: {.sc-jgPyTC .dSaTNC}
::: {.sc-Arkif .jojbRz}
[Example]{.sc-cOifOu .hlhNtL}

::: {.sc-hiKfDv .sc-khIgEk .bycQNU .hLNtis}
Update First NameUpdate Last NameUpdate Email and MobileUpdate
PasswordUpdate Activation StatusCombined UpdatesUpdate First Name
:::
:::

<div>

::: {.sc-jNnpgg .esZIbL}
::: {.sc-giAqHp .hMPeqJ}
::: {.sc-carFqZ .UksDl}
Copy
:::
:::

::: {.sc-iJCRrE .jCdxGr .sc-dPaNzc .gyljjx}
::: {.redoc-json}
`{`

-   ::: {.hoverable}
    [\"first\_name\"]{.property .token .string}: [\"Updated
    Jane\"]{.token .string}
    :::

[}]{.token .punctuation}
:::
:::
:::

</div>
:::

</div>
:::
:::

</div>

<div>

### Response samples {#response-samples-1 .sc-kEqXSa .iXmHCl}

::: {.sc-cxNHIi .gxohHo rttabs="true"}
-   [200]{#react-tabs-4}

::: {#react-tabs-5 .react-tabs__tab-panel .react-tabs__tab-panel--selected role="tabpanel" aria-labelledby="react-tabs-4"}
<div>

::: {.sc-Arkif .jojbRz}
[Content type]{.sc-cOifOu .hlhNtL}

::: {.sc-bBjRSN .kQSIAz}
application/json
:::
:::

::: {.sc-jgPyTC .dSaTNC}
::: {.sc-Arkif .jojbRz}
[Example]{.sc-cOifOu .hlhNtL}

::: {.sc-hiKfDv .sc-khIgEk .bycQNU .hLNtis}
Updated First NameUpdated Last NameUpdated Email and MobileUpdated
PasswordUpdated Activation StatusCombined UpdatesUpdated First Name
:::
:::

<div>

::: {.sc-jNnpgg .esZIbL}
::: {.sc-giAqHp .hMPeqJ}
::: {.sc-carFqZ .UksDl}
Copy
:::
:::

::: {.sc-iJCRrE .jCdxGr .sc-dPaNzc .gyljjx}
::: {.redoc-json}
`{`

-   ::: {.hoverable}
    [\"id\"]{.property .token .string}: [136]{.token .number}[,]{.token
    .punctuation}
    :::

-   ::: {.hoverable}
    [\"first\_name\"]{.property .token .string}: [\"Updated
    Jane\"]{.token .string}
    :::

[}]{.token .punctuation}
:::
:::
:::

</div>
:::

</div>
:::
:::

</div>
:::
:::
:::

::: {#tag/admin/operation/delete-admin-users-userid .sc-eCApnc .liLqNm section-id="tag/admin/operation/delete-admin-users-userid"}
::: {#operation/delete-admin-users-userid .sc-iCoGMd .gLxhOh section-id="operation/delete-admin-users-userid"}
::: {.sc-hKFxyN .juinod}
[](#tag/admin/operation/delete-admin-users-userid){.sc-crzoAE .iUxAWq}Delete User {#delete-user .sc-pNWdM .eftmgB}
---------------------------------------------------------------------------------

::: {.sc-iGkqmO .hCTIhr}
::: {.sc-iJCRrE .sc-ciSkZP .jCdxGr .QGruV}
Permanently remove an existing user and their associated data.
:::
:::

<div>

##### path Parameters {#path-parameters-2 .sc-iqAclL .eONCmm}

+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcnRwz}[userid]{.property-name}  |                                   |
|                                   | <div>                             |
| ::: {.sc-                         |                                   |
| oeezt .sc-hhIiOg .dLCGMn .hIkHYw} | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
| required                          | .jrLlAa}[string]{.sc-laZMeE       |
| :::                               | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | The unique identifier of the      |
|                                   | user.                             |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+

</div>

<div>

##### query Parameters {#query-parameters-2 .sc-iqAclL .eONCmm}

+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcnRwz}[mobile]{.property-name}  |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | Filter users by their mobile      |
|                                   | number.                           |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcnRwz}[email]{.property-name}   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | Filter users by their email       |
|                                   | address.                          |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+

</div>

##### Request Body schema: [application/json]{.sc-cBoqAE .eKyrDP} {#request-body-schema-applicationjson-1 .sc-iqAclL .eONCmm}

::: {.sc-iJCRrE .sc-ciSkZP .jCdxGr .QGruV}
:::

+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcnRwz}[id]{.property-name}      |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[integer]{.sc-laZMeE      |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcn                              |                                   |
| Rwz}[first\_name]{.property-name} | <div>                             |
|                                   |                                   |
| ::: {.sc-                         | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
| oeezt .sc-hhIiOg .dLCGMn .hIkHYw} | .jrLlAa}[string]{.sc-laZMeE       |
| required                          | .sc-jffHpj .jWaWWE .cThoNa}       |
| :::                               |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bc                               |                                   |
| nRwz}[last\_name]{.property-name} | <div>                             |
|                                   |                                   |
| ::: {.sc-                         | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
| oeezt .sc-hhIiOg .dLCGMn .hIkHYw} | .jrLlAa}[string]{.sc-laZMeE       |
| required                          | .sc-jffHpj .jWaWWE .cThoNa}       |
| :::                               |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcnRwz}[email]{.property-name}   |                                   |
|                                   | <div>                             |
| ::: {.sc-                         |                                   |
| oeezt .sc-hhIiOg .dLCGMn .hIkHYw} | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
| required                          | .jrLlAa}[string]{.sc-laZMeE       |
| :::                               | .sc-jffHpj .jWaWWE .cThoNa}[      |
|                                   | \<email\> ]{.sc-laZMeE .sc-jffHpj |
|                                   | .jWaWWE .cThoNa}                  |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcnRwz}[mobile]{.property-name}  |                                   |
|                                   | <div>                             |
| ::: {.sc-                         |                                   |
| oeezt .sc-hhIiOg .dLCGMn .hIkHYw} | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
| required                          | .jrLlAa}[string]{.sc-laZMeE       |
| :::                               | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .                                 |                                   |
| bcnRwz}[username]{.property-name} | <div>                             |
|                                   |                                   |
| ::: {.sc-                         | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
| oeezt .sc-hhIiOg .dLCGMn .hIkHYw} | .jrLlAa}[string]{.sc-laZMeE       |
| required                          | .sc-jffHpj .jWaWWE .cThoNa}       |
| :::                               |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .                                 |                                   |
| bcnRwz}[password]{.property-name} | <div>                             |
|                                   |                                   |
| ::: {.sc-                         | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
| oeezt .sc-hhIiOg .dLCGMn .hIkHYw} | .jrLlAa}[string]{.sc-laZMeE       |
| required                          | .sc-jffHpj .jWaWWE .cThoNa}[      |
| :::                               | \<password\> ]{.sc-laZMeE         |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcnRwz}                          |                                   |
| [email\_verified]{.property-name} | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[boolean]{.sc-laZMeE      |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcnRwz}[avatar]{.property-name}  |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bc                               |                                   |
| nRwz}[is\_active]{.property-name} | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[boolean]{.sc-laZMeE      |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcn                              |                                   |
| Rwz}[created\_at]{.property-name} | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}[      |
|                                   | \<date-time\> ]{.sc-laZMeE        |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcn                              |                                   |
| Rwz}[updated\_at]{.property-name} | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}[      |
|                                   | \<date-time\> ]{.sc-laZMeE        |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcn                              |                                   |
| Rwz}[last\_login]{.property-name} | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}[      |
|                                   | \<date-time\> ]{.sc-laZMeE        |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .b                                |                                   |
| cnRwz}[is\_admin]{.property-name} | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[boolean]{.sc-laZMeE      |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | [ Default: ]{.sc-laZMeE .jWaWWE}  |
|                                   | [false]{.sc-laZMeE .sc-ckTSus     |
|                                   | .jWaWWE .fElSEN}                  |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcnRwz}[roles]{.property-name}   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | [Array of ]{.sc-laZMeE .sc-iNiQyp |
|                                   | .jWaWWE                           |
|                                   | .jrLlAa}[strings]{.sc-laZMeE      |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+

<div>

### Responses {#responses-2 .sc-fIxmyt .DvFer}

<div>

**200** []{.sc-jcwpoC .eDjFAZ}

OK

</div>

<div>

**404** []{.sc-jcwpoC .eDjFAZ}

User Not Found

</div>

</div>
:::

::: {.sc-jSFjdj .sc-gKAaRy .gBjRyf .gcushC}
::: {.sc-EZqKI .fWsqvQ}
[delete]{.sc-fmdNqN .bJzUtf .http-verb .delete
type="delete"}[/admin/users/{userid}]{.sc-jXcxbT .fCEUju}

::: {.sc-ljsmAU .flIrdF aria-hidden="true"}
::: {.sc-jlZJtj .fQkroN}
::: {.sc-iJCRrE .sc-ciSkZP .jCdxGr .lhENGb}
:::

::: {tabindex="0" role="button"}
::: {.sc-dTSzeu .dfUAUz}
http://localhost:8000/admin/users/{userid}
:::
:::
:::
:::
:::

<div>

### Request samples {#request-samples-1 .sc-kEqXSa .iXmHCl}

::: {.sc-cxNHIi .gxohHo rttabs="true"}
-   [Payload]{#react-tabs-6}

::: {#react-tabs-7 .react-tabs__tab-panel .react-tabs__tab-panel--selected role="tabpanel" aria-labelledby="react-tabs-6"}
<div>

::: {.sc-Arkif .jojbRz}
[Content type]{.sc-cOifOu .hlhNtL}

::: {.sc-bBjRSN .kQSIAz}
application/json
:::
:::

::: {.sc-jgPyTC .dSaTNC}
::: {.sc-jNnpgg .esZIbL}
::: {.sc-giAqHp .hMPeqJ}
::: {.sc-carFqZ .UksDl}
Copy
:::
:::

::: {.sc-iJCRrE .jCdxGr .sc-dPaNzc .gyljjx}
::: {.redoc-json}
`{`

-   ::: {.hoverable}
    [\"id\"]{.property .token .string}: [136]{.token .number}[,]{.token
    .punctuation}
    :::

-   ::: {.hoverable}
    [\"first\_name\"]{.property .token .string}: [\"Jane\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"last\_name\"]{.property .token .string}: [\"Smith\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"email\"]{.property .token .string}:
    [\"jane.smith\@gmail.com\"]{.token .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"mobile\"]{.property .token .string}: [\"347-123-4567\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"username\"]{.property .token .string}: [\"janesmith\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"password\"]{.property .token .string}: [\"s3cretPwd\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"email\_verified\"]{.property .token .string}: [true]{.token
    .boolean}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"is\_active\"]{.property .token .string}: [true]{.token .boolean}
    :::

[}]{.token .punctuation}
:::
:::
:::
:::

</div>
:::
:::

</div>
:::
:::
:::

::: {#tag/admin/operation/post-admin-users .sc-eCApnc .liLqNm section-id="tag/admin/operation/post-admin-users"}
::: {#operation/post-admin-users .sc-iCoGMd .gLxhOh section-id="operation/post-admin-users"}
::: {.sc-hKFxyN .juinod}
[](#tag/admin/operation/post-admin-users){.sc-crzoAE .iUxAWq}Create New User {#create-new-user .sc-pNWdM .eftmgB}
----------------------------------------------------------------------------

::: {.sc-iGkqmO .hCTIhr}
::: {.sc-iJCRrE .sc-ciSkZP .jCdxGr .QGruV}
Add a new user
:::
:::

##### Request Body schema: [application/json]{.sc-cBoqAE .eKyrDP} {#request-body-schema-applicationjson-2 .sc-iqAclL .eONCmm}

::: {.sc-iJCRrE .sc-ciSkZP .jCdxGr .QGruV}
Create a new user with the specified details.
:::

+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcn                              |                                   |
| Rwz}[first\_name]{.property-name} | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bc                               |                                   |
| nRwz}[last\_name]{.property-name} | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcnRwz}[email]{.property-name}   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcnRwz}[mobile]{.property-name}  |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .                                 |                                   |
| bcnRwz}[username]{.property-name} | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .                                 |                                   |
| bcnRwz}[password]{.property-name} | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}[      |
|                                   | \<password\> ]{.sc-laZMeE         |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+

<div>

### Responses {#responses-3 .sc-fIxmyt .DvFer}

<div>

**200** []{.sc-jcwpoC .eDjFAZ}

User Created

</div>

<div>

**400** []{.sc-jcwpoC .eDjFAZ}

Missing Required Information

</div>

<div>

**409** []{.sc-jcwpoC .eDjFAZ}

Email Already Taken

</div>

</div>
:::

::: {.sc-jSFjdj .sc-gKAaRy .gBjRyf .gcushC}
::: {.sc-EZqKI .fWsqvQ}
[post]{.sc-fmdNqN .ldMUmp .http-verb .post
type="post"}[/admin/users]{.sc-jXcxbT .fCEUju}

::: {.sc-ljsmAU .flIrdF aria-hidden="true"}
::: {.sc-jlZJtj .fQkroN}
::: {.sc-iJCRrE .sc-ciSkZP .jCdxGr .lhENGb}
:::

::: {tabindex="0" role="button"}
::: {.sc-dTSzeu .dfUAUz}
http://localhost:8000/admin/users
:::
:::
:::
:::
:::

<div>

### Request samples {#request-samples-2 .sc-kEqXSa .iXmHCl}

::: {.sc-cxNHIi .gxohHo rttabs="true"}
-   [Payload]{#react-tabs-8}

::: {#react-tabs-9 .react-tabs__tab-panel .react-tabs__tab-panel--selected role="tabpanel" aria-labelledby="react-tabs-8"}
<div>

::: {.sc-Arkif .jojbRz}
[Content type]{.sc-cOifOu .hlhNtL}

::: {.sc-bBjRSN .kQSIAz}
application/json
:::
:::

::: {.sc-jgPyTC .dSaTNC}
::: {.sc-jNnpgg .esZIbL}
::: {.sc-giAqHp .hMPeqJ}
::: {.sc-carFqZ .UksDl}
Copy
:::
:::

::: {.sc-iJCRrE .jCdxGr .sc-dPaNzc .gyljjx}
::: {.redoc-json}
`{`

-   ::: {.hoverable}
    [\"first\_name\"]{.property .token .string}: [\"David\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"last\_name\"]{.property .token .string}: [\"Gavin\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"email\"]{.property .token .string}:
    [\"davidg\@gmail.com\"]{.token .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"mobile\"]{.property .token .string}: [\"347-123-4567\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"username\"]{.property .token .string}: [\"davidg\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"password\"]{.property .token .string}:
    [\"s3cr3tp\@assw0rd\"]{.token .string}
    :::

[}]{.token .punctuation}
:::
:::
:::
:::

</div>
:::
:::

</div>

<div>

### Response samples {#response-samples-2 .sc-kEqXSa .iXmHCl}

::: {.sc-cxNHIi .gxohHo rttabs="true"}
-   [200]{#react-tabs-10}

::: {#react-tabs-11 .react-tabs__tab-panel .react-tabs__tab-panel--selected role="tabpanel" aria-labelledby="react-tabs-10"}
<div>

::: {.sc-Arkif .jojbRz}
[Content type]{.sc-cOifOu .hlhNtL}

::: {.sc-bBjRSN .kQSIAz}
application/json
:::
:::

::: {.sc-jgPyTC .dSaTNC}
::: {.sc-jNnpgg .esZIbL}
::: {.sc-giAqHp .hMPeqJ}
::: {.sc-carFqZ .UksDl}
Copy
:::
:::

::: {.sc-iJCRrE .jCdxGr .sc-dPaNzc .gyljjx}
::: {.redoc-json}
`{`

-   ::: {.hoverable}
    [\"id\"]{.property .token .string}: [12]{.token .number}[,]{.token
    .punctuation}
    :::

-   ::: {.hoverable}
    [\"first\_name\"]{.property .token .string}: [\"Bob\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"last\_name\"]{.property .token .string}: [\"Fellow\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"email\"]{.property .token .string}:
    [\"bob.fellow\@gmail.com\"]{.token .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"username\"]{.property .token .string}: [\"bobfellow\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"password\"]{.property .token .string}: [\"p\@s\$w0rd\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"mobile\"]{.property .token .string}: [\"347-123-0001\"]{.token
    .string}
    :::

[}]{.token .punctuation}
:::
:::
:::
:::

</div>
:::
:::

</div>
:::
:::
:::

::: {#tag/admin/operation/get-admin-users .sc-eCApnc .liLqNm section-id="tag/admin/operation/get-admin-users"}
::: {#operation/get-admin-users .sc-iCoGMd .gLxhOh section-id="operation/get-admin-users"}
::: {.sc-hKFxyN .juinod}
[](#tag/admin/operation/get-admin-users){.sc-crzoAE .iUxAWq}Get All Users {#get-all-users .sc-pNWdM .eftmgB}
-------------------------------------------------------------------------

::: {.sc-iGkqmO .hCTIhr}
::: {.sc-iJCRrE .sc-ciSkZP .jCdxGr .QGruV}
Retrieve a list of all users
:::
:::

<div>

### Responses {#responses-4 .sc-fIxmyt .DvFer}

<div>

**200** []{.sc-jcwpoC .eDjFAZ}

OK

</div>

</div>
:::

::: {.sc-jSFjdj .sc-gKAaRy .gBjRyf .gcushC}
::: {.sc-EZqKI .fWsqvQ}
[get]{.sc-fmdNqN .ihNycv .http-verb .get
type="get"}[/admin/users]{.sc-jXcxbT .fCEUju}

::: {.sc-ljsmAU .flIrdF aria-hidden="true"}
::: {.sc-jlZJtj .fQkroN}
::: {.sc-iJCRrE .sc-ciSkZP .jCdxGr .lhENGb}
:::

::: {tabindex="0" role="button"}
::: {.sc-dTSzeu .dfUAUz}
http://localhost:8000/admin/users
:::
:::
:::
:::
:::

<div>

### Response samples {#response-samples-3 .sc-kEqXSa .iXmHCl}

::: {.sc-cxNHIi .gxohHo rttabs="true"}
-   [200]{#react-tabs-12}

::: {#react-tabs-13 .react-tabs__tab-panel .react-tabs__tab-panel--selected role="tabpanel" aria-labelledby="react-tabs-12"}
<div>

::: {.sc-Arkif .jojbRz}
[Content type]{.sc-cOifOu .hlhNtL}

::: {.sc-bBjRSN .kQSIAz}
application/json
:::
:::

::: {.sc-jgPyTC .dSaTNC}
::: {.sc-jNnpgg .esZIbL}
::: {.sc-giAqHp .hMPeqJ}
::: {.sc-carFqZ .UksDl}
Copy
:::
:::

::: {.sc-iJCRrE .jCdxGr .sc-dPaNzc .gyljjx}
::: {.redoc-json}
`{`

-   ::: {.hoverable}
    [\"id\"]{.property .token .string}: [0]{.token .number}[,]{.token
    .punctuation}
    :::

-   ::: {.hoverable}
    [\"first\_name\"]{.property .token .string}: [\"string\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"last\_name\"]{.property .token .string}: [\"string\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"email\"]{.property .token .string}: [\"string\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"mobile\"]{.property .token .string}: [\"string\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"username\"]{.property .token .string}: [\"string\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"password\"]{.property .token .string}: [\"string\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"email\_verified\"]{.property .token .string}: [true]{.token
    .boolean}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"is\_active\"]{.property .token .string}: [true]{.token
    .boolean}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"created\_at\"]{.property .token .string}: [\"string\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"updated\_at\"]{.property .token .string}: [\"string\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"last\_login\"]{.property .token .string}: [\"string\"]{.token
    .string}
    :::

[}]{.token .punctuation}
:::
:::
:::
:::

</div>
:::
:::

</div>
:::
:::
:::

::: {#tag/users .sc-eCApnc .jlMQbh section-id="tag/users"}
::: {.sc-iCoGMd .gLxhOh}
::: {.sc-hKFxyN .juinod}
[](#tag/users){.sc-crzoAE .iUxAWq}users {#users .sc-fujyAs .bpZWeL}
=======================================
:::
:::

::: {.sc-hKFxyN .bJcDWV}
::: {.sc-iJCRrE .sc-ciSkZP .jCdxGr .QGruV .redoc-markdown}
Access to user management as a regular user
:::
:::
:::

::: {#tag/users/operation/get-users-userid .sc-eCApnc .liLqNm section-id="tag/users/operation/get-users-userid"}
::: {#operation/get-users-userid .sc-iCoGMd .gLxhOh section-id="operation/get-users-userid"}
::: {.sc-hKFxyN .juinod}
[](#tag/users/operation/get-users-userid){.sc-crzoAE .iUxAWq}Retrieve User Information {#retrieve-user-information-1 .sc-pNWdM .eftmgB}
--------------------------------------------------------------------------------------

::: {.sc-iGkqmO .hCTIhr}
::: {.sc-iJCRrE .sc-ciSkZP .jCdxGr .QGruV}
Retrieve specific user details by their unique ID.
:::
:::

<div>

##### path Parameters {#path-parameters-3 .sc-iqAclL .eONCmm}

+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcnRwz}[userid]{.property-name}  |                                   |
|                                   | <div>                             |
| ::: {.sc-                         |                                   |
| oeezt .sc-hhIiOg .dLCGMn .hIkHYw} | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
| required                          | .jrLlAa}[string]{.sc-laZMeE       |
| :::                               | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | The unique identifier of the      |
|                                   | user.                             |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+

</div>

<div>

### Responses {#responses-5 .sc-fIxmyt .DvFer}

<div>

**200** []{.sc-jcwpoC .eDjFAZ}

User Found

</div>

</div>
:::

::: {.sc-jSFjdj .sc-gKAaRy .gBjRyf .gcushC}
::: {.sc-EZqKI .fWsqvQ}
[get]{.sc-fmdNqN .ihNycv .http-verb .get
type="get"}[/users/{userid}]{.sc-jXcxbT .fCEUju}

::: {.sc-ljsmAU .flIrdF aria-hidden="true"}
::: {.sc-jlZJtj .fQkroN}
::: {.sc-iJCRrE .sc-ciSkZP .jCdxGr .lhENGb}
:::

::: {tabindex="0" role="button"}
::: {.sc-dTSzeu .dfUAUz}
http://localhost:8000/users/{userid}
:::
:::
:::
:::
:::

<div>

### Response samples {#response-samples-4 .sc-kEqXSa .iXmHCl}

::: {.sc-cxNHIi .gxohHo rttabs="true"}
-   [200]{#react-tabs-14}

::: {#react-tabs-15 .react-tabs__tab-panel .react-tabs__tab-panel--selected role="tabpanel" aria-labelledby="react-tabs-14"}
<div>

::: {.sc-Arkif .jojbRz}
[Content type]{.sc-cOifOu .hlhNtL}

::: {.sc-bBjRSN .kQSIAz}
application/json
:::
:::

::: {.sc-jgPyTC .dSaTNC}
::: {.sc-jNnpgg .esZIbL}
::: {.sc-giAqHp .hMPeqJ}
::: {.sc-carFqZ .UksDl}
Copy
:::
:::

::: {.sc-iJCRrE .jCdxGr .sc-dPaNzc .gyljjx}
::: {.redoc-json}
`{`

-   ::: {.hoverable}
    [\"id\"]{.property .token .string}: [134]{.token .number}[,]{.token
    .punctuation}
    :::

-   ::: {.hoverable}
    [\"first\_name\"]{.property .token .string}: [\"Alice\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"last\_name\"]{.property .token .string}: [\"Smith\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"email\"]{.property .token .string}:
    [\"alice.smith\@gmail.com\"]{.token .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"mobile\"]{.property .token .string}: [\"347-321-1234\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"username\"]{.property .token .string}: [\"alicesmith\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"password\"]{.property .token .string}: [\"s3rewtwsdf\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"email\_verified\"]{.property .token .string}: [true]{.token
    .boolean}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"is\_active\"]{.property .token .string}: [true]{.token
    .boolean}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"created\_at\"]{.property .token .string}: [\"2023-09-12
    00:00:00\"]{.token .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"updated\_at\"]{.property .token .string}: [\"2023-09-12
    00:00:00\"]{.token .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"last\_login\"]{.property .token .string}: [\"2023-09-12
    00:00:00\"]{.token .string}
    :::

[}]{.token .punctuation}
:::
:::
:::
:::

</div>
:::
:::

</div>
:::
:::
:::

::: {#tag/users/operation/patch-users-userid .sc-eCApnc .liLqNm section-id="tag/users/operation/patch-users-userid"}
::: {#operation/patch-users-userid .sc-iCoGMd .gLxhOh section-id="operation/patch-users-userid"}
::: {.sc-hKFxyN .juinod}
[](#tag/users/operation/patch-users-userid){.sc-crzoAE .iUxAWq}Update User Information {#update-user-information-1 .sc-pNWdM .eftmgB}
--------------------------------------------------------------------------------------

::: {.sc-iGkqmO .hCTIhr}
::: {.sc-iJCRrE .sc-ciSkZP .jCdxGr .QGruV}
Modify user information, including first name, last name, email, mobile
number, password, and activation status.
:::
:::

<div>

##### path Parameters {#path-parameters-4 .sc-iqAclL .eONCmm}

+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcnRwz}[userid]{.property-name}  |                                   |
|                                   | <div>                             |
| ::: {.sc-                         |                                   |
| oeezt .sc-hhIiOg .dLCGMn .hIkHYw} | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
| required                          | .jrLlAa}[string]{.sc-laZMeE       |
| :::                               | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | The unique identifier of the      |
|                                   | user.                             |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+

</div>

##### Request Body schema: [application/json]{.sc-cBoqAE .eKyrDP} {#request-body-schema-applicationjson-3 .sc-iqAclL .eONCmm}

::: {.sc-iJCRrE .sc-ciSkZP .jCdxGr .QGruV}
Customize user information according to your requirements.
:::

+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcn                              |                                   |
| Rwz}[first\_name]{.property-name} | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bc                               |                                   |
| nRwz}[last\_name]{.property-name} | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcnRwz}[email]{.property-name}   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}[      |
|                                   | \<email\> ]{.sc-laZMeE .sc-jffHpj |
|                                   | .jWaWWE .cThoNa}                  |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | Providing a new email temporarily |
|                                   | sets the email verification       |
|                                   | status to false.                  |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcnRwz}[mobile]{.property-name}  |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | Providing a new email temporarily |
|                                   | sets the email verification       |
|                                   | status to false.                  |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .                                 |                                   |
| bcnRwz}[password]{.property-name} | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}[      |
|                                   | \<password\> ]{.sc-laZMeE         |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bc                               |                                   |
| nRwz}[is\_active]{.property-name} | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[boolean]{.sc-laZMeE      |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | [ Default: ]{.sc-laZMeE .jWaWWE}  |
|                                   | [true]{.sc-laZMeE .sc-ckTSus      |
|                                   | .jWaWWE .fElSEN}                  |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+

<div>

### Responses {#responses-6 .sc-fIxmyt .DvFer}

<div>

**200** []{.sc-jcwpoC .eDjFAZ}

User Updated

</div>

<div>

**404** []{.sc-jcwpoC .eDjFAZ}

User Not Found

</div>

<div>

**409** []{.sc-jcwpoC .eDjFAZ}

Email Already Taken

</div>

</div>
:::

::: {.sc-jSFjdj .sc-gKAaRy .gBjRyf .gcushC}
::: {.sc-EZqKI .fWsqvQ}
[patch]{.sc-fmdNqN .cDAiVX .http-verb .patch
type="patch"}[/users/{userid}]{.sc-jXcxbT .fCEUju}

::: {.sc-ljsmAU .flIrdF aria-hidden="true"}
::: {.sc-jlZJtj .fQkroN}
::: {.sc-iJCRrE .sc-ciSkZP .jCdxGr .lhENGb}
:::

::: {tabindex="0" role="button"}
::: {.sc-dTSzeu .dfUAUz}
http://localhost:8000/users/{userid}
:::
:::
:::
:::
:::

<div>

### Request samples {#request-samples-3 .sc-kEqXSa .iXmHCl}

::: {.sc-cxNHIi .gxohHo rttabs="true"}
-   [Payload]{#react-tabs-16}

::: {#react-tabs-17 .react-tabs__tab-panel .react-tabs__tab-panel--selected role="tabpanel" aria-labelledby="react-tabs-16"}
<div>

::: {.sc-Arkif .jojbRz}
[Content type]{.sc-cOifOu .hlhNtL}

::: {.sc-bBjRSN .kQSIAz}
application/json
:::
:::

::: {.sc-jgPyTC .dSaTNC}
::: {.sc-Arkif .jojbRz}
[Example]{.sc-cOifOu .hlhNtL}

::: {.sc-hiKfDv .sc-khIgEk .bycQNU .hLNtis}
Update First NameUpdate EmailUpdate Last Name & Date of BirthUpdate
PasswordUpdate First Name
:::
:::

<div>

::: {.sc-jNnpgg .esZIbL}
::: {.sc-giAqHp .hMPeqJ}
::: {.sc-carFqZ .UksDl}
Copy
:::
:::

::: {.sc-iJCRrE .jCdxGr .sc-dPaNzc .gyljjx}
::: {.redoc-json}
`{`

-   ::: {.hoverable}
    [\"first\_name\"]{.property .token .string}: [\"Rebecca\"]{.token
    .string}
    :::

[}]{.token .punctuation}
:::
:::
:::

</div>
:::

</div>
:::
:::

</div>

<div>

### Response samples {#response-samples-5 .sc-kEqXSa .iXmHCl}

::: {.sc-cxNHIi .gxohHo rttabs="true"}
-   [200]{#react-tabs-18}

::: {#react-tabs-19 .react-tabs__tab-panel .react-tabs__tab-panel--selected role="tabpanel" aria-labelledby="react-tabs-18"}
<div>

::: {.sc-Arkif .jojbRz}
[Content type]{.sc-cOifOu .hlhNtL}

::: {.sc-bBjRSN .kQSIAz}
application/json
:::
:::

::: {.sc-jgPyTC .dSaTNC}
::: {.sc-jNnpgg .esZIbL}
::: {.sc-giAqHp .hMPeqJ}
::: {.sc-carFqZ .UksDl}
Copy
:::
:::

::: {.sc-iJCRrE .jCdxGr .sc-dPaNzc .gyljjx}
::: {.redoc-json}
`{`

-   ::: {.hoverable}
    [\"id\"]{.property .token .string}: [13]{.token .number}[,]{.token
    .punctuation}
    :::

-   ::: {.hoverable}
    [\"first\_name\"]{.property .token .string}: [\"Rebecca\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"last\_name\"]{.property .token .string}: [\"Baker\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"email\"]{.property .token .string}:
    [\"rebecca\@gmail.com\"]{.token .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"username\"]{.property .token .string}: [\"rebecca\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"password\"]{.property .token .string}: [\"p\@s\$w0rd\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"mobile\"]{.property .token .string}: [\"347-876-5432\"]{.token
    .string}
    :::

[}]{.token .punctuation}
:::
:::
:::
:::

</div>
:::
:::

</div>
:::
:::
:::

::: {#tag/users/operation/post-users .sc-eCApnc .liLqNm section-id="tag/users/operation/post-users"}
::: {#operation/post-users .sc-iCoGMd .gLxhOh section-id="operation/post-users"}
::: {.sc-hKFxyN .juinod}
[](#tag/users/operation/post-users){.sc-crzoAE .iUxAWq}Create New User {#create-new-user-1 .sc-pNWdM .eftmgB}
----------------------------------------------------------------------

::: {.sc-iGkqmO .hCTIhr}
::: {.sc-iJCRrE .sc-ciSkZP .jCdxGr .QGruV}
Add a new user to your system effortlessly.
:::
:::

##### Request Body schema: [application/json]{.sc-cBoqAE .eKyrDP} {#request-body-schema-applicationjson-4 .sc-iqAclL .eONCmm}

::: {.sc-iJCRrE .sc-ciSkZP .jCdxGr .QGruV}
Create a new user with the specified details.
:::

+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcn                              |                                   |
| Rwz}[first\_name]{.property-name} | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bc                               |                                   |
| nRwz}[last\_name]{.property-name} | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcnRwz}[email]{.property-name}   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .bcnRwz}[mobile]{.property-name}  |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .                                 |                                   |
| bcnRwz}[username]{.property-name} | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| []{.sc-iemWCZ                     | <div>                             |
| .                                 |                                   |
| bcnRwz}[password]{.property-name} | <div>                             |
|                                   |                                   |
|                                   | []{.sc-laZMeE .sc-iNiQyp .jWaWWE  |
|                                   | .jrLlAa}[string]{.sc-laZMeE       |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}[      |
|                                   | \<password\> ]{.sc-laZMeE         |
|                                   | .sc-jffHpj .jWaWWE .cThoNa}       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ::: {.sc-i                        |
|                                   | JCRrE .sc-ciSkZP .jCdxGr .lhENGb} |
|                                   | :::                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+

<div>

### Responses {#responses-7 .sc-fIxmyt .DvFer}

<div>

**200** []{.sc-jcwpoC .eDjFAZ}

User Created

</div>

<div>

**400** []{.sc-jcwpoC .eDjFAZ}

Missing Required Information

</div>

<div>

**409** []{.sc-jcwpoC .eDjFAZ}

Email Already Taken

</div>

</div>
:::

::: {.sc-jSFjdj .sc-gKAaRy .gBjRyf .gcushC}
::: {.sc-EZqKI .fWsqvQ}
[post]{.sc-fmdNqN .ldMUmp .http-verb .post
type="post"}[/users]{.sc-jXcxbT .fCEUju}

::: {.sc-ljsmAU .flIrdF aria-hidden="true"}
::: {.sc-jlZJtj .fQkroN}
::: {.sc-iJCRrE .sc-ciSkZP .jCdxGr .lhENGb}
:::

::: {tabindex="0" role="button"}
::: {.sc-dTSzeu .dfUAUz}
http://localhost:8000/users
:::
:::
:::
:::
:::

<div>

### Request samples {#request-samples-4 .sc-kEqXSa .iXmHCl}

::: {.sc-cxNHIi .gxohHo rttabs="true"}
-   [Payload]{#react-tabs-20}

::: {#react-tabs-21 .react-tabs__tab-panel .react-tabs__tab-panel--selected role="tabpanel" aria-labelledby="react-tabs-20"}
<div>

::: {.sc-Arkif .jojbRz}
[Content type]{.sc-cOifOu .hlhNtL}

::: {.sc-bBjRSN .kQSIAz}
application/json
:::
:::

::: {.sc-jgPyTC .dSaTNC}
::: {.sc-jNnpgg .esZIbL}
::: {.sc-giAqHp .hMPeqJ}
::: {.sc-carFqZ .UksDl}
Copy
:::
:::

::: {.sc-iJCRrE .jCdxGr .sc-dPaNzc .gyljjx}
::: {.redoc-json}
`{`

-   ::: {.hoverable}
    [\"first\_name\"]{.property .token .string}: [\"David\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"last\_name\"]{.property .token .string}: [\"Gavin\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"email\"]{.property .token .string}:
    [\"davidg\@gmail.com\"]{.token .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"mobile\"]{.property .token .string}: [\"347-123-4567\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"username\"]{.property .token .string}: [\"davidg\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"password\"]{.property .token .string}:
    [\"s3cr3tp\@assw0rd\"]{.token .string}
    :::

[}]{.token .punctuation}
:::
:::
:::
:::

</div>
:::
:::

</div>

<div>

### Response samples {#response-samples-6 .sc-kEqXSa .iXmHCl}

::: {.sc-cxNHIi .gxohHo rttabs="true"}
-   [200]{#react-tabs-22}

::: {#react-tabs-23 .react-tabs__tab-panel .react-tabs__tab-panel--selected role="tabpanel" aria-labelledby="react-tabs-22"}
<div>

::: {.sc-Arkif .jojbRz}
[Content type]{.sc-cOifOu .hlhNtL}

::: {.sc-bBjRSN .kQSIAz}
application/json
:::
:::

::: {.sc-jgPyTC .dSaTNC}
::: {.sc-jNnpgg .esZIbL}
::: {.sc-giAqHp .hMPeqJ}
::: {.sc-carFqZ .UksDl}
Copy
:::
:::

::: {.sc-iJCRrE .jCdxGr .sc-dPaNzc .gyljjx}
::: {.redoc-json}
`{`

-   ::: {.hoverable}
    [\"id\"]{.property .token .string}: [12]{.token .number}[,]{.token
    .punctuation}
    :::

-   ::: {.hoverable}
    [\"first\_name\"]{.property .token .string}: [\"Bob\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"last\_name\"]{.property .token .string}: [\"Fellow\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"email\"]{.property .token .string}:
    [\"bob.fellow\@gmail.com\"]{.token .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"username\"]{.property .token .string}: [\"bobfellow\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"password\"]{.property .token .string}: [\"p\@s\$w0rd\"]{.token
    .string}[,]{.token .punctuation}
    :::

-   ::: {.hoverable}
    [\"mobile\"]{.property .token .string}: [\"347-123-0001\"]{.token
    .string}
    :::

[}]{.token .punctuation}
:::
:::
:::
:::

</div>
:::
:::

</div>
:::
:::
:::
:::

::: {.sc-ellfGf .bgakXB}
:::
:::
:::
