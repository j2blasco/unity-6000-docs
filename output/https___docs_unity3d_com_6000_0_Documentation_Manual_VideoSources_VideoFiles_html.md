* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/VideoSources-VideoFiles.html

  * [Video and cutscenes](https://docs.unity3d.com/6000.0/Documentation/Manual/Video.html)
  * [Video sources](https://docs.unity3d.com/6000.0/Documentation/Manual/video-sources.html)
  * Understanding video files


[](https://docs.unity3d.com/6000.0/Documentation/Manual/video-sources-reference.html)
Use video sources
[](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoSources-FileCompatibility.html)
Video file compatibility
# Understanding video files
Video files are more accurately described as “containers”. This is because they can contain not only the video itself but also additional tracks including audio, subtitles, and further video footage. There can also be more than one of each type of track in a container, for example:
  * Multiple points of view
  * Stereo or 5.1 versions of the audio mix
  * Subtitles in different languages
  * Dialogue in different languages


To save on bandwidth and storage, each track’s content is encoded using a “codec”, which compresses and decompresses data as required.
A common video codec format is H.264, and a common audio codec format is AAC.
File extensions such as .mp4, .mov, .webm or .avi indicate that the data in the video file is arranged using a certain container format.
## Hardware and software decoding
Most modern devices have hardware dedicated to decoding videos. This hardware typically requires less power to do this task than, for example, the CPU, and means that the resources can be used for tasks other than decoding videos.
This hardware acceleration is made possible by native custom APIs, which vary from platform to platform. Unity’s video architecture hides these differences by providing a common UI and Scripting API in order to access these capabilities.
Unity is also capable of software-based video decoding. This uses the VP8 video codec and Vorbis audio codec, and is useful for situations where a platform’s hardware decoding results in unwanted restrictions in terms of resolution, the presence of multiple audio tracks, or support of alpha channel (see documentation on [Transparency](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoTransparency.html) for more information).
* * *
  * 2017–06–15 Page published 
  * New feature in Unity 5.6


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/video-sources-reference.html)
Use video sources
[](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoSources-FileCompatibility.html)
Video file compatibility
