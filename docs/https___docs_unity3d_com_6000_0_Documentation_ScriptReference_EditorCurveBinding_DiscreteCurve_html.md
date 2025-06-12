* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.DiscreteCurve.html

#  [EditorCurveBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.html).DiscreteCurve
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
public static [EditorCurveBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.html) DiscreteCurve(string inPath, Type inType, string inPropertyName); 
### Parameters
Parameter | Description  
---|---  
inPath | The transform path to the object to animate.  
inType | The type of the object to animate.  
inPropertyName | The name of the property to animate on the object.  
### Description
Creates a preconfigured binding for a curve where values should not be interpolated.
Use discrete curves for properties with discontinuous values, or for values that should not be interpolated. For example, use [EditorCurveBinding.DiscreteCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.DiscreteCurve.html) for enums or hashes. Discrete curves only support properties of type Int (with the DiscreteEvaluation attribute) or Enum. If you attempt to bind discrete curves to other types, a warning will be logged and a default interpolated float curve binding will be returned (see [EditorCurveBinding.FloatCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.FloatCurve.html)). 
* * *
