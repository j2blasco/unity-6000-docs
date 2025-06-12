* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-distribution-google-play.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Building and delivering for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-building-and-delivering.html)
  * [Digital distribution services for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-distribution.html)
  * Delivering to Google Play


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-distribution.html)
Digital distribution services for Android
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dedicated-server.html)
Dedicated Server
# Delivering to Google Play
This page contains information about Google Play-specific delivery requirements and considerations.
For information on how to publish your application on Google Play, see [Google Play](https://developer.android.com/distribute/google-play).
## Delivery requirements
Google Play has requirements an application must fulfil before you publish it. This section describes Google Play-specific requirements and explains how to meet them.
### Android App Bundle
Google Play requires new apps to be an [Android App Bundle](https://developer.android.com/guide/app-bundle) (AAB) instead of an **APK** The Android Package format output by Unity. An APK is automatically deployed to your device when you select File > Build & Run. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/android-BuildProcess.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#APK). For information on why, refer to [The future of Android App Bundles is here](https://android-developers.googleblog.com/2021/06/the-future-of-android-app-bundles-is.html).
To configure an application to be an AAB:
  1. Open the **Build Profiles** window (menu: **File** > **Build Profiles**).
  2. From the list of platforms in the **Platforms** panel, select **Android**.
  3. Select [Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings) for Android.
  4. In the **Publishing Settings** section, enable **Split Application Binary**.
  5. From the list of platforms in the **Platform** pane, select **Android**.
  6. On the **Build Profiles** window, under **Platform Settings** section, enable **Build App Bundle (Google Play)**. If you want to [export the project](https://docs.unity3d.com/6000.0/Documentation/Manual/android-export-process.html) and build it in Android Studio, enable **Export Project** then enable **Export for App Bundle**.
**Notes** : 
     * **Build App Bundle (Google Play)** setting is visible only if you disable **Export Project** setting.
     * Make sure the ****Development Build** A development build includes debug symbols and enables the Profiler. [More info](https://docs.unity.com/devops/en/manual/build-target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DevelopmentBuild)** setting is disabled as otherwise the application upload might fail.


Now when you [build the application](https://docs.unity3d.com/6000.0/Documentation/Manual/android-BuildProcess.html#building), Unity builds the application as an AAB.
### Application size
Google Play limits the install size of applications. The following table describes the size limitations Google Play has for each application type:
**Application type** | **Size limitation**  
---|---  
**APK** | If you [split the application binary](https://docs.unity3d.com/6000.0/Documentation/Manual/android-optimize-distribution-size.html#splitting-the-application-binary) or use a custom [expansion file](https://docs.unity3d.com/6000.0/Documentation/Manual/android-OBBsupport.html), the APK must be smaller than 100MB and the expansion file must be smaller than 2GB. Otherwise, the APK must be smaller than 100MB.  
**AAB** | If you split the application binary or use custom [asset packs](https://docs.unity3d.com/6000.0/Documentation/Manual/play-asset-delivery.html), the base module inside the AAB must be smaller than 200MB and the asset packs must fit the file sizes described in [Android’s Download Size Limits](https://support.google.com/googleplay/android-developer/answer/9859372#size_limits) documentation. Otherwise, the AAB must be smaller than 200MB.  
For information on how to optimize the install size of your application, refer to [Optimize distribution size](https://docs.unity3d.com/6000.0/Documentation/Manual/android-optimize-distribution-size.html).
### Symbols file size
Google Play limits the size of the symbols package or the embedded symbols within an Android App Bundle. The symbols files might be rejected if their file size exceeds this limit. Unity displays a warning if your symbols package exceeds the size limit specified in the **Symbols size threshold** in the Android Player Settings.
### Texture **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression) targeting
[Texture compressions targeting](https://developer.android.com/guide/playcore/asset-delivery/texture-compression) is a feature of Android App Bundles that helps Google Play to generate and serve optimized APKs for different devices. If you enable it, Unity includes texture assets formatted with different compression formats in any Android App Bundles that it builds. When a device installs the application from Google Play, the APKs that the device receives contain texture assets that use the optimal **texture compression** 3D Graphics hardware requires Textures to be compressed in specialized formats which are optimized for fast Texture sampling. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextureCompression) format for the device.
Texture compression targeting also automatically enables the [split application binary](https://docs.unity3d.com/6000.0/Documentation/Manual/android-optimize-distribution-size.html#splitting-the-application-binary) feature and generates an [install-time asset pack](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-in-unity.html#generated-asset-packs) called **UnityTextureCompressionsAssetPack**. This asset pack contains common resources and assets required by the first **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). When texture compression targeting is disabled, Unity packs these assets into the [base module](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-in-unity.html). This means that enabling texture compression targeting reduces the size of the base module. This can be important because the base module has a size limit of 200MB. For more information on how Unity configures asset packs, refer to [Asset packs in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/android-asset-packs-in-unity.html).
To enable texture compression targeting:
  1. Open the [Build Profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettings.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile) window (menu: **File** > **Build Profiles**).
  2. Select [Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html) for the Android platform.
  3. In the **Other Settings** > **Rendering** section, find **Texture Compression Formats** and add all required texture compression formats to it. The first texture compression format in this list is the [default format](https://developer.android.com/guide/playcore/asset-delivery/texture-compression#select-default-format).  
**Note** : You can also use the `PlayerSettings.Android.textureCompressionFormats` API to assign the required texture compression formats.
  4. Open [Build Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettings.html).
  5. On the **Build Profiles** window, select **Asset Import Overrides** and set **Texture Compression** to a value other than **Force Uncompressed**.


**Note** : When Texture compression targeting is enabled, Unity disables and ignores the **Texture Compression** [Android build settings](https://docs.unity3d.com/6000.0/Documentation/Manual/android-build-settings.html) which means you can’t use this setting to override the texture compression format for a build.
If you don’t enable Android App Bundles and [export](https://docs.unity3d.com/6000.0/Documentation/Manual/android-export-process.html) or build your application as an APK, Unity only uses the first texture compression format in the **Texture Compression Formats** list.
If you want some texture assets to use specific texture compression formats, you can override their texture compression format. The value you set for an individual **texture overrides** Platform-specific settings that allow you to set the resolution, file size with associated memory size requirements, pixel dimensions, and quality of your Textures for each target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextureOverrides) the default texture compression format and the optimal format that Google Play would select for specific target devices. For information on how to change the **texture format** A file format for handling textures during real-time rendering by 3D graphics hardware, such as a graphics card or mobile device. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextureFormat) of individual textures, refer to [Texture Importer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html).
### 64-bit Architecture
Google Play requires applications to support 64-bit architecture. For more information, refer to [Support 64-bit architectures](https://developer.android.com/distribute/best-practices/develop/64-bit). To make your application support 64-bit architecture:
  1. Open the **Build Profiles** window (menu: **File** > **Build Profiles**).
  2. From the list of platforms in the **Platforms** panel, select **Android** or [create a build profile](https://docs.unity3d.com/6000.0/Documentation/Manual/create-build-profile.html) for the **Android** platform.
  3. Select [Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html).
  4. In the **Other Settings** section, enable **ARM64**.   
**Note** : You can enable this setting only if you set your project’s [Scripting back end](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html) to [IL2CPP](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#IL2CPP).


### Target API
Google Play requires applications to support a minimum target API. For information on what the current minimum target API is, refer to [Meet Google Play’s target API level requirement](https://developer.android.com/distribute/best-practices/develop/target-sdk).
To change your application’s target API:
  1. Open [Android Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html).
  2. In the **Other Settings** > **Identification** section, set **Target API Level** to at least the target API level that Google Play requires.


### Report App Dependencies
Google Play can check the Package Manager and **Asset Store** A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStore.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AssetStore) packages that your application uses for known certification failures. It does this automatically after you upload your application to the Play Store and before the main certification process begins. This helps to identify issues with your application’s dependencies quickly without running the full certification process. If Google Play finds issues, it reports them to you via the Play Store Console along with details about the issues and how you can fix them before you submit the application again.
To report dependencies:
  1. Select **Edit** > **Project Settings**.
  2. In the Project settings window, select the **Player** tab, then open [Android Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html):  
![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/android-player-settings-tab.png)
  3. In the **Publishing Settings** section, check the **Report Dependencies in App Bundle** box to enable collection and reporting of dependencies to Google Play.


### App signature
Google Play requires applications to be signed. For information on how to sign your application, refer to [Android Keystore Manager](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-manager.html).
## Considerations
This section contains Google Play-specific considerations to be aware of before you publish an application to Google Play.
### Best practice checklist
To help launch an Android application successfully, Android’s documentation includes a best practice checklist of processes to follow. Refer to [Launch checklist](https://developer.android.com/distribute/best-practices/launch/launch-checklist).
### Public symbols
If your application crashes on a device, Google can use a [symbols package](https://docs.unity3d.com/6000.0/Documentation/Manual/android-symbols.html) to make a native stacktrace human-readable on the [Android Vitals](https://developer.android.com/topic/performance/vitals) dashboard. It’s best practice to generate a [public symbols](https://docs.unity3d.com/6000.0/Documentation/Manual/android-symbols.html#public-symbols) package for your application and upload it to Google Play. For information on how to do this, refer to [Generating a symbols package](https://docs.unity3d.com/6000.0/Documentation/Manual/android-symbols.html#generating-a-symbols-package).
### Deobfuscation file
Similar to symbol files, Unity can produce a deobfuscation file if you apply minification to your application build. For more information on applying minification, refer to [Android Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html#minify). A deobfuscation file is automatically generated as a mapping file in the same location as your application build.
If you apply minification, it’s best practice to upload the deobfuscation file when publishing your application on Google Play. A deobfuscation file deciphers the method names in the stack trace, allowing you to identify and resolve the exact cause of the application crashes. For more information, refer to Google’s documentation on [Deobfuscate or symbolicate crash stack traces](https://support.google.com/googleplay/android-developer/answer/9848633)
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-distribution.html)
Digital distribution services for Android
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dedicated-server.html)
Dedicated Server
