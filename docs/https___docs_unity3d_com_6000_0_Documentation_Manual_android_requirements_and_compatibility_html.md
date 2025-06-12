* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-requirements-and-compatibility.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Introducing Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-introducing.html)
  * Android requirements and compatibility


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-introducing.html)
Introducing Android
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html)
Gradle for Android
# Android requirements and compatibility
Before you begin to develop an Android application in Unity, check Unity’s requirements and compatibility information for Android to make sure you’re aware of any limitations for developing a Unity application for this platform.
## Android support
Unity supports Android 6.0 “Marshmallow” (API level 23) and above. For more information, refer to [AndroidSdkVersions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidSdkVersions.html).
## Graphics API support
Android devices support [Vulkan](https://developer.android.com/ndk/guides/graphics) and [OpenGL ES](https://developer.android.com/guide/topics/graphics/opengl). This section contains information about the graphics APIs Unity supports for Android.
**Graphics API** | **Support**  
---|---  
**Vulkan** | Yes  
**OpenGL ES 1.0** | No  
**OpenGL ES 1.1** | No  
**OpenGL ES 2.0** | No  
**OpenGL ES 3.0** | Yes  
**OpenGL ES 3.1** | Yes  
**OpenGL ES 3.2** | Yes  
## Render pipeline compatibility
Not every [render pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) is compatible with Android due to hardware and graphics API limitations.
**Feature** | **Built-in Render Pipeline** | **Universal Render Pipeline** | **High Definition Render Pipeline** | **Custom Scriptable Render Pipeline**  
---|---|---|---|---  
**Android** | Yes | Yes | No | Yes  
## Manifest element attributes
This section contains compatibility information on [Android App Manifest element](https://developer.android.com/guide/topics/manifest/manifest-intro#reference) attributes.
  * For the [<Activity>](https://developer.android.com/guide/topics/manifest/activity-element.html) element, Unity only supports the `singleTask` [launchMode](https://developer.android.com/guide/topics/manifest/activity-element.html#lmode).


## Emulator compatibility
Unity doesn’t support Android emulators. To test your application, you can:
  * [Test on an Android device](https://docs.unity3d.com/6000.0/Documentation/Manual/android-debugging-on-an-android-device.html).
  * If you only need to test mobile input for your application, use [Unity Remote](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityRemote5.html)A downloadable app designed to help with Android, iOS and tvOS development. The app connects with Unity while you are running your project in Play Mode from the Unity Editor. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityRemote5.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#UnityRemote).
  * If you only need to test the appearance of an Android device, use the [Device Simulator](https://docs.unity3d.com/6000.0/Documentation/Manual/android-device-simulator.html).


## Texture compression
The standard texture **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression) formats on Android are [Ericsson Texture Compression (ETC)](https://en.wikipedia.org/wiki/Ericsson_Texture_Compression) and [Adaptable Scalable Texture Compression (ASTC)](https://www.khronos.org/opengl/wiki/ASTC_Texture_Compression). To target the widest range of Android devices, use one of these **texture compression** 3D Graphics hardware requires Textures to be compressed in specialized formats which are optimized for fast Texture sampling. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextureCompression) formats. Unity’s default texture compression format is ASTC. If an Android device doesn’t support the texture compression format you use for a texture, Unity decompresses the texture at runtime. This increases memory usage and decreases rendering speed.
A subset of Android devices support the DXT and PVRTC texture compression formats. These formats support textures with an alpha channel as well as high compression rates or high image quality. For digital distribution services that filter content based on texture compression format, it is best practice to create separate builds of your application for each texture compression format.
There are two ways to change the default texture compression format for your application:
  * In [Android Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html) with the **Texture compression formats** setting. For more information, refer to [texture compression targeting](https://docs.unity3d.com/6000.0/Documentation/Manual/android-distribution-google-play.html#texture-compression-targeting).
  * In [Android build settings](https://docs.unity3d.com/6000.0/Documentation/Manual/android-build-settings.html) with the **Texture Compression** setting. The default value for this is **Use**Player Settings** Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings)**.


The value you set in build settings has priority over the one you set in Player Settings. Use it to change the texture compression format for a particular build.
You can also customize the texture compression format for individual textures. The value you set for an individual **texture overrides** Platform-specific settings that allow you to set the resolution, file size with associated memory size requirements, pixel dimensions, and quality of your Textures for each target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextureOverrides) the default texture compression format value. For information on how to change the **texture format** A file format for handling textures during real-time rendering by 3D graphics hardware, such as a graphics card or mobile device. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextureFormat) of individual textures, see [Texture Importer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html).
## Playing video files
This section provides additional information for playing video files on Android:
  * To play video files on Android, use the [Video Player](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer.html) component. If your application tries to play a video file that the device doesn’t support, Unity doesn’t play the video.
  * You can use any resolution or number of audio channels so long as the target device supports them. **Note** : Not all devices support resolutions greater than 640 × 360.
  * Unity supports playback from uncompressed asset bundles. For [Android Pie](https://en.wikipedia.org/wiki/Android_Pie) and above, Unity supports playback from compressed asset bundles.
  * Unity doesn’t support native webM/VP8 transparency. To play VP8-encoded webM clips with transparency, transcode the clips to a supported format.
  * In Android versions prior to `6.0.1`, videos with transparency that have a higher resolution than the device support render **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) outside the supported resolution as white.
  * Unity reports format compatibility issues in the `adb logcat` output and prefixes them with `AndroidVideoMedia`. This file might display other device-specific error messages near the video format issues Unity reports. These device-specific errors aren’t visible to Unity and often explain what the compatibility issue is.


## 16 KB memory page size support
Unity supports devices with 16 KB memory page sizes, a feature introduced in Android 15. For more information about the feature, refer to the Android documentation on [Support 16 KB page sizes](https://developer.android.com/guide/practices/page-sizes?_gl=1*86rcxf*_up*MQ..*_ga*MTMxMTA4MTU5Ny4xNzM3OTk1NjU1*_ga_6HH9YJMN9M*MTczNzk5NTY1NC4xLjAuMTczNzk5NTY1NC4wLjAuMTA3NjE4ODIy).
Unity applications built for devices with 4 KB memory page size might not work on devices with 16 KB memory page size. To ensure your application is compatible with the devices that use 16 KB memory page size, consider the following key points:
  * Update Unity to 6000.0.38f1 or later version. Update the native **plug-ins** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in), rebuild, and resubmit your application to Google Play. The same application executable will be able to support devices with both 4 KB and 16 KB memory page sizes. For more information, refer to Android documentation on [Build your app with support for 16 KB devices](https://developer.android.com/guide/practices/page-sizes#build).
  * If your project contains a plug-in with a `.so` file that’s aligned to 4 KB instead of 16 KB, the Unity Editor displays a warning during the build process.
  * If your application uses third-party plug-ins or SDKs that link to native libraries, contact the plug-in creators to confirm that their native libraries are compatible with 16 KB page sizes. Update the relevant SDKs and resubmit your application.
  * For guidelines on testing your application on devices with 16 KB memory page sizes, refer to the Android documentation on [Enable 16 KB mode on a device using developer options](https://developer.android.com/guide/practices/page-sizes#developer-option).


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-introducing.html)
Introducing Android
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html)
Gradle for Android
