* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-compression-format.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Combining assets into bundles](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-section.html)
  * [Creating AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-creating.html)
  * AssetBundle compression formats


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Build-MultiProcess.html)
Build AssetBundles in parallel processes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-file-format.html)
AssetBundle file format reference
# AssetBundle compression formats
AssetBundle files are an archive format that contains the following structures:
  * A small header data structure. This is never compressed.
  * A content section containing its virtual files, which you can optionally compress.


You can compress AssetBundle files in the following formats:
  * [Full file LMZA compression](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-compression-format.html#lzma-compression).
  * [Chunk-based LZ4 compression](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-compression-format.html#l4z-compression).
  * [Uncompressed format](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-compression-format.html#uncompressed-format).


By default, Unity compresses the content section with LZMA and caches AssetBundles with LZ4.
Because different data compresses with different size savings, it’s best practice to rebuild your project with each supported option and measure the size difference. 
If you download and store data with a custom caching solution you can use [`AssetBundle.RecompressAssetBundleAsync`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.RecompressAssetBundleAsync.html) to change **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression), for example to convert LZMA format AssetBundles to uncompressed or LZ4 format after download.
## LZMA compression
LZMA compresses the entire content section of the AssetBundle file as a single stream. This full content approach results in smaller file sizes than chunk-based LZ4 compression. LZMA is the preferred format for AssetBundles downloaded from a Content Delivery Network (CDN). 
However, you must decompress the entire file into RAM to read an asset from archives compressed with LZMA. This approach works best when an AssetBundle contains assets that you want to load all at once. For example, packaging all assets for a character or **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) in one AssetBundle. 
LZMA is the format used when calling `BuildPipeline.BuildAssetBundles` with no specific compression specified, for example `BuildAssetBundleOptions.None`.
**Note:** The Web platform doesn’t support LZMA compression. Use LZ4 compression instead. For more information, refer to [AssetBundles in Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-assetbundles.html).
## L4Z compression
LZ4 uses a chunk based algorithm which decompresses the AssetBundle in chunks. While writing the AssetBundle, Unity individually compresses each 128 KB chunk of the content before saving it. This approach means the total AssetBundle file size is larger than LZMA compression. However, you can selectively retrieve and load just the chunks needed for a requested object, rather than decompressing the entire AssetBundle. 
LZ4 has comparable loading times to uncompressed bundles with the added benefit of reduced size on disk. This is the format preferred by the [AssetBundle cache](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Integrity.html#assetbundle-caching), and it can also be a good choice for AssetBundles that you distribute as part of your installation or in other cases where size isn’t important. 
To use this format, specify the flag [`BuildAssetBundleOptions.ChunkBasedCompression`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.ChunkBasedCompression.html) when calling `BuildPipeline.BuildAssetBundles`.
## Uncompressed format
You can build AssetBundles so that the data is completely uncompressed. This creates a larger file download size, but faster load times once downloaded because no decompression is required. Uncompressed AssetBundles are helpful if only a few objects are loaded out of a larger AssetBundle. 
Uncompressed AssetBundles are 16-byte aligned. To build uncompressed AssetBundles, specify the flag [`BuildAssetBundleOptions.UncompressedAssetBundle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.UncompressedAssetBundle.html) when calling `BuildPipeline.BuildAssetBundles`.
## Addtional resources
  * [Optimizing AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-optimizing.html)
  * [Downloading AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Integrity.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Build-MultiProcess.html)
Build AssetBundles in parallel processes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-file-format.html)
AssetBundle file format reference
