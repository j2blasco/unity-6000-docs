* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Snapping.Snap.html

#  [Snapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Snapping.html).Snap
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
public static float Snap(float val, float snap); 
### Parameters
Parameter | Description  
---|---  
val | The value to round.  
snap | The increment to round to.  
### Returns
**float** The rounded value. 
### Description
Rounds `value` to the closest multiple of `snap`.
* * *
## Declaration
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) Snap([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) val, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) snap); 
### Parameters
Parameter | Description  
---|---  
val | The value to round.  
snap | The increment to round to.  
### Returns
**Vector2** The rounded value. 
### Description
Rounds `value` to the closest multiple of `snap`.
* * *
## Declaration
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) Snap([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) val, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) snap, [SnapAxis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SnapAxis.html) axis); 
### Parameters
Parameter | Description  
---|---  
val | The value to round.  
snap | The increment to round to.  
axis | Restrict snapping to the components on these axes.  
### Returns
**Vector3** The rounded value. 
### Description
Rounds `value` to the closest multiple of `snap`.
* * *
