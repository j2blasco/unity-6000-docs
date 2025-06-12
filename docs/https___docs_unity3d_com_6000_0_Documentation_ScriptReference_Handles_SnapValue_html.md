* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.SnapValue.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).SnapValue
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
public static float SnapValue(float value, float snap); 
### Parameters
Parameter | Description  
---|---  
value | The value to snap.  
snap | The increment to snap to.  
### Returns
**float** If snapping is [active](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-active.html), rounds `value` to the closest multiple of `snap` (snap can only be positive). 
### Description
Rounds `value` to the closest multiple of `snap` if snapping is [active](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-active.html). Note that snap can only be positive.
* * *
## Declaration
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) SnapValue([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) value, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) snap); 
### Parameters
Parameter | Description  
---|---  
value | The value to snap.  
snap | The increment to snap to.  
### Returns
**Vector3** If snapping is [active](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-active.html), rounds `value` to the closest multiple of `snap` (snap can only be positive). 
### Description
Rounds `value` to the closest multiple of `snap` if snapping is [active](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-active.html). Note that snap can only be positive.
* * *
## Declaration
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) SnapValue([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) value, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) snap); 
### Parameters
Parameter | Description  
---|---  
value | The value to snap.  
snap | The increment to snap to.  
### Returns
**Vector2** If snapping is [active](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-active.html), rounds `value` to the closest multiple of `snap` (snap can only be positive). 
### Description
Rounds `value` to the closest multiple of `snap` if snapping is [active](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-active.html). Note that snap can only be positive.
* * *
