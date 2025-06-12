* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorJsonUtility.FromJsonOverwrite.html

#  [EditorJsonUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorJsonUtility.html).FromJsonOverwrite
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
public static void FromJsonOverwrite(string json, object objectToOverwrite); 
### Parameters
Parameter | Description  
---|---  
json | The JSON representation of the object.  
objectToOverwrite | The object to overwrite.  
### Description
Overwrite data in an object by reading from its JSON representation.
This is similar to [JsonUtility.FromJsonOverwrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JsonUtility.FromJsonOverwrite.html), but it supports any engine object.  
  
Note that using this method with a struct may not do what you expect because structs are passed to the method by value and not by reference. This means that instead of the method overwriting your original struct, a boxed copy of the struct is passed into the method and overwritten. You can avoid this by making your own boxed copy of the struct to pass into the method and then copying the values back again after the method returns. See example below.  
  
Even when you do this, Unity’s built-in structs (such as [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) or [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html)) cannot be directly passed to the method, so you must enclose Unity’s built-in structs inside a wrapper class or struct. 
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
[System.Serializable]
struct MyStruct
{
    public int value;
}  
  
public class StructExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        MyStruct myStruct = new MyStruct();
        object boxedStruct = myStruct;
        var json = @"{ ""value"" : 42 }";
        EditorJsonUtility.FromJsonOverwrite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorJsonUtility.FromJsonOverwrite.html)(json, boxedStruct);
        myStruct = (MyStruct)boxedStruct;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("myStruct.value = " + myStruct.value);
    }
}

```

* * *
