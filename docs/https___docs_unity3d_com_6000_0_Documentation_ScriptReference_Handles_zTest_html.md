* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-zTest.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).zTest
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
[Rendering.CompareFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CompareFunction.html) zTest; 
### Description
zTest of the handles.
Default value is Always.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/HandleZTest.png)  
_This anchor shows the first downwards collider intersection. Depth pass lines appears green, depth fail, red._  
  
To use this example, attach this script to the object you wish to display the anchor :
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
[ExecuteInEditMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExecuteInEditMode.html)]
public class SampleAnchor : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnDrawGizmosSelected()
    {
        Ray[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) ray = new Ray[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html)(transform.position, Vector3.down[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-down.html));
        RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) hit;
        if (Physics.Raycast[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html)(ray, out hit))
        {
            Handles.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-color.html) = Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html);
            Handles.zTest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-zTest.html) = UnityEngine.Rendering.CompareFunction.LessEqual;
            Handles.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawLine.html)(transform.position, hit.point);
            Handles.DrawWireDisc[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawWireDisc.html)(hit.point, hit.normal, 0.5f);  
  
            Handles.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-color.html) = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);
            Handles.zTest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-zTest.html) = UnityEngine.Rendering.CompareFunction.Greater;
            Handles.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawLine.html)(transform.position, hit.point);
            Handles.DrawWireDisc[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawWireDisc.html)(hit.point, hit.normal, 0.5f);
        }
    }
}

```

* * *
