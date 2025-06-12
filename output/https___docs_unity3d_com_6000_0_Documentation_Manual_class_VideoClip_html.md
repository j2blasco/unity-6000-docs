* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoClip.html

  * [Video and cutscenes](https://docs.unity3d.com/6000.0/Documentation/Manual/Video.html)
  * [Video sources](https://docs.unity3d.com/6000.0/Documentation/Manual/video-sources.html)
  * Video Clip Importer reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoSources-FileCompatibility.html)
Video file compatibility
[](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoTransparency.html)
Video transparency support
# Video Clip Importer reference
Configure the settings of the Video Clip Importer to transcode video files into different formats, ensuring compatibility with your target platforms.
**Note:** The transcoding process can result in longer build times and lower video quality.
## Transcode your video files
To access the Video Clip Importer settings for transcoding:
  1. Select your [video clip asset](https://docs.unity3d.com/6000.0/Documentation/Manual/video-clips-use.html).
  2. Enable the **Transcode** property.
  3. Configure the [Video Clip Importer settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoClip.html#VideoClipImporterProperties).
  4. Select **Apply**.


## Video Clip Importer settings
The following settings are available after you enable the **Transcode** property.
**Property** |  | **Description**  
---|---|---  
**sRGB (Color Texture)** |  | Choose whether the VideoPlayer converts sRGB to Linear color space when it loads the video data into textures. Unity enables this setting by default because most video clips store color data in sRGB color space. For non-color video clips, disable this setting to avoid unnecessary conversions.  
**Transcode** |  | Transcode the source content into a format that’s compatible with the target platform.   
  
**Note:** Verify that the source format is compatible with each target platform. For more information, refer to [Video file compatibility](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoSources-FileCompatibility.html).  
**Dimensions** |  | Control how the source content is resized in **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel). **Aspect ratio** The relationship of an image’s proportional dimensions, such as its width and height.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AspectRatio) is controllable for all options.  
| **Original Size** | Keep the original size of the source.  
| **Three Quarter Res** | Resize the source to three quarters of its original width and height.  
| **Half Res** | Resize the source to half of its original width and height.  
| **Quarter Res** | Resize the source to a quarter of its original width and height.  
| **Square 1024** | Resize the source to a 1024 x 1024 square image.  
| **Square 512** | Resize the source to a 512 x 512 square image.  
| **Square 256** | Resize the source to a 256 x 256 square image.  
| **Custom Size** | Resize the source to a custom width and height.  
**Codec** |  | Choose the codec to encode the video track. For information about codec support, refer to [Video file compatibility](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoSources-FileCompatibility.html).  
| **Auto** | Choose the most suitable video codec for the target platform automatically.  
| **H264** | Choose the MPEG–4 Advanced Video Coding (AVC) video codec, supported by hardware on most platforms.  
| **H265** | Choose the MPEG-H Part 2, or High Efficiency Video Coding (HEVC), video codec, supported by hardware on some platforms.  
| **VP8** | Choose the VP8 video codec, supported by software on most platforms, and by hardware on Android and Web.  
**Bitrate Mode** |  | Choose a bitrate relative to the chosen codec’s baseline profile.   
  
**Note:** Higher bitrates provide a higher quality video, but impose a higher load on network connections or storage.  
| **Low** | Choose a low bitrate.  
| **Medium** | Choose a medium bitrate.  
| **High** | Choose a high bitrate.  
**Spatial Quality** |  | Choose whether the spatial quality of video images are reduced in size during transcoding.   
  
**Note:** Resizing images uses less storage but also results in blurriness during playback.  
| **Low Spatial Quality** | The image is significantly reduced in size during transcoding (typically to a quarter of its original dimensions), and then expanded back to its original size upon playback. This is the highest amount of resizing, meaning it saves the most storage space but results in the largest amount of blurriness upon playback.  
| **Medium Spatial Quality** | The image is moderately reduced in size during transcoding (typically to half of its original dimensions), and then expanded back to its original size upon playback. Although there is some resizing, images will be less blurry than those that use the Low Spatial Quality option, and there is some reduction in required storage space.  
| **High Spatial Quality** | No resizing takes place if this option is selected. This means the image is not reduced in size during transcoding, and therefore the video’s original level of visual clarity is maintained.  
**Keep Alpha** |  | Preserve the [alpha channel](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoTransparency.html) and encode it during transcoding so it can be used even if the target platform does not natively support videos with alpha.   
  
**Note:** This property is only visible for sources that have an alpha channel.  
**Deinterlace** |  | Control how interlaced sources are deinterlaced during transcoding.   
  
**Note:** Interlaced videos have two time samples in each frame: one in odd-numbered lines, and one in even-numbered lines.  
| **Off** | The source is not interlaced and there is no processing to perform. This is the default setting.  
| **Even** | Take the even lines of each frame and interpolate them to create missing content. Odd lines are dropped.  
| **Odd** | Take the odd lines of each frame and interpolate them to create missing content. Even lines are dropped.  
**Flip Horizontally** |  | Flip the source content along a horizontal axis when transcoding.  
**Flip Vertically** |  | Flip the source content along a vertical axis when transcoding.  
**Import Audio** |  | Import the audio tracks when transcoding.   
  
**Note:** This property is available only for sources that have audio tracks.  
* * *
VideoClip
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoSources-FileCompatibility.html)
Video file compatibility
[](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoTransparency.html)
Video transparency support
