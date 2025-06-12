* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.AddPropertyModification.html

#  [AnimationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.html).AddPropertyModification
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
public static void AddPropertyModification([EditorCurveBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.html) binding, [PropertyModification](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyModification.html) modification, bool keepPrefabOverride); 
### Parameters
Parameter | Description  
---|---  
binding | Description of the animation clip curve being modified.  
modification | Object property being modified.  
keepPrefabOverride | Indicates whether to retain modifications when the targeted object is an instance of a Prefab.  
### Description
Marks a property as currently being animated.
This method uses the animation recording system to add a property to the Animation mode snapshot. A property is added when the user modifies its value through scripting, in the Inspector window, and so on.
* * *
