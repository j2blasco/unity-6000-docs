* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.RequestUserAuthorization.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).RequestUserAuthorization
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
## Declaration
public static [AsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation.html) RequestUserAuthorization([UserAuthorization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UserAuthorization.html) mode); 
### Description
Request authorization to use the webcam or microphone on iOS, and the webcam only on WebGL.
`Application.RequestUserAuthorization` is called to request permission for microphone and camera. The application shows a dialog box to the user and waits for the operation to complete before being able to use these features.  
  
**Note:** Use [Application.HasUserAuthorization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.HasUserAuthorization.html) to query the result of the operation.
```
using UnityEngine;
using UnityEngine.iOS;
using System.Collections;  
  
// Show WebCams and Microphones on an iPhone/iPad.
// Make sure NSCameraUsageDescription and NSMicrophoneUsageDescription
// are in the Info.plist.  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    IEnumerator Start()
    {
        FindWebCams();  
  
        yield return Application.RequestUserAuthorization[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.RequestUserAuthorization.html)(UserAuthorization.WebCam[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UserAuthorization.WebCam.html));
        if (Application.HasUserAuthorization[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.HasUserAuthorization.html)(UserAuthorization.WebCam[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UserAuthorization.WebCam.html)))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("webcam found");
        }
        else
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("webcam not found");
        }  
  
        FindMicrophones();  
  
        yield return Application.RequestUserAuthorization[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.RequestUserAuthorization.html)(UserAuthorization.Microphone[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UserAuthorization.Microphone.html));
        if (Application.HasUserAuthorization[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.HasUserAuthorization.html)(UserAuthorization.Microphone[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UserAuthorization.Microphone.html)))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Microphone[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone.html) found");
        }
        else
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Microphone[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone.html) not found");
        }
    }  
  
    void FindWebCams()
    {
        foreach (var device in WebCamTexture.devices[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture-devices.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Name: " + device.name);
        }
    }  
  
    void FindMicrophones()
    {
        foreach (var device in Microphone.devices[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone-devices.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Name: " + device);
        }
    }
}

```

* * *
