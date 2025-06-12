* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.TypeTraits.IsContainer.html

#  [TypeTraits](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.TypeTraits.html).IsContainer
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
public static bool IsContainer(Type type); 
### Parameters
Parameter | Description  
---|---  
type | The type to test.  
### Returns
**bool** `true` if the given type is a container type; `false` otherwise. 
### Description
Returns `true` if the given type can be treated as a container. i.e. not primitive, pointer, enum or string. 
* * *
