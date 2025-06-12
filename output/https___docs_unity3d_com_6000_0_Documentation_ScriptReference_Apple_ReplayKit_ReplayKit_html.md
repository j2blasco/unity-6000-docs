* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Apple.ReplayKit.ReplayKit.html

**Method group is Obsolete**   

# ReplayKit
class in UnityEngine.Apple.ReplayKit
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
**Obsolete** ReplayKit will be removed in future version of Unity.
### Description
ReplayKit is only available on certain iPhone, iPad and iPod Touch devices running iOS 9.0 or later.
ReplayKit allows you to record the audio and video of your game, along with user commentary through the microphone and user video through the camera. Start a recording with the StartRecording() function, and stop it with StopRecording(). You can preview the recording with the Preview() function, which launches a separate video viewer. In addition to local recordings, you can broadcast your recordings via StartBroadcasting(). There are also functions to pause, resume, and stop broadcasting.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEngine;
#if PLATFORM_IOS
using UnityEngine.iOS;
using UnityEngine.Apple.ReplayKit;  
  
public class Replay : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public bool enableMicrophone = false;
    public bool enableCamera = false;  
  
    string lastError = "";
    void OnGUI()
    {
        if (!ReplayKit.APIAvailable)
        {
            return;
        }
        var recording = ReplayKit.isRecording;
        string caption = recording ? "Stop Recording" : "Start Recording";
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 500, 200), caption))
        {
            try
            {
                recording = !recording;
                if (recording)
                {
                    ReplayKit.StartRecording(enableMicrophone, enableCamera);
                }
                else
                {
                    ReplayKit.StopRecording();
                }
            }
            catch (Exception e)
            {
                lastError = e.ToString();
            }
        }  
  
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 220, 500, 50), "Last error: " + ReplayKit.lastError);
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 280, 500, 50), "Last exception: " + lastError);  
  
        if (ReplayKit.recordingAvailable)
        {
            if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 350, 500, 200), "Preview"))
            {
                ReplayKit.Preview();
            }
            if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 560, 500, 200), "Discard"))
            {
                ReplayKit.Discard();
            }
        }
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // If the camera is enabled, show the recorded video overlaying the game.
        if (ReplayKit.isRecording && enableCamera)
            ReplayKit.ShowCameraPreviewAt(10, 350, 200, 200);
        else
            ReplayKit.HideCameraPreview();
    }
}
#endif

```

### Static Methods
Method | Description  
---|---  
[StartBroadcasting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Apple.ReplayKit.ReplayKit.StartBroadcasting.html) | Initiates and starts a new broadcast When StartBroadcast is called, user is presented with a broadcast provider selection screen, and then a broadcast setup screen. Once it is finished, a broadcast will be started, and the callback will be invoked. It will also be invoked in case of any error.   
* * *
