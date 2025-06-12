* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.html

# EditorCurveBinding
struct in UnityEditor
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
Defines how a curve is attached to an object that it controls.
### Properties
Property | Description  
---|---  
[isDiscreteCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding-isDiscreteCurve.html) | Returns true if the binding is a discrete curve. Returns false otherwise. (Read Only)  
[isPPtrCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding-isPPtrCurve.html) | Returns true if the binding is an object curve. Returns false otherwise (Read Only)  
[isSerializeReferenceCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding-isSerializeReferenceCurve.html) | Returns true if the binding is to a curve that points to field on a SerializeReference instance. Returns false otherwise. (Read Only)  
[path](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding-path.html) | The transform path of the object that is animated.  
[propertyName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding-propertyName.html) | The name of the property to be animated.  
[type](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding-type.html) | The type of the property to be animated.  
### Static Methods
Method | Description  
---|---  
[DiscreteCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.DiscreteCurve.html) | Creates a preconfigured binding for a curve where values should not be interpolated.  
[FloatCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.FloatCurve.html) | Creates a preconfigured binding for a float curve.  
[PPtrCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.PPtrCurve.html) | Creates a preconfigured binding for a curve that points to an Object.  
[SerializeReferenceCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.SerializeReferenceCurve.html) | Creates a preconfigured binding for a curve that points to a SerializeReference instance field.  
* * *
