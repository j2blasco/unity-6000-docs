* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/VideoSources-FileCompatibility.html

  * [Video and cutscenes](https://docs.unity3d.com/6000.0/Documentation/Manual/Video.html)
  * [Video sources](https://docs.unity3d.com/6000.0/Documentation/Manual/video-sources.html)
  * Video file compatibility


[](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoSources-VideoFiles.html)
Understanding video files
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoClip.html)
Video Clip Importer reference
# Video file compatibility
You can import many video file formats into Unity. Unity stores imported video files as [VideoClip](https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoClip.html) assets.
For Unity to preview video files, the files must be compatible with the platform where you run the Unity Editor. Your files must also be compatible with the target build platforms. Unity provides options for transcoding files to commonly supported formats, but you can also manage compatibility yourself. See [Compatibility with target platforms](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoSources-FileCompatibility.html#CompatibilityWithTargetPlatforms) below for more information.
## Compatibility with Editor platforms
Video source files must use a format that your Editor platform supports. Each platform supports different video file formats.
Extension | Windows | macOS | Linux  
---|---|---|---  
.asf | ✓ |  |   
.avi | ✓ |  |   
.dv | ✓ | ✓ |   
.m4v | ✓ | ✓ |   
.mov | ✓ | ✓ |   
.mp4 | ✓ | ✓ |   
.mpg | ✓ | ✓ |   
.mpeg | ✓ | ✓ |   
.ogv | ✓ | ✓ | ✓  
.vp8 | ✓ | ✓ | ✓  
.webm | ✓ | ✓ | ✓  
.wmv | ✓ |  |   
Encoding for video file tracks must use a supported codec. Each platform supports specific codecs that can change with each version of the platform.
Video files that use unsupported codecs trigger an error message in the Editor and you must convert them to a compatible codec before you can use them.
[H.264](https://en.wikipedia.org/wiki/H.264/MPEG-4_AVC) is the optimal supported video codec for most platforms. It offers the best cross-platform compatibility, but the Linux Editor doesn’t support this codec.
For Linux, the optimal encoding is a .webm container with the following codecs:
  * For video tracks, [VP8](https://en.wikipedia.org/wiki/VP8).
  * For audio, [Vorbis](https://en.wikipedia.org/wiki/Vorbis).


For information about codec support, see the official platform documentation for your Editor. See the links below for codec compatibility for Windows and macOS:
  * [Windows codec compatibility](https://docs.microsoft.com/en-us/windows/desktop/medfound/supported-media-formats-in-media-foundation)
  * [macOS codec compatibility](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/OSX_Technology_Overview/MediaLayer/MediaLayer.html)


### Video Clip Importer
The [Video Clip Importer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoClip.html#VideoClipImporterProperties) can transcode video files that you import into Unity. This is useful when your videos use a codec that the Editor platform supports, but the files aren’t compatible with your target platform.
### Using unsupported video files in the Editor
To use video files that are compatible with your target platforms, but not your Editor platform, set them up as [streaming assets](https://docs.unity3d.com/6000.0/Documentation/Manual/StreamingAssets.html). For example, you might want to use the VP9 codec for an Android build, even though the Editor only supports VP8.
To set video files up as streaming assets, place them in the `StreamingAssets` folder of your project. Use the URL property to point the [Video Player](https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoPlayer.html) component to streaming assets.
You can also use [Application.streamingAssetsPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-streamingAssetsPath.html) to access platform-specific paths to streaming assets via **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts). You can’t preview these paths in the Editor.
If you want to have placeholder versions that are compatible with your Editor but use a different version for your target platform, you can include both versions in your project, use Editor-compatible versions as placeholders, and decide which version to use at run time.
The example below demonstrates how to use different video URLs for different platforms. For more information, see the documentation on [Platform-dependent compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/platform-dependent-compilation.html).
```
void SetupMovieFile(VideoPlayer vp)
{
#if UNITY_EDITOR || UNITY_LINUX
vp.url = pathToMyVp8File;
#elif UNITY_ANDROID
vp.url = pathToMyVp9File;
#elif UNITY_STANDALONE_WIN
vp.url = pathToMyWmvFile;
#else
vp.url = pathToMyMp4File;
#endif
}

```

## Compatibility with target platforms
The [Video Player](https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoPlayer.html) component uses the native audio and video decoding libraries of your Editor platform to play video files in the Editor. You must confirm that the files also meet the requirements for the target platform.
### Encoding recommendations
  * The best natively supported video codec for hardware acceleration is [H.264](https://en.wikipedia.org/wiki/H.264/MPEG-4_AVC)
  * When cross-platform support is a high priority, [VP8](https://en.wikipedia.org/wiki/VP8) is a good choice. It’s widely supported and has a comprehensive **feature set** A feature set is a collection of related packages that you can use to achieve specific results in the Unity Editor. You can manage feature sets directly in Unity’s Package Manager. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/FeatureSets.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Featureset), but it consumes more resources than hardware-accelerated codecs such as H.264.
  * [H.265](https://en.wikipedia.org/wiki/High_Efficiency_Video_Coding) is available on devices that support it. See [H.265 Compatibility](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoSources-FileCompatibility.html#H265Compatibility) below, for more information.
  * Android supports VP8 using native libraries, so VP8 might also be hardware-assisted on some Android devices.
  * The Unity Editor supports the .ogv format, but it isn’t widely supported on other platforms. Transcode .ogv files into .mp4 ([H.264](https://en.wikipedia.org/wiki/H.264/MPEG-4_AVC)) or .webm ([VP8](https://en.wikipedia.org/wiki/VP8)) depending on the target platform.


#### Key encoding values
The table below lists key values to look for in your encoding parameters:
Parameter | Description  
---|---  
Video Codec |  [H.264](https://en.wikipedia.org/wiki/H.264/MPEG-4_AVC), [H.265](https://en.wikipedia.org/wiki/High_Efficiency_Video_Coding) or [VP8](https://en.wikipedia.org/wiki/VP8).  
Resolution | The resolution of your display. For example: 1280 × 720.  
Profile | The profile is a set of capabilities and constraints, often specified by the vendor, such as Baseline or Main. Applies to H.264/H.265.See [H.264](https://en.wikipedia.org/wiki/H.264/MPEG-4_AVC#Profiles) or [H.265](https://en.wikipedia.org/wiki/High_Efficiency_Video_Coding#Profiles).  
Profile Level | Applies for H.264/H.265. Within a given profile, the level specifies performance requirements, for example, Baseline 3.1.  
Audio Codec |  [AAC](https://en.wikipedia.org/wiki/Advanced_Audio_Coding) (for mp4 videos using H.264/H.265) or [Vorbis](https://en.wikipedia.org/wiki/Vorbis) (for webm videos using VP8).  
Audio Channels | Dependent on the platform. Refer to the developer guide for your platform. For example, the article on [Supported media formats](https://developer.android.com/guide/topics/media/media-formats) for Android.  
### Transcoding VideoClips
The [Video Clip Importer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoClip.html#VideoClipImporterProperties) provides the option to transcode VideoClip assets into one of the following video codecs:
  * [H.264](https://en.wikipedia.org/wiki/H.264/MPEG-4_AVC)
  * [H.265](https://en.wikipedia.org/wiki/High_Efficiency_Video_Coding)
  * [VP8](https://en.wikipedia.org/wiki/VP8)


Transcoded VideoClips use the appropriate audio codec automatically:
  * [AAC](https://en.wikipedia.org/wiki/Advanced_Audio_Coding) videos encoded with H.264 or H.265
  * [Vorbis](https://en.wikipedia.org/wiki/Vorbis) for videos encoded with VP8


**Note** : The [Video Clip Importer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoClip.html#VideoClipImporterProperties) provides only basic transcoding options. Depending on how your source files are encoded, you might not get optimal performance from clips transcoded with the importer options. In that case, you might get better results with an external transcoding program.
### Encoding VideoClips with an external program
If you use videos that the target system definitely supports, you can leave the [Video Clip Importer’s](https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoClip.html#VideoClipImporterProperties) transcoding options disabled. If disabled, Unity doesn’t modify the files. You can manage encoding with an external program, which allows for finer control.
### Compatibility notes
This section provides useful information about video compatibility, and links to external resources.
#### Vendor recommendations for media support
Follow vendor recommendations for codec support. On older mobile platforms, codec choices are limited . You might need to inspect and convert or re-encode videos that you intend to include in a game running on multiple devices.
  * **Android:** [Supported Media Formats](https://developer.android.com/guide/topics/media/media-formats.html#recommendations)
  * **Windows:** [Supported Media Formats](https://docs.microsoft.com/en-us/windows/desktop/medfound/supported-media-formats-in-media-foundation), [H.265](https://docs.microsoft.com/en-us/windows/desktop/medfound/h-265---hevc-video-decoder#format-constraints)
  * **iPhone:** [Compare iPhone Models](http://www.apple.com/iphone/compare/)
  * **UWP:** [Supported Codecs](https://docs.microsoft.com/en-us/windows/uwp/audio-video-camera/supported-codecs)


#### H.265 compatibility
The table below provides platform-specific requirements and information for the H.265 codec.
Platform | Requirements | Encoding/Decoding | Notes  
---|---|---|---  
**macOS** | SDK 10.13+ |  **Hardware encoding:** 6th Generation Intel Core processor   
  
**Software encoding:** All Macs   
  
**Hardware decoding:** 6th Generation Intel Core processor   
  
**Software decoding:** All Macs |   
**Windows** | Windows 10 + HEVC extensions |  [Encoder](https://docs.microsoft.com/en-us/windows/desktop/medfound/h-265---hevc-video-encoder)  
  
[Decoder](https://docs.microsoft.com/en-us/windows/desktop/medfound/h-265---hevc-video-decoder) |  [HEVC extension (Hardware only)](https://www.microsoft.com/en-ca/p/hevc-video-extensions-from-device-manufacturer/9n4wgh0z6vhq)  
  
[HEVC extension (Hardware + software support)](https://www.microsoft.com/en-ca/p/hevc-video-extensions/9nmzlz57r3t7/0010)  
**iOS** | SDK 11.0+ |  **Hardware decoding:** A9 Chip   
  
**Software decoding:** All iOS Devices |   
**tvOS** | SDK 11.0+ |  |   
**UWP** | [Windows 10+](https://docs.microsoft.com/en-us/windows/uwp/audio-video-camera/supported-codecs) |  | If a device lists support for H.265, that might not apply to all devices within the device family.  
**Android** | [5.0+](https://developer.android.com/guide/topics/media/media-formats) |  |   
* * *
  * 2019–05–07 Page amended 
  * New feature in Unity 5.6


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoSources-VideoFiles.html)
Understanding video files
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoClip.html)
Video Clip Importer reference
