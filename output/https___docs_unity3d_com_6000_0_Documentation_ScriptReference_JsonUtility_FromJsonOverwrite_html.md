* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JsonUtility.FromJsonOverwrite.html

#  [JsonUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JsonUtility.html).FromJsonOverwrite
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
objectToOverwrite | The object that should be overwritten.  
### Description
Overwrite data in an object by reading from its JSON representation.
This method is very similar to [JsonUtility.FromJson](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JsonUtility.FromJson.html), except that instead of creating a new object and loading the JSON data into it, it loads the JSON data into an existing object. This allows you to update the values stored in classes or objects without any allocations.  
  
Internally, this method uses the Unity serializer; therefore the object you pass in must be supported by the serializer: it must be a MonoBehaviour, ScriptableObject, or plain class/struct with the Serializable attribute applied. The types of fields that you want to be overwritten must be supported by the serializer; unsupported fields will be ignored, as will private fields, static fields, and fields with the NonSerialized attribute applied.  
  
Any plain class or structure is supported, along with classes derived from MonoBehaviour or ScriptableObject. Other engine types are not supported. In the Editor only, you can use [EditorJsonUtility.FromJsonOverwrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorJsonUtility.FromJsonOverwrite.html) to overwrite other engine objects.  
  
If a field of the object is not present in the JSON representation, that field will be left unchanged.  
  
The version of this method that takes a string can be called from background threads. You should not alter the object that is being overwritten while the function is running. The version of this method that takes a TextAsset cannot be called from a background thread.
```
using UnityEngine;  
  
public class PlayerState : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public string playerName;
    public int lives;
    public float health;  
  
    public void Load(string savedData)
    {
        JsonUtility.FromJsonOverwrite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JsonUtility.FromJsonOverwrite.html)(savedData, this);
    }  
  
    // Given JSON input:
    // {"lives":3, "health":0.8}
    // the Load function will change the object on which it is called such that
    // lives == 3 and health == 0.8
    // the 'playerName' field will be left unchanged
}

```

* * *
