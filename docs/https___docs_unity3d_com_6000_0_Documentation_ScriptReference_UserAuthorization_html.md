* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UserAuthorization.html

# UserAuthorization
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
Use this enum to request permission from the user’s device for access to system features.
To request permission, pass this as a parameter to [Application.RequestUserAuthorization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.RequestUserAuthorization.html).   
  
**Note** : The Microphone API is not available for the Web platform.
```
// This script outputs the feed from a video input source (if one exists) to the texture of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) you attach this script to. 
// For this to work, attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) that has a Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) component.   
  
using UnityEngine;
using System.Collections;  
  
public class WebcamExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private WebCamTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.html) webCamTexture;  
  
    IEnumerator Start()
    {
        // Request[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.Request.html) permission from the device for access to video input sources. 
        yield return Application.RequestUserAuthorization[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.RequestUserAuthorization.html)(UserAuthorization.WebCam[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UserAuthorization.WebCam.html));
        
        // If the user approves access to video, play video feed to GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s texture. 
        if (Application.HasUserAuthorization[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.HasUserAuthorization.html)(UserAuthorization.WebCam[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UserAuthorization.WebCam.html)))
        {
            // Get the first available video input source.
            string webCamName = WebCamTexture.devices[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture-devices.html)[0].name;
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Selected WebCam[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.WebCam.html): {webCamName}");  
  
            // Use this webcam to create a WebCamTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.html).
            webCamTexture = new WebCamTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.html)(webCamName);  
  
            // Assign the texture to the current GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html). 
            Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) renderer = GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();
            if (renderer != null)
            {
                renderer.material.mainTexture = webCamTexture;
            }  
  
            // Stream the footage from the webcam. 
            webCamTexture.Play();
        }
        else
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Webcam not found.");
        }
    }  
  
    void OnApplicationQuit()
    {
        // Stop the webcam feed when the application closes. 
        if (webCamTexture != null && webCamTexture.isPlaying)
        {
            webCamTexture.Stop();
        }
    }
}

```

### Properties
Property | Description  
---|---  
[WebCam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UserAuthorization.WebCam.html) | Request permission to use any video input sources attached to the device.  
[Microphone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UserAuthorization.Microphone.html) | Request permission to use any audio input sources attached to the device.  
* * *
