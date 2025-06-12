* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform-anchoredPosition.html

#  [RectTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.html).anchoredPosition
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
[Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) anchoredPosition; 
### Description
The position of the pivot of this RectTransform relative to the anchor reference point.
The Anchored Position is the position of the pivot of the RectTransform taking into consideration the anchor reference point. The anchor reference point is the position of the anchors. If the anchors are not together, Unity estimates the four anchor positions using the pivot placement as a reference.  
  
**Note** : The Inspector changes which properties are exposed based on which anchor preset is in use. For more information see [Rect Transform](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RectTransform.html) and [Basic Layout](https://docs.unity3d.com/6000.0/Documentation/Manual/UIBasicLayout.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    RectTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.html) m_RectTransform;
    float m_XAxis, m_YAxis;  
  
    void Start()
    {
        //Fetch the RectTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.html) from the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        m_RectTransform = GetComponent<RectTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.html)>();
        //Initiate the x and y positions
        m_XAxis = 0.5f;
        m_YAxis = 0.5f;
    }  
  
    void OnGUI()
    {
        //The Labels show what the Sliders represent
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 20, 150, 80), "Anchor Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) X : ");
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(300, 20, 150, 80), "Anchor Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) Y : ");  
  
        //Create a horizontal Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html) that controls the x and y Positions of the anchors
        m_XAxis = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(150, 20, 100, 80), m_XAxis, -50.0f, 50.0f);
        m_YAxis = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(450, 20, 100, 80), m_YAxis, -50.0f, 50.0f);  
  
        //Detect a change in the GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html)
        if (GUI.changed[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-changed.html))
        {
            //Change the RectTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.html)'s anchored positions depending on the Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html) values
            m_RectTransform.anchoredPosition = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(m_XAxis, m_YAxis);
        }
    }
}

```

* * *
