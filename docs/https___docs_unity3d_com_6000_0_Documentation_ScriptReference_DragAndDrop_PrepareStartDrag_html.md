* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.PrepareStartDrag.html

#  [DragAndDrop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.html).PrepareStartDrag
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
public static void PrepareStartDrag(); 
### Description
Clears drag & drop data.
Clears everything stored in the drag & drop object and prepares it so you can write into it for initiating a drag operation.  
  
Additional resources: [StartDrag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.StartDrag.html), [paths](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop-paths.html), [objectReferences](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop-objectReferences.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        if (Event.current.type == EventType.MouseDrag[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseDrag.html))
        {
            // Clear out drag data
            DragAndDrop.PrepareStartDrag[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.PrepareStartDrag.html)();  
  
            // Set up what we want to drag
            DragAndDrop.paths[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop-paths.html) = new string[] { "/Users/joe/myPath.txt" };  
  
            // Start the actual drag
            DragAndDrop.StartDrag[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.StartDrag.html)("Dragging title");  
  
            // Make sure no one uses the event after us
            Event.current.Use();
        }
    }
}

```

* * *
