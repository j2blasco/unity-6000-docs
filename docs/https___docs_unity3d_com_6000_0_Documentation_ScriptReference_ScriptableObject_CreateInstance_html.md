* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html

#  [ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html).CreateInstance
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ScriptableObject.html "Go to ScriptableObject Component in the Manual")
## Declaration
public static [ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html) CreateInstance(string className); 
## Declaration
public static [ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html) CreateInstance(Type type); 
### Parameters
Parameter | Description  
---|---  
className | The type of the ScriptableObject to create, as the name of the type.  
type | The type of the ScriptableObject to create, as a System.Type instance.  
### Returns
**ScriptableObject** The created ScriptableObject. 
### Description
Creates an instance of a scriptable object.
To easily create a ScriptableObject instance that is bound to a .asset file via the Editor user interface, consider using [CreateAssetMenuAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CreateAssetMenuAttribute.html).
* * *
## Declaration
public static T CreateInstance(); 
### Returns
**T** The created ScriptableObject. 
### Description
Creates an instance of a scriptable object.
To easily create a ScriptableObject instance that is bound to a .asset file via the Editor user interface, consider using [CreateAssetMenuAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CreateAssetMenuAttribute.html).
* * *
