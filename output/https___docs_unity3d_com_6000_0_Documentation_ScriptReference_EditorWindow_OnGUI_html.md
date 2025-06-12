* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnGUI.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).OnGUI()
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
Implement your own editor GUI here.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/SimpleRecorder.png)   
_Use OnGUI to draw all the controls of your window._
```
// A simple script that saves frames from the Game view when in Play mode.
//
// You can put the frames together later to create a video.
// The frames are saved in the project, at the same level of the project hierarchy as the Assets folder.  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class SimpleRecorder : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    string fileName = "FileName";  
  
    string status = "Idle";
    string recordButton = "Record";
    bool recording = false;
    float lastFrameTime = 0.0f;
    int capturedFrame = 0;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Simple Recorder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder.html)")]
    static void Init()
    {
        SimpleRecorder window =
            (SimpleRecorder)EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)(typeof(SimpleRecorder));
    }  
  
    void OnGUI()
    {
        fileName = EditorGUILayout.TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.TextField.html)("File[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.html) Name:", fileName);  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)(recordButton))
        {
            if (recording)  //recording
            {
                status = "Idle...";
                recordButton = "Record";
                recording = false;
            }
            else     // idle
            {
                capturedFrame = 0;
                recordButton = "Stop";
                recording = true;
            }
        }
        EditorGUILayout.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html)("Status[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.Status.html): ", status);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (recording)
        {
            if (EditorApplication.isPlaying[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-isPlaying.html) && !EditorApplication.isPaused[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-isPaused.html))
            {
                RecordImages();
                Repaint();
            }
            else
                status = "Waiting for Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) to Play";
        }
    }  
  
    void RecordImages()
    {
        if (lastFrameTime < Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) + (1 / 24f)) // 24fps
        {
            status = "Captured frame " + capturedFrame;
            ScreenCapture.CaptureScreenshot[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScreenCapture.CaptureScreenshot.html)(fileName + " " + capturedFrame + ".png");
            capturedFrame++;
            lastFrameTime = Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html);
        }
    }
}

```

* * *
