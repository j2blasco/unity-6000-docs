* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html

#  [Time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html).deltaTime
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
deltaTime; 
### Description
The interval in seconds from the last frame to the current one (Read Only).
When this is called from inside [MonoBehaviour.FixedUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.FixedUpdate.html), it returns [Time.fixedDeltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-fixedDeltaTime.html). The maximum value for `deltaTime` is defined by [Time.maximumDeltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-maximumDeltaTime.html).  
  
`deltaTime` inside [MonoBehaviour.OnGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnGUI.html) is not reliable, because Unity might call it multiple times per frame.  
  
The following example rotates a GameObject around its z axis at a constant speed.  
  
See [Time and Frame Rate Management](https://docs.unity3d.com/6000.0/Documentation/Manual/managing-time-and-frame-rate.html) in the User Manual for more information about how this property relates to the other Time properties.
```
using UnityEngine;
// Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) around the z axis at a constant speed
public class ConstantRotation : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float degreesPerSecond = 2.0f;
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        transform.Rotate(0, 0, degreesPerSecond * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html));
    }
}

```

The following example implements a timer. The timer adds deltaTime each frame. The example displays the timer value and resets it when it reaches 2 seconds. [Time.timeScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-timeScale.html) controls the speed at which time passes and how fast the timer resets.
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;  
  
// Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html) example.
//
// Wait two seconds and display waited time.
// This is typically just beyond 2 seconds.
// Allow the speed of the time to be increased or decreased.
// It can range between 0.5 and 2.0. These changes only
// happen when the timer restarts.  
  
public class ScriptExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private float waitTime = 2.0f;
    private float timer = 0.0f;
    private float visualTime = 0.0f;
    private int width, height;
    private float value = 10.0f;
    private float scrollBar = 1.0f;  
  
    void Awake()
    {
        width = Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html);
        height = Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html);
        Time.timeScale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-timeScale.html) = scrollBar;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        timer += Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);  
  
        // Check if we have reached beyond 2 seconds.
        // Subtracting two is more accurate over time than resetting to zero.
        if (timer > waitTime)
        {
            visualTime = timer;  
  
            // Remove the recorded 2 seconds.
            timer = timer - waitTime;
            Time.timeScale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-timeScale.html) = scrollBar;
        }
    }  
  
    void OnGUI()
    {
        GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) sliderDetails = new GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html)(GUI.skin.GetStyle("horizontalSlider"));
        GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) sliderThumbDetails = new GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html)(GUI.skin.GetStyle("horizontalSliderThumb"));
        GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) labelDetails = new GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html)(GUI.skin.GetStyle("label"));  
  
        // Set the size of the fonts and the width/height of the slider.
        labelDetails.fontSize = 6 * (width / 200);
        sliderDetails.fixedHeight = height / 32;
        sliderDetails.fontSize = 12 * (width / 200);
        sliderThumbDetails.fixedHeight = height / 32;
        sliderThumbDetails.fixedWidth = width / 32;  
  
        // Show the slider. Make the scale to be ten times bigger than the needed size.
        value = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(width / 8, height / 4, width - (4 * width / 8), height - (2 * height / 4)),
            value, 5.0f, 20.0f, sliderDetails, sliderThumbDetails);  
  
        // Show the value from the slider. Make sure that 0.5, 0.6... 1.9, 2.0 are shown.
        float v = ((float)Mathf.RoundToInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.RoundToInt.html)(value)) / 10.0f;
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(width / 8, height / 3.25f, width - (2 * width / 8), height - (2 * height / 4)),
            "timeScale: " + v.ToString("f1"), labelDetails);
        scrollBar = v;  
  
        // Display[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html) the recorded time in a certain size.
        labelDetails.fontSize = 14 * (width / 200);
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(width / 8, height / 2, width - (2 * width / 8), height - (2 * height / 4)),
            "Timer value is: " + visualTime.ToString("f4") + " seconds.", labelDetails);
    }
}

```

* * *
