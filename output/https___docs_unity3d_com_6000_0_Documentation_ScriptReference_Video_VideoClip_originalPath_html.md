* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip-originalPath.html

#  [VideoClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html).originalPath
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
originalPath; 
### Description
Gets the original video clip file path as it was imported into Unity. (Read Only).
Use this property to find the original location of the file when you imported it into Unity. If you move the video clip file, this property’s value remains as the original location. The value only updates if you reimport the file.   
  
**Note** : When you import your video file, if you enable **Transcode** in the VideoClip Import Settings, `originalPath` returns the new video format instead of the original format. For example, if you do the following: 
  1. Import an MP4 video file into Unity.
  2. Click on the file to show the Import Settings window.
  3. Enable **Transcode**.
  4. Set **Codec** to **VP8**.


Unity imports the video file in the WebM format, and `originalPath` returns `.webm` instead of `.mp4`. To get your original format instead, use [AssetDatabase.GetAssetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html).  
  
Additional resources: [VideoClip Importer](https://docs.unity3d.com/Manual/class-VideoClip.html).
```
// The script outputs the clip’s original path to the console. 
// Assign this script and a VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) component to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in your Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html).
// In the VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) component, assign a video clip.   
  
using UnityEngine;
using UnityEngine.Video;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class OriginalPathExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) videoPlayer = GetComponent<VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html)>();
        VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html) videoClip = videoPlayer.clip;
        // Get the original video file path as it was imported into Unity.
        string originalPath = videoClip.originalPath;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Original Path: " + originalPath);  
  
        // Verify if the original file exists. 
        if (System.IO.File.Exists(originalPath))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Original video file found at: " + originalPath);
        }
        else
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Original video file not found at: " + originalPath +
                ". Checking AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html) instead.");
            // Check Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) database instead for the video clip. 
            string assetPath = AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(videoClip);
            if (System.IO.File.Exists(assetPath))
            {
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Original video file found at " + assetPath);
            }
            else Debug.LogWarning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogWarning.html)("Original video file not found!");
        }
    }
}
```

* * *
