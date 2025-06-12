* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop-visualMode.html

#  [DragAndDrop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.html).visualMode
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
[DragAndDropVisualMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDropVisualMode.html) visualMode; 
### Description
The visual indication of the drag.
Default is [DragAndDropVisualMode.Link](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDropVisualMode.Link.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        EventType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.html) eventType = Event.current.type;
        if (eventType == EventType.DragUpdated[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.DragUpdated.html) ||
            eventType == EventType.DragPerform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.DragPerform.html))
        {
            // Show a copy icon on the drag
            DragAndDrop.visualMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop-visualMode.html) = DragAndDropVisualMode.Copy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDropVisualMode.Copy.html);  
  
            if (eventType == EventType.DragPerform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.DragPerform.html))
            {
                DragAndDrop.AcceptDrag[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.AcceptDrag.html)();
            }
            Event.current.Use();
        }
    }
}

```

* * *
