* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.Pause.html

#  [WebCamTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.html).Pause
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
public void Pause(); 
### Description
Pauses the camera.
Call [Application.RequestUserAuthorization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.RequestUserAuthorization.html) before creating a WebCamTexture.
```
// Starts a camera and assigns the texture to the current renderer.
// Pauses the camera when the "Pause" button is clicked and released.
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public WebCamTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.html) webcamTexture;  
  
    void Start()
    {
        webcamTexture = new WebCamTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.html)();
        Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) renderer = GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();
        renderer.material.mainTexture = webcamTexture;
        webcamTexture.Play();
    }  
  
    void OnGUI()
    {
        if (webcamTexture.isPlaying)
            if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Pause"))
                webcamTexture.Pause();  
  
            else if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Play"))
                webcamTexture.Play();
    }
}

```

* * *
