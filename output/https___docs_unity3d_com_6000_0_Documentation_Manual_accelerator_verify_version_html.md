* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-verify-version.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Caching assets](https://docs.unity3d.com/6000.0/Documentation/Manual/importing-caching-assets.html)
  * Verify the Unity Accelerator version


[](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-install-docker.html)
Install Unity Accelerator with Docker Hub
[](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-configure.html)
Configure Unity Accelerator in the Editor
# Verify the Unity Accelerator version
You can verify the Unity **Accelerator** The Unity Accelerator is an external tool that provides an asset cache that keeps copies of a team’s imported assets. The goal of the Accelerator is to speed up teamwork and reduce iteration time by coordinating asset sharing so that you don’t need to reimport portions of your project. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityAccelerator.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Accelerator) version from a client machine accessing a remote Unity Accelerator instance and also from the server machine. 
## Verify on a client machine
From the client, access the API agent health end point by visiting the following page from a browser: `http://[AcceleratorIP]:[AcceleratorPort]/api/agent-health`
Alternatively, examine the unity-accelerator.log file in the log folder of the Accelerators configuration directory. The sysinfo message displays the currently loaded Unity Accelerator version:
```
{"level":"info","ts":"2025-03-05T11:10:52.144Z","msg":"sysinfo","agent_id":"john.smith_id","agent_name":"john.smith","component":"agent","pid":91985,"agentversion":"v1.0.941+g6b39b61","goversion":"go1.15.4","os":"darwin","arch":"amd64","compiler":"gc","maxprocs":10,"numcpu":10}

```

The data is arranged in key-value pairs, and the `agentversion` key displays the current version `"agentversion":"v1.0.941+g6b39b61"`
## Verify on a server
From the Accelerator server you can use the Unity Accelerator application to report the version with `unity-accelerator --version`, or `unity-accelerator.exe --version` on Windows
On Windows, the Unity Accelerator application is usually installed under `C:\Program Files\Unity\accelerator`, and on macOS it is usually installed under `/Applications/Unity/accelerator` unless a different location was specified during install.
## Verify on Linux systems
For Unity Accelerator installations on Linux systems, all Linux executables have signature files that you can verify to ensure that no malicious entities have tampered with your downloaded Unity Accelerator version. 
You can verify the signature files with a trusted version of GnuPG. The following key signs the current release. The public key block with the key is available at <https://collab-accelerator.cloud.unity3d.com/>.
```
pub     rsa4096 2019-12-02
Key fingerprint = 9BC4 B04D F2E8 74E5 64AA 47E7 6D44 3B8B 002C F61F
uid       Unity Technologies ApS (Accelerator signing key) <sst-ops@unity3d.com>

```

To download the key to your GPG store, use one of the following commands:
```
$ gpg --keyserver https://collab-accelerator.cloud.unity3d.com/ --search-key "sst-ops@unity3d.com"

$ gpg --keyserver https://collab-accelerator.cloud.unity3d.com/ --recv-key 9BC4B04DF2E874E564AA47E76D443B8B002CF62F

```

To check the version of Unity Accelerator that you installed is original and unmodified, verify the file’s signature.
The Accelerator installation file comes with a signature file that’s available at <https://storage.googleapis.com/unity-accelerator-prd/unity-accelerator-installer.sig>. Use this signature file to verify the Accelerator installer:
```
$ gpg --verify unity-accelerator-installer.sig unity-accelerator-linux-x64-installer.run

```

Before trusting the key, compare the fingerprint with what is displayed in Forged or Untrusted keys. After trusting the key, the following is displayed:
```
gpg: Signature made Thu Jan 16 12:29:14 2020 PST
gpg:                using RSA key 9BC4B04DF2E874E564AA47E76D443B8B002CF61F
gpg: Good signature from "Unity Technologies ApS (Accelerator signing key) <sst-ops@unity3d.com>" [ultimate]

```

This means the signature is valid and that you trusted this key.
### Incorrect keys
If you don’t have the correct distribution key, the output of the previous commands will look as follows:
```
gpg: Signature made Thu Jan 16 12:29:14 2020 PST
gpg:                using RSA key 9BC4B04DF2E874E564AA47E76D443B8B002CF61F
gpg: Can't check signature: No public key

```

In this case, you must get the key using the previous instructions.
### Forged or untrusted keys
If you have a copy of the key with a valid signature, but either the key wasn’t marked as trusted or the key is a forgery, the output will look as follows:
```
gpg: Signature made Thu Jan 16 12:29:14 2020 PST
gpg:                using RSA key 9BC4B04DF2E874E564AA47E76D443B8B002CF61F
gpg: Good signature from "Unity Technologies ApS (Accelerator signing key) <sst-ops@unity3d.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 9BC4 B04D F2E8 74E5 64AA  47E7 6D44 3B8B 002C F61F

```

If the key has been forged, you must verify the fingerprint using the signature file. If the key isn’t marked as trusted, edit it to mark it as trusted. For more information, refer to <https://www.gnupg.org/gph/en/manual/x334.html>.
## Additional resources
  * [Command line arguments reference](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorCommandLineArguments.html#accelerator)
  * [Configure Unity Accelerator in the Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-configure.html)
  * [Stop and restart Unity Accelerator](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-stop-restart.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-install-docker.html)
Install Unity Accelerator with Docker Hub
[](https://docs.unity3d.com/6000.0/Documentation/Manual/accelerator-configure.html)
Configure Unity Accelerator in the Editor
