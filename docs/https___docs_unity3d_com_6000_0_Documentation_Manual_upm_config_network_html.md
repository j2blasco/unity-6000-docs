* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/upm-config-network.html

  * [Packages and package management](https://docs.unity3d.com/6000.0/Documentation/Manual/PackagesList.html)
  * [Package Manager configuration](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-config.html)
  * Configure your network for Package Manager


[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-config-files.html)
Configuration files
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CustomPackages.html)
Create custom packages
# Configure your network for Package Manager
Use these procedures to:
  * [Configure your firewall settings](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-config-network.html#Firewall) so that Unity has access to the Package Manager registry server.
  * [Configure your proxy server](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-config-network.html#Proxy), either by setting environment variables or adding custom certificate authority (CA) certificates.


## Configuring your firewall
To ensure that the Unity Package Manager can access the domains it uses, you must add the domains to your firewall’s safe list.
For a complete list of these domains, and all domains that the Unity Editor requires, refer to [Endpoints that Unity applications access](https://docs.unity3d.com/6000.0/Documentation/Manual/ent-proxy-exception-list.html#endpoints-unity). You can either use the list to add entire domains, or use the table to selectively add subdomains.
Refer to your operating system’s help to learn how to add a domain name to the firewall’s safe list.
## Configuring your proxy server
When using a proxy server, configure the `HTTP_PROXY` and `HTTPS_PROXY` environment variables for the Unity Package Manager to use when performing requests against the Unity package registry. For more information, refer to [Use environment variables to identify your proxy server](https://docs.unity3d.com/6000.0/Documentation/Manual/ent-proxy-env-vars.html).
You can set these variables globally (either system or user variables) according to your operating system. Alternatively, you can [create a command file to set these environment variables and launch the Hub](https://docs.unity3d.com/6000.0/Documentation/Manual/ent-proxy-cmd-file.html).
For environments where you are behind a proxy server using a certificate that Package Manager doesn’t recognize, you can [configure a custom certificate authority](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-config-network.html#SSL).
### Custom certificate authority
In some organizations, users can only access the internet through a proxy server. Some proxies unpack the HTTPS content and repack it with their own SSL certificate. Unity Package Manager’s underlying HTTPS layer sometimes rejects these certificates because it doesn’t recognize the certificate authority that emitted them. When this happens, the Package Manager treats the connection as a possible machine-in-the-middle attack (MITM). This means that you can’t use many features in Unity, including the Package Manager, unless you configure additional SSL certificate authorities to allow these certificates.
To configure additional SSL certificate authorities:
  1. Locate the [`upmconfig.toml` global configuration file](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-config-files.html). If the file doesn’t already exist, create an empty text file.
  2. Create a text file with one or more certificates for custom certificate authorities. The file must consist of one or more trusted certificates in the Privacy-Enhanced Mail (PEM) format. For example:
```
-----BEGIN CERTIFICATE-----
MIIC+zCCAeOgAwIBAgIJAO0U6hVJnbvjMA0GCSqGSIb3DQEBBQUAMBQxEjAQBgNV
BAMMCWxvY2FsaG9zdDAeFw0xOTAzMTIwMTIxMzRaFw0yOTAzMDkwMTIxMzRaMBQx
(additional lines omitted for conciseness)
LFwHSUdqk0lJK4b0mCwyTHNvYO1IDziE5EKwfuaKVgOa62iCHVahgIVa+een4EfS
hCCr3M3cq11Mi+mnRi1scxxrOno4OEEChWg2szZLlxBrkVJllrrq620XJ6RLB/8=
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
MIIDtzCCAp+gAwIBAgIQDOfg5RfYRv6P5WD8G/AwOTANBgkqhkiG9w0BAQUFADBl
MQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3
(additional lines omitted for conciseness)
H2sMNgcWfzd8qVttevESRmCD1ycEvkvOl77DZypoEd+A5wwzZr8TDRRu838fYxAe
+o0bJW1sj6W3YQGx0qMmoRBxna3iw/nDmVG3KwcIzi7mULKn+gpFL6Lw8g==
-----END CERTIFICATE-----

```

  3. Save this file to the same folder as the global configuration file if possible, although Unity supports any location on the file system.
  4. In the global configuration file, add the **caFile** key and set its value as an absolute file path to your PEM file. **Important** : When setting Windows paths in TOML files, use forward slashes (`/`) or double backslashes (`\\`). Don’t use single backslashes (`\`) because they’re special characters which mark escape sequences and can cause TOML parsing errors.
**Windows example**
```
caFile = "C:\\ProgramData\\Unity\\config\\cert.pem"

```

**macOS and Linux example**
```
caFile = "/etc/cert.pem"

```



## Additional resources
  * [Using Unity through web proxies](https://docs.unity3d.com/6000.0/Documentation/Manual/ent-proxy-autoconfig.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-config-files.html)
Configuration files
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CustomPackages.html)
Create custom packages
