* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-manage.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * [Android application size restrictions](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-size-restrictions.html)
  * [Play Asset Delivery](https://docs.unity3d.com/6000.0/Documentation/Manual/play-asset-delivery.html)
  * Manage asset packs at runtime


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-create-custom.html)
Create a custom asset pack
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-graphics.html)
Graphics for Android
# Manage asset packs at runtime
Unity provides [APIs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.html) to manage asset packs at runtime. They use Google’s PlayCore API, which means they have the same limitations as PlayCore, and can’t manage `install-time` asset packs. Using the PlayCore API also means your application requires the [PlayCore](https://developer.android.com/guide/playcore) **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in). If your project has asset packs, either custom asset packs or Unity-generated asset packs, Unity automatically adds the PlayCore dependency to the application’s manifest.
The way you download asset packs and access their assets depends on the asset pack delivery mode. There are three asset pack delivery modes:
  * `install-time`: Google Play automatically downloads `install-time` asset packs when the device installs the application. Google Play considers these asset packs to be part of the base application, and an end user can’t uninstall them without uninstalling the entire application. The PlayCore API doesn’t handle `install-time` asset packs, which means that you can’t check the status, request to download, or remove `install-time` asset packs. You also can’t directly access assets inside of these asset packs, except streaming assets in Unity-generated `install-time` asset packs. To access streaming assets, use [Application.streamingAssetsPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-streamingAssetsPath.html) to get the path to streaming assets location, then use [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) to access assets in that path. If you create a custom asset pack, you can’t access assets inside it using standard file APIs. Instead, use [Android’s AssetManager APIs](https://developer.android.com/guide/playcore/asset-delivery/integrate-java#install-time-delivery).
  * `fast-follow`: Google Play automatically starts to download `fast-follow` asset packs after it installs the application. However, it’s possible that not all `fast-follow` asset packs are available on the first time the application launches. To check the status and download `fast-follow` asset packs, refer to [Download asset packs](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-manage.html#download-asset-packs).
  * `on-demand`: Google Play doesn’t automatically download `on-demand` asset packs. You have to manually start the download. For information on how to do this, refer to [Download asset packs](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-manage.html#download-asset-packs).


For more information about delivery modes, refer to [Delivery modes](https://developer.android.com/guide/playcore/asset-delivery#delivery-modes).
## Download asset packs
If your application uses `fast-follow` or `on-demand` asset packs, the device must download these asset packs before the application can access assets inside of them. To check the status of asset packs and download them if they’re not on the device, you must first know the name of each asset pack. To get the names of Unity-generated asset packs, call [AndroidAssetPacks.GetCoreUnityAssetPackNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.GetCoreUnityAssetPackNames.html). There is no runtime API to get the names of [custom asset packs](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-in-unity.html#custom-asset-packs) so you must keep track of them yourself. You set the name of custom asset packs at build time; it’s the name of the directory.
After you have the names of your asset packs, to check the status of each asset pack, call [AndroidAssetPacks.GetAssetPackStateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.GetAssetPackStateAsync.html), passing in the asset pack name. This returns the status of the asset pack you query, and you can use the result to determine whether you need to download the asset pack. If you want to quickly query the status of every Unity-generated asset pack, you can use [AndroidAssetPacks.coreUnityAssetPacksDownloaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks-coreUnityAssetPacksDownloaded.html). This helps you to ensure that every Unity-generated asset pack is available before you load any **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) other than the first one or try to access other resources that Unity handles.
For every asset pack you need to download, call [AndroidAssetPacks.DownloadAssetPackAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.DownloadAssetPackAsync.html), passing in the asset pack name. While the asset pack downloads, monitor the download status because downloads can pause or fail. There are two ways to do this:
  * Periodically check the [DownloadAssetPackAsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.DownloadAssetPackAsyncOperation.html) instance that AndroidAssetPacks.DownloadAssetPackAsync returns.
  * Use the version of [AndroidAssetPacks.DownloadAssetPackAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPacks.DownloadAssetPackAsync.html) that takes a callback as its second parameter. The callback you pass in must take an [AndroidAssetPackInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidAssetPackInfo.html) as a parameter that you can use to determine the state of the download.


## Additional resources
  * [Asset packs in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-in-unity.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-create-custom.html)
Create a custom asset pack
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-graphics.html)
Graphics for Android
