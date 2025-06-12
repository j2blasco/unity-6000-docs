* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoCodec.html

# VideoCodec
enumeration
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
### Description
Choose the video codec to use to import video clips.
Use this enum to set [VideoImporterTargetSettings.codec](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoImporterTargetSettings-codec.html).   
  
A video codec compresses (encodes) or decompresses (decodes) video data to reduce the file size but avoid reduction of quality as much as possible. For Unity to consider the video codec when it imports a video, make sure to enable the **Transcoding** property in the video clip’s **Inspector** window. For more information about video encoding, refer to [Video encoding compatibility reference](https://docs.unity3d.com/6000.0/Documentation/Manual/video-encoding-compatibility.html).
```
// This script creates an Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) menu option that reimports a video with your preferred video codec (Auto is default). 
// Put this script in your **Assets**>**Editor** folder. If you don't have an Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) folder, create your own.  
// In the script, change the videoPath to a video file in your project. Save the script. 
// In the menu, go to **Tools** and select **Change video codec settings**.
// The video reimports with the new video codec.   
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class VideoImportSettingsEditor : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Tools[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tools.html)/Change video codec settings")]
    static void SetVideoImporterSettings()
    {
        // Path to the video file in your project. Change the path to suit your own project. 
        string videoPath = "Assets/YourVideo.mp4";
        // Change this to your preferred video codec. 
        VideoCodec[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoCodec.html) preferredCodec = VideoCodec.Auto[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoCodec.Auto.html);   
  
        // Get the VideoClipImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter.html) for the video file
        VideoClipImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter.html) importer = AssetImporter.GetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetAtPath.html)(videoPath) as VideoClipImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter.html);  
  
        if (importer != null)
        {
            VideoImporterTargetSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoImporterTargetSettings.html) defaultSettings = importer.defaultTargetSettings;
            // Set the video codec to your chosen video codec.
            defaultSettings.codec = preferredCodec;  
  
            // Apply the updated settings for standalone. 
            importer.SetTargetSettings("Standalone[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Standalone.html)", defaultSettings);  
  
            // Re-import the video file. 
            importer.SaveAndReimport();  
  
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Updated video importer settings for: {videoPath}");
        }
        else
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)($"Failed to find VideoClipImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter.html) for the path: {videoPath}");
        }
    }
}

```

### Properties
Property | Description  
---|---  
[Auto](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoCodec.Auto.html) | Choose the codec that supports hardware decoding on the target platform.  
[H264](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoCodec.H264.html) | Encode video with the H.264 codec.  
[H265](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoCodec.H265.html) | Encode video with the H.265 codec.  
[VP8](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoCodec.VP8.html) | Encode video using the vp8 codec.  
* * *
