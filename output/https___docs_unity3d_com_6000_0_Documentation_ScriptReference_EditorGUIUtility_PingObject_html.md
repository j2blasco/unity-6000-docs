* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.PingObject.html

#  [EditorGUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.html).PingObject
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
public static void PingObject([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj); 
## Declaration
public static void PingObject(int targetInstanceID); 
### Parameters
Parameter | Description  
---|---  
obj | The object to be pinged.  
### Description
Ping an object in the Scene like clicking it in an inspector.
[PingObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.PingObject.html) will cause the Hierarchy to highlight the pinged object. The pinged object does not have to be selected. For example [GameObject.Find](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.Find.html) can be used to locate an object to ping.
```
// Pings the currently selected Object
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class PingObjectExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Ping[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ping.html) Selected")]
    static void Ping[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ping.html)()
    {
        if (!Selection.activeObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeObject.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Select an object to ping");
            return;
        }  
  
        EditorGUIUtility.PingObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.PingObject.html)(Selection.activeObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeObject.html));
    }
}

```

* * *
