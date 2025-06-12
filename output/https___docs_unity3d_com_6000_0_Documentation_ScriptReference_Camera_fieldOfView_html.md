* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-fieldOfView.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).fieldOfView
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
fieldOfView; 
### Description
The vertical field of view of the Camera, in degrees.
This is the vertical field of view; horizontal field of view depends on the viewport's aspect ratio. For for more information, see [VerticalToHorizontalFieldOfView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.VerticalToHorizontalFieldOfView.html).  
  
If [Camera.orthographic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-orthographic.html) is `true`, the Camera ignores `fieldOfView`.  
  
Some VR SDKs have fixed field of view values that are used for VR cameras. When VR is enabled with those SDKs, this property will always return the value from the SDK. You will see a warning logged if you attempt to set the property and the value will be ignored.  
  
If you make changes to [Camera.projectionMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-projectionMatrix.html), the Camera ignores `fieldOfView`. This lasts until you call [Camera.ResetProjectionMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ResetProjectionMatrix.html).  
  
In the Unity Editor, this corresponds to the **Clipping Planes: Near** property in the Camera component Inspector.  
  
Additional resources: [Camera Inspector reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html).
```
//Attach this script to an empty GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).
//This script creates a Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html) that allows you to manipulate the Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)'s field of view. Place GameObjects in the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) to show the full effect.  
  
using UnityEngine;  
  
public class CameraFieldOfViewExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //This is the field of view that the Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) has
    float m_FieldOfView;  
  
    void Start()
    {
        //Start the Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) field of view at 60
        m_FieldOfView = 60.0f;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) the camera's field of view to be the variable returning from the Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html)
        Camera.main.fieldOfView = m_FieldOfView;
    }  
  
    void OnGUI()
    {
        //Set up the maximum and minimum values the Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html) can return (you can change these)
        float max, min;
        max = 150.0f;
        min = 20.0f;
        //This Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html) changes the field of view of the Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) between the minimum and maximum values
        m_FieldOfView = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(20, 20, 100, 40), m_FieldOfView, min, max);
    }
}

```

* * *
