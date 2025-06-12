* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip-sRGB.html

#  [VideoClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html).sRGB
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
sRGB; 
### Description
Whether the imported clip contains sRGB color data (Read Only).
This setting controls whether sRGB->Linear color space conversion is done when the [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) is loading the video data into textures. This setting is only relevant when [Linear color space](https://docs.unity3d.com/6000.0/Documentation/Manual/LinearLighting.html) is used.  
  
Most movies store color data in sRGB color space. Set [VideoClipImporter.sRGBClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter-sRGBClip.html) to true in most cases.  
  
Non-color movies are commonly stored as linear values, and the GPU should not perform color space conversions. Set to false in the [VideoClipImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter.html) for non-color movies.  
  
This setting corresponds to [VideoClipImporter.sRGBClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter-sRGBClip.html) in the video clip importer.  
  
Additional resources: [PlayerSettings.colorSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-colorSpace.html).
```
using UnityEngine;
using UnityEngine.Video;  
  
public class SRGBExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) videoPlayer;  
  
    void Start()
    {
        videoPlayer = GetComponent<VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html)>();
        // Get the VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html) from the VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html)
        VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html) clip = videoPlayer.clip;  
  
        if (clip != null)
        {
            // Output if the clip contains sRGB color data.  
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Does this clip use sRGB color data? : " + clip.sRGB);
        }
        else
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("No VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html) assigned to the VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html).");
        }
    }
}

```

* * *
