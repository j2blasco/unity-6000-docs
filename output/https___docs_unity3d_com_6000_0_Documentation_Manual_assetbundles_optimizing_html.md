* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-optimizing.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Combining assets into bundles](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-section.html)
  * Optimizing AssetBundles


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Dependencies.html)
Handling dependencies between AssetBundles
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Integrity.html)
Downloading AssetBundles
# Optimizing AssetBundles
Loading AssetBundles can consume memory depending on **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression) formats and access patterns.
## Temporary in-memory AssetBundles
Unity manages memory efficiently, but temporary in-memory AssetBundles are created in the following scenarios:
  * LZMA-compressed bundles loaded via `AssetBundle.LoadFromFile`, `LoadFromMemory`, or `LoadFromStream` APIs.
  * AssetBundles downloaded without a version or hash.


Temporary files exist until reads complete and `AssetBundle.Unload` is called.
### Caching considerations
  * **LZ4 Default** : Temporary in-memory bundles use LZ4 when `Caching.compressionEnabled` is `true`.
  * **Uncompressed** : When `false`, temporary bundles are uncompressed, potentially increasing RAM usage.


## CRC checks and performance
[CRC checks](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Integrity.html) for chunk-based (LZ4) files do not require full-file decompression but may affect load times.
CRC checks for LZMA files incur no additional cost, as full decompression is inherent. For more information, refer to [Downloading AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Integrity.html).
## Memory Profiler and AssetBundles
Use [Memory Profiler](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest) to monitor memory usage and optimize AssetBundle loading workflows.
## Additional resources
  * [Handling dependencies between AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Dependencies.html)
  * [Loading assets from AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Native.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Dependencies.html)
Handling dependencies between AssetBundles
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Integrity.html)
Downloading AssetBundles
