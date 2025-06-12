* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-pixelWidth.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).pixelWidth
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html "Go to Camera Component in the Manual")
pixelWidth; 
### Description
How wide is the camera in pixels (not accounting for dynamic resolution scaling) (Read Only).
Use this to return how wide the Camera viewport is in pixels. This is read-only.
```
//Attach this script to an empty GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
//Create a new Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) (**Create**>**Camera**) and position it appropriately. Attach it to the Second Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) field in the Inspector of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
//Press the space key to enable and disable the second Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)  
  

using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //Attach a new Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) in the Inspector window
    public Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) m_SecondCamera;
    //This is set as the main Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) in this script
    Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) m_FirstCamera;  
  
    void Start()
    {
        //Disable the second Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)
        m_SecondCamera.enabled = false;
        //Set where to place the second Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) along with its width and height
        m_SecondCamera.pixelRect = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 400, 200);
        //Set the first Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) as the main Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)
        m_FirstCamera = Camera.main[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-main.html);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Press the space key to toggle the second Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) and output camera pixel width and height
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
        {
            //Check if the second camera is enabled yet
            if (!m_SecondCamera.enabled)
            {
                //Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html) the second Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) and output the second Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)'s details
                ToggleCamera(m_SecondCamera, m_SecondCamera);
            }
            else
            {
                //Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html) the second Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) and output the first Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)'s details
                ToggleCamera(m_SecondCamera, m_FirstCamera);
            }
        }
    }  
  
    //Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html) the Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) and output the Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) specified
    void ToggleCamera(Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) cameraToggle, Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) cameraOutput)
    {
        //Set Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) on and off
        cameraToggle.enabled = !cameraToggle.enabled;  
  
        //Output the Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)'s new Pixel width
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Pixel width :" + cameraOutput.pixelWidth + " Pixel height : " + cameraOutput.pixelHeight);
    }
}

```

* * *
