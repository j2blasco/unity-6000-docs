* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/VideoTransparency.html

  * [Video and cutscenes](https://docs.unity3d.com/6000.0/Documentation/Manual/Video.html)
  * [Video sources](https://docs.unity3d.com/6000.0/Documentation/Manual/video-sources.html)
  * Video transparency support


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoClip.html)
Video Clip Importer reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer.html)
Video Player
# Video transparency support
Unity’s [Video Clips](https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoClip.html) and [Video Player component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoPlayer.html) support alpha, which is the standard term used to refer to [transparency](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterAlbedoColor.html). 
In graphics terminology, “alpha” is another way of saying “transparency”. Alpha is a continuous value, not something that can be switched on or off.
The lowest alpha value means an image is fully transparent (not visible at all), while the highest alpha value means it is fully opaque (the image is solid and cannot be seen through). Intermediate values make the image partially transparent, allowing you to see both the image and the background behind it simultaneously.
The Video Player component supports a global alpha value when playing its content in a **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera)’s near or far planes. However, videos can have per-pixel alpha values, meaning that transparency can vary across the video image. This per-pixel transparency control is done in applications that produce images and videos (such as [NUKE](https://www.thefoundry.co.uk/products/non-commercial/nuke-non-commercial/) or [After Effects](http://www.adobe.com/products/aftereffects.html)), and not in the Unity Editor.
Some platforms have limitations for rendering videos with transparency. For more information, see: * [Android requirements and compatibility](https://docs.unity3d.com/6000.0/Documentation/Manual/android-requirements-and-compatibility.html)
Unity supports two types of sources that have per-pixel alpha:
## Apple ProRes 4444
The [Apple ProRes 4444 codec](https://support.apple.com/en-gb/HT202410) is a high-quality version of Apple ProRes for 4:4:4:4 image sources, including alpha channels. It offers the same level of visual fidelity as the source video.
Apple ProRes 4444 is only supported on OSX because this is the only platform where it is available natively. It normally appears in .mov files.
When importing a video that uses this codec, enable both the **Transcode** and **Keep Alpha** options by ticking the relevant checkboxes in the Video Clip Importer. Your operating system’s video playback software may have the functionality to identify which codecs your video uses.
![A Video Clip Asset viewed in the Inspector, showing the Keep Alpha option - highlighted in red - enabled](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/Video-10.png) A Video Clip Asset viewed in the Inspector, showing the **__Keep Alpha__** option - highlighted in red - enabled
During transcoding, Unity inserts the alpha into the color stream so it can be used both with H.264 or VP8.
Omitting the transcode operation leaves the ProRes representation in the Asset, meaning the target platform has to support this codec (see documentation on video file compatibility for more information). 
This codec also usually produces large files, which increases storage and bandwidth requirements.
## Webm with VP8
The .webm file format has a specification refinement that allows it to carry alpha information natively when combined with the VP8 video codec. This means any Editor platform can read videos with transparency with this format.
Because most of Unity’s supported platforms use a software implementation for decoding these files, they don’t need to be transcoded for these platforms.
One notable exception is Android. This platform’s native VP8 support does not include transparency support, which means transcoding must be enabled so Unity uses its internal alpha representation. 
* * *
  * 2017–06–15 Page published 
  * New feature in Unity 5.6


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoClip.html)
Video Clip Importer reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer.html)
Video Player
