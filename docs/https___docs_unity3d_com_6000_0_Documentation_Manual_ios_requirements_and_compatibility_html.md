* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ios-requirements-and-compatibility.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone.html)
  * [Introducing iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-introducing.html)
  * iOS requirements and compatibility


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-introducing.html)
Introducing iOS
[](https://docs.unity3d.com/6000.0/Documentation/Manual/how-unity-builds-ios-applications.html)
How Unity builds iOS applications
# iOS requirements and compatibility
Learn about the system requirements and compatibility information for iOS to make sure you’re aware of any limitations for developing a Unity application for this platform.
## iOS version support
Unity supports iOS 13 and above. For more information, see [`PlayerSettings.iOS-targetOSVersionString`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.iOS-targetOSVersionString.html).
## Xcode version support
When developing for iOS, it’s recommended to use Xcode version 15+. For more information, refer to [Xcode](https://developer.apple.com/support/xcode/).
## Graphics API support
iOS devices support [Metal](https://developer.apple.com/documentation/metal). For more information, see [Metal Graphics API](https://docs.unity3d.com/6000.0/Documentation/Manual/Metal.html).
## Audio compression
Unity supports importing a variety of source format sound files. However, when importing these files (with the exception of tracker files), they are always re-encoded to the build target format. By default, this format is Vorbis, though this can be overridden per platform to other formats (ADPCM, MP3, etc.) if required. Vorbis playback provides better **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression) and quality for iOS compared with MP3 playback.
## ASTC and PVRTC instead of DXT texture compression
Unity iOS doesn’t support DXT textures. Instead, ASTC, PVRTC, ETC2, and ETC **texture compression** 3D Graphics hardware requires Textures to be compressed in specialized formats which are optimized for fast Texture sampling. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextureCompression) are natively supported by iPhone and iPad devices. For more information about iOS **texture formats** A file format for handling textures during real-time rendering by 3D graphics hardware, such as a graphics card or mobile device. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextureFormat), refer to [Texture Import Settings window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html) and [Choose a GPU texture format by platform](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-choose-format-by-platform.html#ios-and-tvos). 
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-introducing.html)
Introducing iOS
[](https://docs.unity3d.com/6000.0/Documentation/Manual/how-unity-builds-ios-applications.html)
How Unity builds iOS applications
