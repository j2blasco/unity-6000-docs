* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-streamingAssetsPath.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).streamingAssetsPath
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
streamingAssetsPath; 
### Description
The path to the `StreamingAssets` folder (Read Only).
Use the `StreamingAssets` folder to store assets. At runtime, `Application.streamingAssetsPath` provides the path to the folder. Add the asset name to `Application.streamingAssetsPath`. The built application can load the asset at this address. You can use the [Debug.Log](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html) class to print the path to the `StreamingAssets` folder to the Unity Console.  
  
You cannot use synchronous filesystem APIs, such as the C# `System.IO.File` class, to access the `StreamingAssets` folder on the WebGL and Android platforms. No file access is available on WebGL. Android uses a compressed `.apk` file. These platforms return a URL. Use the [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) class to access the assets.
```
using UnityEngine;
using System.IO;
using UnityEngine.Video;  
  
// Application[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html)-streamingAssetsPath example.
//
// Play a video and let the user stop/start it.
// The video location is StreamingAssets. The video is
// played on the camera background.  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private UnityEngine.Video.VideoPlayer videoPlayer;
    private string status;  
  
    void Start()
    {
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) cam = GameObject.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.Find.html)("Main Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)");
        videoPlayer = cam.AddComponent<UnityEngine.Video.VideoPlayer>();  
  
        // Obtain the location of the video clip.
        videoPlayer.url = Path.Combine(Application.streamingAssetsPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-streamingAssetsPath.html), "SampleVideo_1280x720_5mb.mp4");  
  
        // Restart from beginning when done.
        videoPlayer.isLooping = true;  
  
        // Do not show the video until the user needs it.
        videoPlayer.Pause();  
  
        status = "Press to play";
    }  
  
    void OnGUI()
    {
        GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) buttonWidth = new GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html)(GUI.skin.GetStyle("button"));
        buttonWidth.fontSize = 18 * (Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html) / 800);  
  
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html) / 16, Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html) / 16, Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html) / 3, Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html) / 8), status, buttonWidth))
        {
            if (videoPlayer.isPlaying)
            {
                videoPlayer.Pause();
                status = "Press to play";
            }
            else
            {
                videoPlayer.Play();
                status = "Press to pause";
            }
        }
    }
}

```

The following code example demonstrates how to access a file in the `StreamingAssets` folder on Android platform.
```
using UnityEngine;
using UnityEngine.Networking;
using System.Threading.Tasks;  
  
public class LoadStreamingAsset : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    async void Start()
    {
        string filePath = System.IO.Path.Combine(Application.streamingAssetsPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-streamingAssetsPath.html), "filetoload.txt");  
  
        UnityWebRequest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) request = UnityWebRequest.Get[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Get.html)(filePath);
        UnityWebRequestAsyncOperation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestAsyncOperation.html) operation = request.SendWebRequest();  
  
        while (!operation.isDone)
        {
            await Task.Yield();
        }  
  
        if (request.result == UnityWebRequest.Result.Success[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Result.Success.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(request.downloadHandler.text);
        }
        else
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("Cannot load file at " + filePath);
        }
    }
}

```

* * *
