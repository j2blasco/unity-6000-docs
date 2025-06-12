* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-assetbundles.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)
  * [Build and distribute a Web application](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-building-distribution.html)
  * AssetBundles in Web


[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-building.html)
Web Build folder
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-distributionsize-codestripping.html)
Distribution size and code stripping
# AssetBundles in Web
**Note** : Unity’s [Addressables system](https://docs.unity3d.com/Packages/com.unity.addressables@latest?subfolder=/manual/index.html) is the recommended approach for asset loading. The following content applies only if you use AssetBundles directly.
As all asset data must be pre-downloaded before your content starts, consider moving assets out of your main data files and into [AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundlesIntro.html). Doing so creates a smaller loader **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) that loads quickly, while AssetBundles dynamically load assets on-demand as the user proceeds through your content. AssetBundles also help with [Asset data memory](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-memory.html) management: You can unload asset data from memory for assets that you don’t need any more by calling [AssetBundle.Unload](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.Unload.html).
The following considerations apply when using AssetBundles on the Web platform:
  * When you use class types in your AssetBundle that aren’t used in your main build, Unity might strip the code for those classes from the build. This can cause a fail when trying to load assets from the AssetBundle. Use [BuildPlayerOptions.assetBundleManifestPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions-assetBundleManifestPath.html) to fix that issue, and refer to [Distribution size and code stripping](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-distributionsize-codestripping.html) for other options.
  * The **WebGL** A JavaScript API that renders 2D and 3D graphics in a web browser. The Unity Web build option allows Unity to publish content as JavaScript programs which use HTML5 technologies and the WebGL rendering API to run Unity content in a web browser. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#WebGL) graphics API doesn’t support threading. As HTTP downloads become available only after they’re downloaded, Unity Web platform builds need to decompress AssetBundle data on the main thread after the download is complete, blocking the main thread. To avoid this interruption, [LZMA AssetBundle compression](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-compression-format.html) isn’t available for AssetBundles on Web. AssetBundles are compressed using LZ4 instead, which is de-compressed efficiently on-demand. If you need smaller **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression) sizes than LZ4 delivers, configure your web server to use gzip or Brotli compression (on top of LZ4 compression) on your AssetBundles. Refer to [Deploying compressed builds](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-deploying.html) for more information on how to do this.
  * The Web platform doesn’t support file-system-based AssetBundle caching with [UnityWebRequestAssetBundle.GetAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestAssetBundle.GetAssetBundle.html). Instead the browser caches the WebRequest responses; refer to [Cache behavior in Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-caching.html) for details. This means that the entire AssetBundle file is held in memory when an AssetBundle loads, and you must promptly unload unused AssetBundles, especially when they’re large.


## Additional resources
  * [Addressables package](https://docs.unity3d.com/Packages/com.unity.addressables@latest?subfolder=/manual/index.html)
  * [Distribution size and code stripping](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-distributionsize-codestripping.html)
  * [Optimize your Web build](https://docs.unity3d.com/6000.0/Documentation/Manual/web-optimization.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-building.html)
Web Build folder
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-distributionsize-codestripping.html)
Distribution size and code stripping
