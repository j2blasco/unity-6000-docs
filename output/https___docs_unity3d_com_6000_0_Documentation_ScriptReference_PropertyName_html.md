* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyName.html

# PropertyName
struct in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
Represents a string as an int for efficient lookup and comparison. Use this for common PropertyNames.  
  
Internally stores just an int to represent the string. A PropertyName can be created from a string but can not be converted back to a string. The same string always results in the same int representing that string. Thus this is a very efficient string representation in both memory and speed when all you need is comparison.  
  
PropertyName is serializable.  
  
ToString() is only implemented for debugging purposes in the editor it returns "theName:3737" in the player it returns "Unknown:3737".
### Constructors
Constructor | Description  
---|---  
[PropertyName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyName-ctor.html) | Initializes the PropertyName using a string.  
### Public Methods
Method | Description  
---|---  
[Equals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyName.Equals.html) | Determines whether this instance and a specified object, which must also be a PropertyName object, have the same value.  
[GetHashCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyName.GetHashCode.html) | Returns the hash code for this PropertyName.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyName.ToString.html) | For debugging purposes only. Returns the string value representing the string in the Editor. Returns "UnityEngine.PropertyName" in the player.  
### Static Methods
Method | Description  
---|---  
[IsNullOrEmpty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyName.IsNullOrEmpty.html) | Indicates whether the specified PropertyName is an Empty string.  
### Operators
Operator | Description  
---|---  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyName-operator_ne.html) | Determines whether two specified PropertyName have a different string value.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyName-operator_eq.html) | Determines whether two specified PropertyName have the same string value. Because two PropertyNames initialized with the same string value always have the same name index, we can simply perform a comparison of two ints to find out if the string value equals.  
[PropertyName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyName-operator_string.html) | Converts the string passed into a PropertyName. Additional resources: PropertyName.ctor(System.String).  
* * *
