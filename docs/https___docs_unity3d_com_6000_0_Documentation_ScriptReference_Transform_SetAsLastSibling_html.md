* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.SetAsLastSibling.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).SetAsLastSibling
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html "Go to Transform Component in the Manual")
## Declaration
public void SetAsLastSibling(); 
### Description
Move the transform to the end of the local transform list.
```
using UnityEngine;
using System.Collections;
using UnityEngine.UI; //Required when using UI Elements.
using UnityEngine.EventSystems; // Required when using event data.  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html), IPointerDownHandler
{
    public RectTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.html) panelRectTransform;  
  
    //Invoked when the mouse pointer goes down on a UI element.
    public void OnPointerDown(PointerEventData data)
    {
        // Puts the panel to the front as it is now the last UI element to be drawn.
        panelRectTransform.SetAsLastSibling();
    }
}

```

* * *
