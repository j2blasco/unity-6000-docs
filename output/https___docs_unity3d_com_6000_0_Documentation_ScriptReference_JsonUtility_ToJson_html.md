* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JsonUtility.ToJson.html

#  [JsonUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JsonUtility.html).ToJson
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
public static string ToJson(object obj); 
## Declaration
public static string ToJson(object obj, bool prettyPrint); 
### Parameters
Parameter | Description  
---|---  
obj | The object to convert to JSON form.  
prettyPrint | If true, format the output for readability. If false, format the output for minimum size. Default is false.  
### Returns
**string** The object's data in JSON format. 
### Description
Generate a JSON representation of the public fields of an object.
Internally, this method uses the Unity serializer; therefore the object you pass in must be supported by the serializer: it must be a MonoBehaviour, ScriptableObject, or plain class/struct with the Serializable attribute applied. The types of fields that you want to be included must be supported by the serializer; unsupported fields will be ignored, as will private fields, static fields, and fields with the NonSerialized attribute applied.  
  
Any plain class or structure is supported, as well as classes derived from MonoBehaviour or ScriptableObject. Other engine types are not supported. (In the Editor only, you can use [EditorJsonUtility.ToJson](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorJsonUtility.ToJson.html) to serialize other engine types to JSON).  
  
If the object contains fields with references to other Unity objects, those references are serialized by recording the InstanceID for each referenced object. Because the Instance ID acts like a handle to the in-memory object instance, the JSON string can only be deserialized back during the same session of the Unity engine.  
  
Note that while it is possible to pass primitive types to this method, the results may not be what you expect; instead of serializing them directly, the method will attempt to serialize their public instance fields, producing an empty object as a result. Similarly, passing an array to this method will not produce a JSON array containing each element, but an object containing the public fields of the array object itself (of which there are none). To serialize the actual content of an array or primitive type, it is necessary to wrap it in a class or struct.  
  
This method can be called from background threads. You should not alter the object that you pass to this function while it is still executing.  
  
Additional resources: [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html), [ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html), [Object.GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html)
```
using UnityEngine;  
  
public class PlayerState : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public string playerName;
    public int lives;
    public float health;  
  
    public string SaveToString()
    {
        return JsonUtility.ToJson[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JsonUtility.ToJson.html)(this);
    }  
  
    // Given:
    // playerName = "Dr Charles"
    // lives = 3
    // health = 0.8f
    // SaveToString returns:
    // {"playerName":"Dr Charles","lives":3,"health":0.8}
}

```

* * *
