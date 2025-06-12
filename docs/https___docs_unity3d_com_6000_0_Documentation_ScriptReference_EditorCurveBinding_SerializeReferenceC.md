* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.SerializeReferenceCurve.html

#  [EditorCurveBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.html).SerializeReferenceCurve(string,Type,string)
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
### Parameters
Parameter | Description  
---|---  
inPath | The transform path to the object to animate.  
inType | The type of the MonoBehaviour managing the [SerializeReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html) instance to animate.  
refID | The reference id of the SerializeReference instance to animate. Additional resources: [ManagedReferenceUtility.GetManagedReferenceIdForObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Serialization.ManagedReferenceUtility.GetManagedReferenceIdForObject.html)  
inPropertyName | The name of the property to animate on the object.  
### Description
Creates a preconfigured binding for a curve that points to a [SerializeReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html) instance field.
Fields on objects referenced with SerializeReference can be animated when the host object is derived from [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html). The animation binding to the referenced object will be based on the reference id instead of the property path, which makes it possible to correctly resolve the animation even when there are changes in the path leading to the referenced object. For example, if the object is referenced from within an array, the animation is retained even if the position of the object within the array changes.
* * *
