* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/iphone-playerSizeOptimization.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone.html)
  * [Developing for iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-developing.html)
  * [Optimize performance for iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone-performance.html)
  * Optimize the size of the iOS Player


[](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone-InternalProfiler.html)
Measure performance with the built-in profiler
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PluginsForIOS.html)
Native plug-ins for iOS
# Optimize the size of the iOS Player
There are two main ways to reduce the size of the built iOS Player: create a Release build within Xcode, or change the Stripping Level within Unity.
## Release build
It’s recommended to create final release builds within Xcode. Navigate to the menu bar and select **Product** > **Archive**. This option ensures the build has the correct release configuration and strips any debug symbols. After issuing this command, Xcode switches to the Organizer window Archives tab. For further information on how to calculate app size, and for other size-reducing tips, refer to [Reducing the size of my App](https://developer.apple.com/library/content/qa/qa1795/_index.html).
**Note** : It’s recommended to factor in a small margin for error when aiming for the over-the-air download limit. The current download limit is set at 200MB. However, starting with iOS 13, the app users have the option to override this limit to download apps larger than 200MB. 
## Managed code stripping
Unity removes unused or unreachable code during the build process through a technique called managed code stripping, which can significantly reduce the final size of your application. Refer to [managed code stripping](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-stripping.html) for more information.
**Note:** It can sometimes be difficult to determine which classes are getting stripped in error, even though the application requires them. You can often get useful information about this by running the stripped application on the [simulator](https://developer.apple.com/documentation/xcode/running-your-app-in-simulator-or-on-a-device) and checking the Xcode console for error messages.
## Reduce the build size
Use the following checklist to help reduce the size of your build: 
  * Enable **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression) for textures and minimize the number of uncompressed sounds. For more information, and tips on file size reduction, refer to [Reducing the file size of your build](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).
  * From the [**iOS Player settings**](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsiOS.html) window: 
    * Enable [**Strip Engine Code**](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsiOS.html#Optimization)
    * Set the script call optimization level to [**Fast but no exceptions**](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsiOS.html#Optimization)
    * Set the API Compatibility Level to [**.Net Standard**](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsiOS.html#Configuration)
  * Remove unnecessary code dependencies.
  * Avoid generic containers in combination with value types, including structs.


## Minimum Unity application size
If disabling size optimizations, it’s expected that an empty project might be around 20MB in the App Store. Using code stripping, an application containing an empty **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) can be reduced to less than 12MB in the App Store. However, the application must be zipped and have digital rights management (DRM) attached. 
## Increased application size in the Apple App Store
When publishing your app, Apple App Store service first encrypts the binary file and then compresses it via zip. Encryption increases the randomness of the code segment, and can increase the applications size before compression.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone-InternalProfiler.html)
Measure performance with the built-in profiler
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PluginsForIOS.html)
Native plug-ins for iOS
