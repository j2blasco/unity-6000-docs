* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.PPtrCurve.html

#  [EditorCurveBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.html).PPtrCurve
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
public static [EditorCurveBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.html) PPtrCurve(string inPath, Type inType, string inPropertyName); 
### Parameters
Parameter | Description  
---|---  
inPath | The transform path to the object to animate.  
inType | The type of the object to animate.  
inPropertyName | The name of the property to animate on the object.  
### Description
Creates a preconfigured binding for a curve that points to an Object.
Use PPtr curves for curves that manipulate references to Objects. For example, use [EditorCurveBinding.PPtrCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.PPtrCurve.html) for [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) curves or [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) curves.
* * *
