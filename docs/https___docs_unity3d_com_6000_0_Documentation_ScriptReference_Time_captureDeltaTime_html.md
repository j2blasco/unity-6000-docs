* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-captureDeltaTime.html

#  [Time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html).captureDeltaTime
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
captureDeltaTime; 
### Description
Slows your application’s playback time to allow Unity to save screenshots in between frames.
If this property has a non-zero value then [Time.time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) increases at an interval of captureDeltaTime (scaled by [Time.timeScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-timeScale.html)) regardless of real time and the duration of a frame. This is useful if you want to capture a movie where you need a constant frame rate and want to leave enough time between frames to save screen images.  
  
**Note:** captureDeltaTime does not have any affect on [Time.unscaledTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-unscaledTime.html). Therefore, if parts of your application rely on it for animations or other effects, captureDeltaTime might not be enough to capture a movie.
```
using UnityEngine;
using System.Collections;  
  
// Capture frames as a screenshot sequence. Images are
// stored as PNG files in a folder - these can be combined into
// a movie using image utility software (eg, QuickTime Pro).  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // The folder to contain our screenshots.
    // If the folder exists we will append numbers to create an empty folder.
    public string folder = "ScreenshotFolder";
    public int frameRate = 25;
    void Start()
    {
        // Set the playback framerate (real time will not relate to game time after this).
        Time.captureDeltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-captureDeltaTime.html) = 1.0f / frameRate;  
  
        // Create the folder
        System.IO.Directory.CreateDirectory(folder);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Append filename to folder name (format is '0005 shot.png"')
        string name = string.Format("{0}/{1:D04} shot.png", folder, Time.frameCount[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-frameCount.html));  
  
        // Capture the screenshot to the specified file.
        ScreenCapture.CaptureScreenshot[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScreenCapture.CaptureScreenshot.html)(name);
    }
}

```

* * *
