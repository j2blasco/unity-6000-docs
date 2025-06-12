* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Integrity.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Combining assets into bundles](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-section.html)
  * Downloading AssetBundles


[](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-optimizing.html)
Optimizing AssetBundles
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ScriptingAssets.html)
Scripting with assets
# Downloading AssetBundles
AssetBundles can be distributed with your application or downloaded from remote servers.
## Verifying AssetBundle downloads
When downloading AssetBundles, precautions are necessary to prevent data corruption and attacks from malicious actors. Data corruption in downloaded AssetBundles is a common cause of crashes on user devices and can require significant effort to resolve. While AssetBundles can’t contain executable code, altered serialized data could exploit vulnerabilities in your application code or the Unity runtime.
### Download using a secure protocol
Use [`UnityWebRequestAssetBundle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestAssetBundle.html) to download AssetBundles from the internet. Always use HTTPS in your URL, unless it’s for a local web server on the same machine. HTTP is insecure and susceptible to man-in-the-middle attacks.
### Cyclic redundancy checks (CRC)
Unity generates a 32-bit checksum during the AssetBundle build process, stored in the `.manifest` file, and accessible via [`BuildPipeline.GetCRCForAssetBundle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.GetCRCForAssetBundle.html). Use cyclic redundancy checks (CRC) to ensure AssetBundles haven’t been tampered with or corrupted. When downloading AssetBundles via `UnityWebRequestAssetBundle.GetAssetBundle`, provide the expected CRC value to prevent invalid AssetBundles from being [cached](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-caching).
If you handle AssetBundle downloads directly (outside Unity’s cache), perform integrity checks before using retrieved content. Optional parameters in the AssetBundle load APIs let you pass CRC values for validation. If the calculated CRC doesn’t match, the AssetBundle won’t load. For LZ4-compressed bundles, this check is expensive as it requires full decompression into RAM. LZMA-compressed bundles already require full decompression for loading, so CRC checks don’t add significant overhead. To avoid repeated checks during loads, validate the bundle once when it is retrieved and saved on the device. Refer to [AssetBundle compression formats](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundle-compression-formats) for more information.
**Important:**
  * Don’t use common hashing algorithms such as md5 for validating compressed AssetBundles. Unity may recompress AssetBundles without changing their content, which alters the file hash despite valid content. CRC values are calculated from uncompressed content and remain consistent across recompression.
  * The AssetBundle hash in the `.manifest` file, accessible via [`BuildPipeline.GetHashForAssetBundle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.GetHashForAssetBundle.html) is not a hash of the full file content. It serves as a version identifier and is unsuitable for file corruption detection.


### User-generated content
For user-generated content (UGC) distributed to other players, filter submissions to prevent inappropriate or malicious content. Don’t allow users to upload binary AssetBundle files directly. Instead, require them to upload source assets and build the AssetBundle files yourself. This process enables manual and automated filtering and allows you to rebuild AssetBundles for newer Unity versions if needed.
## AssetBundle caching
Unity’s built-in disk-based caching system prevents redundant downloads by storing AssetBundles downloaded via [`UnityWebRequestAssetBundle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestAssetBundle.html).
AssetBundles in the cache are automatically converted to LZ4 for optimal performance. If [`Caching.compressionEnabled`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.compressionEnabled.html) is `false`, bundles are stored uncompressed.
Use the [`Caching`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.html) class to manage cached AssetBundles (e.g., clearing or checking cache presence).
Use version/hash parameters when downloading AssetBundles to enable caching.
**Note** : On unsupported platforms such as Web, disk-based caching is unavailable, and all interactions are in-memory.
## Patching AssetBundles
To patch AssetBundles, download a new AssetBundle and replace the existing one. Using [`UnityWebRequestAssetBundle.GetAssetBundle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityWebRequestAssetBundle.GetAssetBundle.html) with a different version or hash parameter triggers the download of updated AssetBundles.
The main challenge is identifying which AssetBundles need replacement. A patching system must manage two lists:
  * Local AssetBundles: Currently downloaded bundles and their version info.
  * Server AssetBundles: Available bundles on the server and their version info.


The patching system compares these lists, re-downloading AssetBundles that are missing or have updated version information.
Unity does not support differential patching by default. `UnityWebRequestAssetBundle.GetAssetBundle` downloads entire files, even when using the built-in cache system. Developers needing differential patching must implement custom downloaders. Since Unity orders AssetBundle data deterministically, patch files for rebuilt AssetBundles can be much smaller. Uncompressed bundles or those using chunk-based **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression) (LZ4) are more patch-efficient than fully compressed bundles (LZMA).
For custom systems, most developers use standard formats such as JSON for AssetBundle file lists and common tools such as [.NET cryptography APIs](https://learn.microsoft.com/en-us/dotnet/standard/security/cryptography-model) to compute file content hashes. These hashes can act as version identifiers, though traditional version numbers are an alternative if supported by build systems.
## Additional resources
  * [`UnityWebRequestAssetBundle` API documentation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestAssetBundle.html)
  * [`Caching` API documentation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.html)
  * [Loading assets from AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Native.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-optimizing.html)
Optimizing AssetBundles
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ScriptingAssets.html)
Scripting with assets
